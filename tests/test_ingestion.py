from src.ingestion.data_ingestion import DataIngestion

def test_data_loading():
    ingestion = DataIngestion()
    df = ingestion.load_data()
    assert len(df)>0