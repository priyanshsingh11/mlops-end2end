from src.pipline.training_pipeline import TrainPipeline

pipeline = TrainPipeline()
pipeline.start_data_ingestion() # Call this instead of run_pipeline
