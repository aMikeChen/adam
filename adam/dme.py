import kdp_host_api as api
import ctypes
from time import sleep
from adam import constants

KDP_USB_DEV = 1

DME_FWINFO_SIZE = 512
DME_MODEL_SIZE = 20 * 1024 * 1024

class DME:
    def __init__(self, fwinfo_path):
        self.__init_kdp_lib()
        self.__add_device()
        self.__start_kdp_lib()
        self.__load_firmware_setup_data_to_device(fwinfo_path)

    def __del__(self):
        api.kdp_lib_de_init()
        print("Deinitialized.")

    def load_model(self, model_path):
        self.__load_model_to_device(model_path)
        self.__start_dme_mode()
        print("Loaded model.")
        sleep(0.001)

    def configure(self,
                  model_id=1000,
                  output_num=1,
                  image_col=640,
                  image_row=480,
                  image_ch=3):
        print("Starting DME configure...")

        image_format = (constants.IMAGE_FORMAT_SUB128 |
                        constants.NPU_FORMAT_RGB565 |
                        constants.IMAGE_FORMAT_RAW_OUTPUT |
                        constants.IMAGE_FORMAT_CHANGE_ASPECT_RATIO)
        config = constants.KDPDMEConfig(model_id,
                                        output_num,
                                        image_col,
                                        image_row,
                                        image_ch,
                                        image_format)
        data = ctypes.cast(ctypes.byref(config), ctypes.c_char_p)
        data_size = ctypes.sizeof(config)
        ret, model_id = api.kdp_dme_configure(self.dev_idx,
                                              data,
                                              data_size,
                                              model_id)

        if ret:
            raise "Cannot set to DME congiure mode"

        print("Configured DME model [{}].".format(model_id))
        sleep(0.001)

    def __init_kdp_lib(self):
        api.kdp_init_log("/tmp/", "adam.log")

        if api.kdp_lib_init() < 0:
            raise "Failed to init for kdp host lib"

    def __add_device(self):
        print("Adding device...")

        self.dev_idx = api.kdp_add_dev(KDP_USB_DEV, "")

        if self.dev_idx < 0:
            raise "Failed to add device"

    def __start_kdp_lib(self):
        print("Start kdp host lib...")

        if api.kdp_lib_start() < 0:
            raise "Failed to start kdp host lib"

    def __load_firmware_setup_data_to_device(self, fwinfo_path):
        print("Loading models to Kneron Device...")

        self.data = (ctypes.c_char * DME_FWINFO_SIZE)()
        self.data_size = api.read_file_to_buf(self.data, fwinfo_path, DME_FWINFO_SIZE)

        if self.data_size <= 0:
            raise "Failed to read fw setup file"

    def __load_model_to_device(self, model_path):
        self.img_buf = (ctypes.c_char * DME_MODEL_SIZE)()
        self.model_size = api.read_file_to_buf(self.img_buf, model_path, DME_MODEL_SIZE)

        if self.model_size <= 0:
            raise "Failed to read model file"

    def __start_dme_mode(self):
        print("Starting DME mode...")

        ret, ret_size = api.kdp_start_dme(self.dev_idx,
                                          self.model_size,
                                          self.data,
                                          self.data_size,
                                          0,
                                          self.img_buf,
                                          self.model_size)

        if ret:
            raise "Could not set to DME mode: {}".format(ret_size)
