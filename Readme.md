# Bustard Vision

**Bustard Vision** is a project focused on detecting and monitoring the Great Indian Bustard using advanced computer vision techniques. The project leverages the YOLOv8n model to achieve high-performance object detection, trained on a meticulously annotated dataset.

## Project Overview

This project involves training a YOLOv8n model to identify and track the Great Indian Bustard, a critically endangered bird species. The model was trained using an extensive dataset annotated with CVAT, demonstrating YOLOv8n's effectiveness in delivering accurate and efficient results.

## Key Results

- **Precision**: 62.8%
- **Recall**: 68.3%
- **mAP50**: 67.0%
- **mAP50-95**: 31.3%

### Model Specifications

- **Model Type**: YOLOv8n
- **Speed (A100 TensorRT)**: 0.99 ms
- **Parameters**: 3.2M
- **FLOPs**: 8.7B

## Training Details

- **Epochs**: 250
- **Learning Rate**: 3.58E-05
- **Model Size (pixels)**: 640

## Data Annotation

The dataset was meticulously annotated using [CVAT](https://github.com/openvinotoolkit/cvat), ensuring high-quality training data for the model.
