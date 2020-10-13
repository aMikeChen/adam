import cv2
import ctypes
import numpy as np

class Camera:
    def __init__(self, cam_id, width, height):
        self.capture = cv2.VideoCapture(cam_id)

        if not self.capture.isOpened():
            raise "Cannot open camera"

        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        self.frames = []
        self.image_size = width * height * 2

    def capture_frame(self):
        _cv_ret, frame = self.capture.read()

        if frame is None:
            raise "Failed to read from camera"

        frame = cv2.flip(frame, 1)

        frame_data = cv2.cvtColor(frame, cv2.COLOR_BGR2BGR565)
        frame_data = frame_data.reshape(self.image_size)
        c_char_p = ctypes.POINTER(ctypes.c_char)
        frame_data = frame_data.astype(np.uint8)
        data_p = frame_data.ctypes.data_as(c_char_p)

        return (frame, data_p)
