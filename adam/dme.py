import kdp_host_api as api
import ctypes

KDP_USB_DEV = 1

DME_FWINFO_PATH = "./models/fw_info.bin"
DME_FWINFO_SIZE = 512
DME_MODEL_SIZE = 20 * 1024 * 1024

class DME:
    def __init__(self):
        self.__init_kdp_lib()
        self.__add_device()
        self.__start_kdp_lib()

    def __del__(self):
        api.kdp_lib_de_init()
        print("Deinitialized.")

    def load_model(self, model_path):
        self.__load_fireware_setup_data_to_device()
        self.__load_model_to_device(model_path)

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

    def __load_fireware_setup_data_to_device(self):
        print("Loading models to Kneron Device...")

        data = (ctypes.c_char * DME_FWINFO_SIZE)()
        n_len = api.read_file_to_buf(data, DME_FWINFO_PATH, DME_FWINFO_SIZE)

        if n_len <= 0:
            raise "Failed to read fw setup file"

    def __load_model_to_device(self, model_path):
        p_buf = (ctypes.c_char * DME_MODEL_SIZE)()
        n_len = api.read_file_to_buf(p_buf, model_path, DME_MODEL_SIZE)

        if n_len <= 0:
            raise "Failed to read model file"
