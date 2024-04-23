FastAPI MNIST digit prediction project:

# FastAPI MNIST Digit Prediction

This project provides a simple API for predicting handwritten digits using a pre-trained Keras model. The API accepts images of handwritten digits, processes them, and returns the predicted digit.


## Usage

1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
2. Open your web browser and navigate to `http://localhost:8000/docs` to access the Swagger UI.
3. Upload an image of a handwritten digit from the `Figures` folder or any other image to the `/predict` endpoint to get the predicted digit.

## File Descriptions

- `main.py`: Contains the FastAPI application without resizing the uploaded image.
- `main2.py`: Contains the FastAPI application with resizing the uploaded image to 28x28 pixels.

## Sample Images

The `Figures` folder contains sample images of handwritten digits for testing the API.

## Contributors

- NAKKA KIRAN KUMAR
