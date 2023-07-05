from abc import ABC, abstractmethod

from pydantic import BaseModel, validator


class RougeEvaluator(ABC,BaseModel):
    ground_truth: str
    predicted: str
    delimiter:str = " "

    @validator("ground_truth",pre=True)
    @classmethod
    def check_ground_truth(cls, value):
        if value is None:
            raise ValueError("Ground truth is a mandatory input and cannot be null.")
        return value

    @validator("predicted")
    @classmethod
    def check_predicted(cls, value):
        if value is None:
            raise ValueError("Predicted is a mandatory input and cannot be null.")
        return value

    @abstractmethod
    def evaluate(self):
        pass