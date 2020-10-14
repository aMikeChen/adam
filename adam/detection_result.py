from adam.structs import BoundingBox, ObjectDetectionResult
import ctypes

def parse_box(box):
    x1 = int(box.x1)
    y1 = int(box.y1)
    x2 = int(box.x2)
    y2 = int(box.y2)
    score = float(box.score)
    class_num = int(box.class_num)

    return [x1, y1, x2, y2, class_num, score]

class DetectionResult:
    def __init__(self, inf_res):
        object_detection_result = ctypes.cast(ctypes.byref(inf_res),
                                              ctypes.POINTER(ObjectDetectionResult)).contents
        self.class_count = object_detection_result.class_count

        boxes = ctypes.cast(ctypes.byref(object_detection_result.boxes),
                            ctypes.POINTER(BoundingBox * object_detection_result.box_count)).contents

        box_list = []
        for box in boxes:
            box_list.append(parse_box(box))

        self.boxes = box_list
