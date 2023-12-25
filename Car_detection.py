import cv2

def initialize_video_capture(video_path):
    """
    Initializes video capture from the given video path.

    Args:
    video_path (str): Path to the video file.

    Returns:
    cv2.VideoCapture: Video capture object.
    """
    return cv2.VideoCapture(video_path)

def load_car_cascade(cascade_path):
    """
    Loads the car cascade classifier from the given XML file.

    Args:
    cascade_path (str): Path to the car cascade XML configuration file.

    Returns:
    cv2.CascadeClassifier: Car cascade classifier object.
    """
    return cv2.CascadeClassifier(cascade_path)

def detect_cars(frame, car_cascade):
    """
    Detects cars in the given frame using the specified car cascade.

    Args:
    frame (np.array): The frame in which cars are to be detected.
    car_cascade (cv2.CascadeClassifier): Car cascade classifier object.

    Returns:
    list of tuples: List of detected cars represented as (x, y, width, height).
    """
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray_frame, 1.1, 9)
    return cars

def draw_car_boxes(frame, cars):
    """
    Draws bounding boxes and labels around detected cars.

    Args:
    frame (np.array): The frame on which to draw.
    cars (list of tuples): List of detected cars represented as (x, y, width, height).
    """
    for x, y, w, h in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (51, 51, 255), 2)
        cv2.rectangle(frame, (x, y - 40), (x + w, y), (51, 51, 255), -2)
        cv2.putText(frame, "Car", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

def main():
    video_path = "path-to-video"
    cascade_path = "path-to-the-xml-configuration-file"

    video_capture = initialize_video_capture(video_path)
    car_cascade = load_car_cascade(cascade_path)

    cv2.namedWindow("Car Detection System", cv2.WINDOW_NORMAL)

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        cars = detect_cars(frame, car_cascade)
        draw_car_boxes(frame, cars)

        resized_frame = cv2.resize(frame, (600, 400))
        cv2.imshow("Car Detection System", resized_frame)

        if cv2.waitKey(30) & 0xFF == 27:  # ESC key
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
