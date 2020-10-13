from adam.dme import DME
from adam.camera import Camera
import cv2

if __name__ == "__main__":
    dme = DME("./models/fw_info.bin")
    dme.load_model("./models/all_models.bin")
    dme.configure()

    camera = Camera(0, 640, 480)

    # while True:
    #     frame, _data = camera.capture_frame()
    #     cv2.imshow('detection', frame)

    #     key = cv2.waitKey(1)
    #     if key == ord('q'):
    #         dme.exit()
    #         sys.exit()
