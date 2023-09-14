# Liquid_level_indicator

## Overview
This project focuses on predicting the liquid level (LOW, MEDIUM, HIGH) in containers using machine learning techniques. It involves training a neural network model on a dataset of images showcasing different water capacities. Additionally, the project incorporates real-time testing using a PC camera, OpenCV library, OPC-UA protocol, and client-server architecture. The results are displayed and analyzed within a Jupyter Notebook environment.

## Key features
1. Data Collection: Curated a dataset of images with varying liquid levels to train the predictive model.

2. Real-time Testing: Utilized OpenCV to capture real-time images from a PC camera, ensuring that the model can make predictions on new data as it becomes available.

3. Client-Server Architecture: Employed OPC-UA for seamless communication between the camera and the predictive model, ensuring efficient data transfer.

4. Model Selection: Implemented the VGG16 architecture, a powerful convolutional neural network model typically used for image recognition tasks.

5. Validation Accuracy: Achieved an impressive validation accuracy of 90.48% on the test dataset, highlighting the model's effectiveness.


## Usage

1. Train the model: Use the provided dataset to train the liquid level prediction model.

2. Real-time Testing: Capture images using a PC camera and send them to the model using the OPC-UA protocol.

3. Predictions: The model will analyze the images and provide predictions for the liquid level.

4. Display Results: View the results and analysis in the Jupyter Notebook interface.
