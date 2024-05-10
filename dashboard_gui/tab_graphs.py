import pyqtgraph as pg
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QProgressBar
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer
import psutil
import GPUtil
import pyamdgpuinfo

class GraphsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initTimers()

    def initUI(self):
        layout = QVBoxLayout()

        # Create the plots for loss and performance metrics
        self.lossPlot = pg.PlotWidget(title="Loss Metrics")
        self.trainingLossCurve = self.lossPlot.plot(pen='r', name="Training Loss")
        self.validationLossCurve = self.lossPlot.plot(pen='b', name="Validation Loss")

        self.performancePlot = pg.PlotWidget(title="Performance Metrics")
        self.accuracyCurve = self.performancePlot.plot(pen='g', name="Accuracy")
        self.perplexityCurve = self.performancePlot.plot(pen='y', name="Perplexity")

        # Resource usage indicators (simple progress bars here for illustration)
        self.cpuUsageBar = QProgressBar()
        self.cpuUsageBar.setFormat("CPU Usage: %p%")
        self.memoryUsageBar = QProgressBar()
        self.memoryUsageBar.setFormat("Memory Usage: %p%")

        # GPU usage indicators
        self.gpuUsageBar = QProgressBar()
        self.gpuUsageBar.setMaximum(100)
        self.gpuUsageBar.setFormat("GPU Load: %p%")
        
        self.vramUsageBar = QProgressBar()
        self.vramUsageBar.setMaximum(100)
        self.vramUsageBar.setFormat("VRAM Usage: %p%")

        resourceLayout = QHBoxLayout()
        resourceLayout.addWidget(QLabel("Resource Usage:"))
        resourceLayout.addWidget(self.gpuUsageBar)
        resourceLayout.addWidget(self.vramUsageBar)
        resourceLayout.addWidget(self.cpuUsageBar)
        resourceLayout.addWidget(self.memoryUsageBar)

        # Training progress
        self.trainingProgress = QProgressBar()
        self.trainingProgress.setMaximum(100)  # Assume max epochs or steps
        self.trainingProgress.setFormat("Training Progress: %p%")

        # Adding widgets to the main layout
        layout.addWidget(self.lossPlot)
        layout.addWidget(self.performancePlot)
        layout.addLayout(resourceLayout)
        layout.addWidget(self.trainingProgress)

        self.setLayout(layout)


    def update_metrics(self, training_loss, validation_loss, accuracy, perplexity, gpu_usage, cpu_usage, memory_usage, epoch, total_epochs):
        self.trainingLossCurve.setData(training_loss)
        self.validationLossCurve.setData(validation_loss)
        self.accuracyCurve.setData(accuracy)
        self.perplexityCurve.setData(perplexity)
        self.gpuUsageBar.setValue(gpu_usage)
        self.cpuUsageBar.setValue(cpu_usage)
        self.memoryUsageBar.setValue(memory_usage)
        self.trainingProgress.setValue((epoch / total_epochs) * 100)

    def initTimers(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_resource_usage)
        self.timer.start(1000)  # Update every second

    def update_resource_usage(self):
        # Update CPU usage
        cpu_usage = int(psutil.cpu_percent())  # Convert float to int
        self.cpuUsageBar.setValue(cpu_usage)

        # Update memory usage
        memory = psutil.virtual_memory()
        memory_usage = int(memory.percent)  # Convert float to int
        self.memoryUsageBar.setValue(memory_usage)
        gpu_load, vram_load = self.get_gpu_usage()
        if gpu_load is not None and vram_load is not None:
            self.gpuUsageBar.setValue(gpu_load)
            #self.gpuUsageLabel.setText(f"GPU Load: {gpu_load}%")
            self.vramUsageBar.setValue(vram_load)
            #self.vramUsageLabel.setText(f"VRAM Usage: {vram_load}%")

    def get_gpu_usage(self):
        # NVIDIA GPU Check
        gpus = GPUtil.getGPUs()
        if gpus:
            gpu = gpus[0]  # Assuming single GPU
            gpu_load = int(gpu.load * 100)
            vram_load = query_vram_usage
            return gpu_load, vram_load

        # AMD GPU Check
        if pyamdgpuinfo.detect_gpus():
            first_gpu = pyamdgpuinfo.get_gpu(0)
            vram_load = first_gpu.query_vram_usage()
            gpu_load = int(first_gpu.query_load() * 100)
            return gpu_load, vram_load

        return None, None



if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    ex = GraphsTab()
    ex.show()
    sys.exit(app.exec_())
