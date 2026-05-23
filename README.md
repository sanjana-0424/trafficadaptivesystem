# Adaptive Traffic Signal System using Python & OpenCV

## Project Overview

Traditional traffic signal systems use fixed timing for all roads, which often causes unnecessary waiting time and traffic congestion. This project aims to solve this issue by creating an adaptive traffic signal system that dynamically adjusts signal timing based on real-time vehicle density.

The project uses Python, OpenCV, and computer vision techniques to detect vehicles from traffic videos, count vehicles, and allocate signal timing according to traffic density.

---

# Features

* Vehicle detection using OpenCV
* Motion detection using background subtraction
* Vehicle counting system
* Adaptive traffic signal timing
* GUI-based traffic signal simulation
* Real-time traffic video processing

---

# Technologies Used

* Python
* OpenCV
* Tkinter
* Computer Vision
* GitHub

---

# Installations Performed

## 1. Install Python

Download and install Python from:
https://www.python.org/downloads/

---

## 2. Install Visual Studio Code

Download VS Code from:
https://code.visualstudio.com/

---

## 3. Install OpenCV

Run the following command in terminal:

```bash
pip3 install opencv-python
```

This installs the OpenCV library used for:

* video processing
* motion detection
* vehicle detection
* computer vision tasks

---

# Libraries Used

## random

Used to generate random traffic values during simulation.

```python
import random
```

---

## time

Used for delays and countdown timers.

```python
import time
```

---

## tkinter

Used to create GUI traffic signal windows.

```python
import tkinter as tk
```

---

## cv2 (OpenCV)

Used for:

* video processing
* motion detection
* vehicle counting
* computer vision

```python
import cv2
```

---

# Terminal Commands Used

## Run Python File

```bash
python3 filename.py
```

Example:

```bash
python3 smart_signal.py
```

---

## Change Directory

```bash
cd traffic_project
```

Used to move terminal into the project folder.

---

## Show Files

```bash
ls
```

Displays all files in current folder.

---

## Stop Running Program

```bash
CONTROL + C
```

Used to stop running terminal programs.

---

# Project Development Process

## Step 1 — Python Setup

* Installed Python
* Installed VS Code
* Created first Python file

---

## Step 2 — Adaptive Traffic Logic

Built traffic signal timing logic using:

* if-else conditions
* functions
* loops

Logic:

* More traffic → More green signal time
* Less traffic → Less green signal time

---

## Step 3 — Dynamic Traffic Simulation

Generated random traffic values using:

```python
random.randint(0,30)
```

Used loops and timers to simulate real-time traffic updates.

---

## Step 4 — Signal Switching

Implemented traffic signal switching system:

* GREEN signal
* RED signal
* road-by-road execution

---

## Step 5 — Countdown Timer

Added countdown timer for realistic signal simulation.

Used:

```python
time.sleep()
```

and countdown loops.

---

## Step 6 — Tkinter GUI

Created GUI windows using Tkinter.

Built:

* signal windows
* labels
* traffic signal graphics

---

## Step 7 — GUI Traffic Signal

Built graphical traffic signal simulator with:

* red signal
* green signal
* dynamic updates

---

## Step 8 — OpenCV Integration

Installed OpenCV and integrated video processing.

---

## Step 9 — Traffic Video Processing

Processed traffic video using:

```python
cv2.VideoCapture()
```

Read video frame-by-frame.

---

## Step 10 — Motion Detection

Implemented motion detection using:

```python
cv2.createBackgroundSubtractorMOG2()
```

Detected moving vehicles from traffic footage.

---

## Step 11 — Vehicle Counting

Counted vehicles using:

* contours
* contour area filtering
* bounding rectangles

Displayed vehicle count on video frames.

---

## Step 12 — Smart Adaptive Traffic Signal

Connected vehicle counting with adaptive signal timing logic.

Workflow:

Traffic Video
↓
Vehicle Detection
↓
Vehicle Counting
↓
Adaptive Signal Logic
↓
Dynamic Signal Timing

---

# How to Run the Project

## Step 1

Move into project folder:

```bash
cd traffic_project
```

---

## Step 2

Run the main project:

```bash
python3 smart_signal.py
```

---

# Output

The system:

* detects vehicles
* counts vehicles
* analyzes traffic density
* dynamically adjusts green signal timing

---

# Future Improvements

* YOLO AI-based vehicle detection
* Ambulance priority system
* Multi-lane traffic analysis
* Live CCTV integration
* Dashboard visualization

---

# Conclusion

This project demonstrates the use of Python, OpenCV, and computer vision techniques for intelligent traffic management. The system successfully analyzes traffic density and dynamically adjusts traffic signal timing based on real-time vehicle movement.
