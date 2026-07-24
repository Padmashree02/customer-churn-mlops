from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from src.utils.model_utils import save_model

from sklearn.pipeline import Pipeline

from sklearn.metrics import (accuracy_score, f1_score, precision_score, recall_score)

import mlflow
import mlflow.sklearn
#mlflow.set_tracking_uri("sqlite:/C:/Users/Padmashree/customer-churn-mlops/mlflow.db")
#mlflow.set_experiment("Customer-Churn-Prediction")

class ModelTrainer:

    def train_and_evaluate(self,preprocessor, X_train,y_train, X_test, y_test):
        
        models={
            "LogisticRegression": LogisticRegression(),

            "RandomForest": RandomForestClassifier(),

            "XGBoost": XGBClassifier()
        }

        trained_models={}
        scores={}

        for name,model in models.items():

            pipeline=Pipeline(
                steps=[
                    (
                        "preprocessor", preprocessor
                    ),
                    (
                        "model",model
                    )
                ]
            )
            
            # MLflow- experiment tracking
            with mlflow.start_run(run_name=name):
                
                # Training phase
                pipeline.fit(X_train,y_train)

                trained_models[name]=pipeline
                
                mlflow.log_param("model_name",name)

                # Testing phase
                predictions=pipeline.predict(X_test)

                accuracy=accuracy_score(y_test,predictions)
                mlflow.log_metric("accuracy", accuracy)

                f1=f1_score(y_test, predictions, pos_label=1)
                mlflow.log_metric("f1_score",f1)

                precision=precision_score(y_test,predictions,pos_label=1)
                mlflow.log_metric("precision",precision)

                recall=recall_score(y_test,predictions,pos_label=1)
                mlflow.log_metric("recall",recall)

                mlflow.sklearn.log_model(sk_model=pipeline,name=name)

                scores[name]={
                    "accuracy": accuracy,
                    "f1": f1,
                    "precision": precision,
                    "recall": recall
                }

        return trained_models, scores
        
    def get_best_model(self,models, scores):
        best_model_name=max(scores, key=lambda x: scores[x]['f1'])
        best_model=models[best_model_name]
        save_model(best_model,"models/best_model.pkl")
        return best_model_name
    
#preprocess data-> train model-> track parameters-> track metrics-> save artifacts-> store model

'''
    def evaluate(self, models, X_test, y_test):
        scores={}

        for name,model in models.items():
            predictions=model.predict(X_test)

            accuracy=accuracy_score(y_test,predictions)
            mlflow.log_metric("accuracy", accuracy)

            f1=f1_score(y_test, predictions, pos_label=1)
            mlflow.log_metric("f1_score",f1)

            precision=precision_score(y_test,predictions,pos_label=1)
            mlflow.log_metric("precision",precision)

            recall=recall_score(y_test,predictions,pos_label=1)
            mlflow.log_metric("recall",recall)

            mlflow.sklearn.log_model(model,name)

            scores[name]={
                "accuracy": accuracy,
                "f1": f1,
                "precision": precision,
                "recall": recall
            }

        return scores
'''