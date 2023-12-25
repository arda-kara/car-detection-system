
---

# Car Detection System

## Introduction
This project is a simple car detection system implemented in Python using OpenCV. It utilizes Haar cascades to detect cars in video frames. The system reads a video file, processes each frame to detect cars, and displays the video with bounding boxes around the detected cars.

## Installation

### Prerequisites
- Python 3.x
- OpenCV library
- NumPy (usually installed with OpenCV)

### Installing OpenCV
You can install OpenCV using pip:
```bash
pip install opencv-python
```

## Usage

### Setting Up
1. Clone this repository to your local machine.
2. Download a Haar cascade XML file for car detection. (An XML file for a trained classifier is included in the repo for usage)
3. Have a video file ready to test the car detection.

### Running the Program
1. Open the script and set `video_path` to the path of your video file.
2. Set `cascade_path` to the path of your downloaded Haar cascade XML file.
3. Run the script:
```bash
python car_detection.py
```

### Exiting the Program
Press the 'ESC' key to exit the program while the video window is active.

## Customization
You can modify the parameters in the `detectMultiScale` method to tweak the detection sensitivity.

## Contributing
Contributions to improve this project are welcome. Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---
