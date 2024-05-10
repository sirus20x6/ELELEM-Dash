import imgui
from imgui.integrations.glfw import GlfwRenderer
import glfw
import sqlite3

def fetch_data():
    conn = sqlite3.connect("pythonsqlite.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data")
    rows = cursor.fetchall()
    conn.close()
    return rows

def main():
    if not glfw.init():
        return

    window = glfw.create_window(1280, 720, "Data Visualization", None, None)
    glfw.make_context_current(window)
    imgui.create_context()
    renderer = GlfwRenderer(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        imgui.new_frame()

        data = fetch_data()
        if imgui.begin("Database Data"):
            for row in data:
                imgui.text(str(row))
        imgui.end()

        imgui.render()
        renderer.render(imgui.get_draw_data())
        glfw.swap_buffers(window)

    renderer.shutdown()
    glfw.terminate()

if __name__ == "__main__":
    main()
