from pathlib import Path
import mlflow


def setup_mlflow():

    project_root = Path(__file__).resolve().parents[2]

    mlflow_db = project_root / "mlflow.db"

    mlflow.set_tracking_uri(f"sqlite:///{mlflow_db}")

    mlflow.set_experiment("Customer-Churn-Prediction")