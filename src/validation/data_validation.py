from src.utils.logger import logger

class DataValidation:
    def __init__(self,df):
        self.df=df
    
    def validate_columns(self):
        required_columns=[
            'customerID',
            'gender',
            'MonthlyCharges',
            'TotalCharges',
            'Churn'
        ]

        missing=[]

        for col in required_columns:
            if col not in self.df.columns:
                missing.append(col)

        if len(missing)>0:
            logger.error(f'Missing columns:{missing}')
            return False
        
        logger.info('All required columns present')
        return True
    
    def check_missing_values(self):
        missing=self.df.isnull().sum()
        logger.info(f'\n{missing}')
        return missing