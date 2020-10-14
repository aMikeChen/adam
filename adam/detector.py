from adam.dme import DME
from adam.detection_result import DetectionResult
from adam import constants

FWINFO_PATH = "./models/fw_info.bin"
MODEL_PATH = "./models/all_models.bin"

class Detector:
    def __init__(self, camera):
        self.camera = camera
        self.dme = DME(FWINFO_PATH)
        self.dme.load_model(MODEL_PATH)

        image_format = (constants.IMAGE_FORMAT_SUB128 |
                        constants.NPU_FORMAT_RGB565)
        self.dme.configure(model_id=3,
                           output_num=8,
                           image_format=image_format)

    def detect(self):
        frame, img_buf = self.camera.capture_frame()
        _ret, inf_size, _res_flag = self.dme.inference(img_buf=img_buf,
                                                       buf_len=self.camera.image_size)

        return self.__get_detection_result(inf_size, frame)

    def __get_detection_result(self, inf_size, frame):
        inf_res = self.dme.get_result(inf_size)
        return DetectionResult(inf_res)
