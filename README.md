# BackgroundCVzone

A computer vision project for background processing and manipulation using OpenCV and CVZone.

## Overview

BackgroundCVzone is a Python application that leverages computer vision techniques to detect, separate, and manipulate backgrounds in images and video streams. It uses OpenCV for core vision operations and the CVZone library for enhanced functionality.

## Features

- Background removal and replacement
- Real-time video processing
- Person segmentation using Mediapipe
- Custom background effects

## Requirements

- Python 3.7+
- OpenCV
- NumPy
- Mediapipe
- CVZone

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/BackgroundCVzone.git
   cd BackgroundCVzone
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

```bash
python main.py
```