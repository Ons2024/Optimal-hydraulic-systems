# Optimal Hydraulic Systems - Valve Condition Prediction

This project is a web application for predicting the condition of a hydraulic system valve using sensor data and machine learning. It provides a user-friendly interface to input a cycle ID and receive a prediction about the valve's state, along with the model's confidence and the ground truth for comparison.

---

## Features

- Predicts valve condition (normal/faulty) based on sensor data  
- Uses pre-trained machine learning models including XGBoost, RandomForest, SVM, and others  
- Flask-based web interface for easy interaction  
- Data preprocessing and feature extraction utilities for raw sensor data  
- Dockerfile included for easy containerized deployment  


## Dataset Description

The data used in this project comes from the **Condition Monitoring of Hydraulic Systems** dataset, available from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/447/condition+monitoring+of+hydraulic+systems). It was collected from a hydraulic test rig designed to simulate normal operations and various fault scenarios.

### Sensors Used
Key sensors involved in this project:
- `PS2.txt`: Pressure sensor (100 Hz)
- `FS1.txt`: Flow rate sensor (10 Hz)


### Target Variable
The valve condition is provided in `profile.txt` and categorized as:
- `100%`: Optimal valve condition  
- `<100%`: Faulty behavior (lag or failure)




