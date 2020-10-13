import ctypes

# Image format flags
IMAGE_FORMAT_SUB128 = 1 << 31
IMAGE_FORMAT_RAW_OUTPUT = 1 << 28
IMAGE_FORMAT_PARALLEL_PROC = 1 << 27
IMAGE_FORMAT_MODEL_AGE_GENDER = 1 << 24
# right shift for 1-bit if 1
IMAGE_FORMAT_RIGHT_SHIFT_ONE_BIT = 1 << 22
IMAGE_FORMAT_SYMMETRIC_PADDING = 1 << 21
IMAGE_FORMAT_CHANGE_ASPECT_RATIO = 1 << 20
IMAGE_FORMAT_BYPASS_PRE = 1 << 19
IMAGE_FORMAT_BYPASS_NPU_OP = 1 << 18
IMAGE_FORMAT_BYPASS_CPU_OP = 1 << 17
IMAGE_FORMAT_BYPASS_POST = 1 << 16

NPU_FORMAT_RGBA8888 = 0x00
NPU_FORMAT_NIR = 0x20
# Support YCBCR (YUV)
NPU_FORMAT_YCBCR422 = 0x30
NPU_FORMAT_YCBCR444 = 0x50
NPU_FORMAT_RGB565 = 0x60

# Structures used for the C shared library.
class KDPDMEConfig(ctypes.Structure):
    """Image configuration structure"""
    _fields_ = [("model_id", ctypes.c_int),       # int32_t
                ("output_num", ctypes.c_int),     # int32_t
                ("image_col", ctypes.c_int),      # int32_t
                ("image_row", ctypes.c_int),      # int32_t
                ("image_ch", ctypes.c_int),       # int32_t
                ("image_format", ctypes.c_uint)]  # uint32_t

    def __init__(self, model_id, output_num, col, row, ch, image_format):
        self.model_id = model_id
        self.output_num = output_num
        self.image_col = col
        self.image_row = row
        self.image_ch = ch
        self.image_format = image_format

    def __repr__(self):
        return "id: {}, output_num: {}, dims: ({}, {}, {}), format: {}".format(
            self.model_id, self.output_num, self.ch, self.col, self.row, self.image_format)
