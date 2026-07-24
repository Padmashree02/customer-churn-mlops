from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

import pandas as pd

class DataTransformation:
    def get_transformer(self,df):
        
        df['TotalCharges']=pd.to_numeric(df['TotalCharges'],errors='coerce')
        print(df.dtypes)

        numerical_columns=[
            'tenure',
            'MonthlyCharges',
            'TotalCharges'
        ]

        categorical_columns=[
            'gender',
            'Partner',
            'Dependents',
            'PhoneService',
            'Contract'
        ]

        numerical_pipeline=Pipeline(
            steps=[
                (
                    'imputer',
                    SimpleImputer(strategy='median')
                ),

                (
                    'scaler',
                    StandardScaler()
                )
            ]
        )

        categorical_pipeline=Pipeline(
            steps=[
                (
                    'imputer',
                    SimpleImputer(strategy='most_frequent')
                ),
                (
                    'encoder',
                    OneHotEncoder(handle_unknown='ignore')
                )
            ] 
        )

        preprocessor=ColumnTransformer(
            [
                (
                    'num',
                    numerical_pipeline,
                    numerical_columns
                ),

                (
                    'cat',
                    categorical_pipeline,
                    categorical_columns
                )
            ]
        )

        return preprocessor