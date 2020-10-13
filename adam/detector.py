from adam.dme import DME
import ctypes

class Detector:
    def __init__(self, camera):
        self.camera = camera
        self.dme = DME("./models/fw_info.bin")
        self.dme.load_model("./models/all_models.bin")
        self.dme.configure()

    def detect(self):
        frame, img_buf = self.camera.capture_frame()
        inf_res = (ctypes.c_char * 256000)()

        det_res = self.dme.inference(img_buf=img_buf,
                                     buf_len=self.camera.image_size,
                                     inf_res=inf_res)
        print(det_res)
