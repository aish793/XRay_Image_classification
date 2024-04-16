import sys
from Xray_src.cloud_storage.s3_ops import S3Operation
import os
from Xray_src.entity.config_entity import ModelPusherConfig
from Xray_src.exception import XRayException
from Xray_src.logger import logging


class ModelPusher:
    def __init__(self, model_pusher_config: ModelPusherConfig):

        self.model_pusher_config = model_pusher_config
        self.s3 = S3Operation()

    def initiate_model_pusher(self):

        """
        Method Name :   initiate_model_pusher

        Description :   This method initiates model pusher.

        Output      :    Model pusher artifact
        """
        logging.info("Entered initiate_model_pusher method of Modelpusher class")
        try:
            # Uploading the best model to s3 bucket
            self.s3.upload_file(
                os.path.join("..", "..", "model", "model_training", "model.pt"),
                "model.pt",
                "lungxrayimgs",
                remove=False,
            )
            logging.info("Uploaded best model to s3 bucket")
            logging.info("Exited initiate_model_pusher method of ModelTrainer class")


        except Exception as e:
            raise e