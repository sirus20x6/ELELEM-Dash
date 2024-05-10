from src.log_metrics import log_metrics
from src.db_utils import setup_database
import training_loop  # Assume this is a module where the actual model training happens

def main():
    db_path = 'db/training_metrics.db'
    setup_database(db_path)  # Ensure the database is set up
    # Run the training loop and log metrics
    training_loop.run_training(db_path)

if __name__ == "__main__":
    main()
