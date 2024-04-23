from fastapi import FastAPI, File, UploadFile
from tensorflow import keras
from keras.models import Sequential, load_model
import numpy as np
from PIL import Image
import io
import sys

app = FastAPI()

#Function to load keras model for digit prediction
def load_keras_model(path: str) -> Sequential:
    return load_model(path)

#function to make prediction from array of grayscale values
def predict_digit(model: Sequential, data_point: list) -> str:
    data_array = np.array(data_point,dtype=np.float64)/ 255.0
    prediction = model.predict(data_array.reshape(1,-1))
    predicted_digit = np.argmax(prediction)
    return str(predicted_digit)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    img_bytes = await file.read()
    img = Image.open(io.BytesIO(img_bytes)).convert('L').resize((28, 28))
    img_array = np.array(img).reshape(784)

    model_path = "DigitPredictor.keras"
    model = load_keras_model(model_path)
    digit = predict_digit(model, img_array)
    return {"digit": digit}

