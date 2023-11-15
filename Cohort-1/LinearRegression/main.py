from typing import List
import pandas as pd
from fastapi import FastAPI

from pydantic import BaseModel
import torch.nn as nn
import torch

app = FastAPI()

class LinearRegressionModel(nn.Module):
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)

model = LinearRegressionModel()
model.load_state_dict(torch.load('linear_regression_model.pth'))
model.eval()

class CarYears(BaseModel):
    years: List[float]

# Prediction endpoint
@app.post("/predict/")
def predict(car_years: CarYears):
    years_int = [int(year) for year in car_years.years]
    input_data = pd.DataFrame({'year': years_int})
    input_tensor = torch.tensor(input_data.values, dtype=torch.float32)
    predictions = model(input_tensor).detach().numpy().flatten()  # Ensure predictions are 1D
    prediction_data = pd.DataFrame({
        'year': years_int,
        'price': predictions.tolist()  # Convert numpy array to list if needed
    })
    print("Input years:", years_int)
    print("Predictions:", predictions.tolist())

    return prediction_data.to_dict(orient='records')