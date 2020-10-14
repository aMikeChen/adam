from adam.detector import Detector
from adam.camera import Camera

if __name__ == "__main__":
    camera = Camera(0, 640, 480)
    detector = Detector(camera)

    while True:
        detector.detect()
