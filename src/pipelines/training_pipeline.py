from sklearn.model_selection import train_test_split

from src.ingestion.data_ingestion import DataIngestion
from src.validation.data_validation import DataValidation
from src.feature_engineering.data_transformation import DataTransformation
from src.training.model_trainer import ModelTrainer

obj=DataIngestion()

df=obj.load_data()

validator=DataValidation(df)

if validator.validate_columns():

    validator.check_missing_values()

    transformer= DataTransformation()

    preprocessor= transformer.get_transformer(df)

    X=df.drop(columns=['Churn'])
    y=df['Churn'].map({
        'No':0,
        "Yes":1
                       }) 
    #to convert the target values to normal format
    
    #print("Target values:", y.unique())

    #X_transformed= preprocessor.fit_transform(X)

    X_train, X_test, y_train, y_test= train_test_split(X,y,test_size=0.2,random_state=42)

    from src.utils.mlflow_utils import setup_mlflow
    setup_mlflow()

    trainer=ModelTrainer()

    models, results=trainer.train_and_evaluate(preprocessor,X_train, y_train, X_test, y_test)
    print("\n",results)

    best_model_name=trainer.get_best_model(models, results)
    print(f"\nBest model: {best_model_name}")

#load data-> validate data-> seperate feature/input & target/output-> handle missing values-> encode categories-> scale numbers-> transformed data
#load data-> validate data-> transformed data-> spilt train/test-> train models-> evaluate models-> compare results
#run in terminal: python -m src.pipelines.training_pipeline