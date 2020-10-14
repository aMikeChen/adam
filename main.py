from adam.detector import Detector
from adam.camera import Camera

if __name__ == "__main__":
    camera = Camera(0, 640, 480)
    detector = Detector(camera)

    print("\nStart detecting:\n")

    while True:
        result = detector.detect()
        print("class_count: {}, box_count: {}".format(result.class_count, len(result.boxes)))
        for box in result.boxes:
            print(box)
