import ctypes

class BoundingBox(ctypes.Structure):
    _fields_ = [("x1", ctypes.c_float),       # float
                ("y1", ctypes.c_float),       # float
                ("x2", ctypes.c_float),       # float
                ("y2", ctypes.c_float),       # float
                ("score", ctypes.c_float),    # float
                ("class_num", ctypes.c_int)]  # int32_t

class ObjectDetectionResult(ctypes.Structure):
    _fields_ = [("class_count", ctypes.c_uint), # uint32_t
                ("box_count", ctypes.c_uint),   # boxes of all classes
                ("boxes", BoundingBox * 0)]     # box array
