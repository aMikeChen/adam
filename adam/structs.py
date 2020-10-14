import ctypes

class BoundingBox(ctypes.Structure):
    _fields_ = [("x1", ctypes.c_float),
                ("y1", ctypes.c_float),
                ("x2", ctypes.c_float),
                ("y2", ctypes.c_float),
                ("score", ctypes.c_float),
                ("class_num", ctypes.c_int)]

class ObjectDetectionResult(ctypes.Structure):
    _fields_ = [("class_count", ctypes.c_uint),
                ("box_count", ctypes.c_uint),
                ("boxes", BoundingBox * 0)]

    def new(inf_res):
        result = ctypes.cast(ctypes.byref(inf_res),
                             ctypes.POINTER(ObjectDetectionResult)).contents
        boxes = ctypes.cast(ctypes.byref(result.boxes),
                            ctypes.POINTER(BoundingBox * result.box_count)).contents

        return result
