# from ultralytics import YOLO
#
# model = YOLO("./yolo_model/yolov8n.pt")
#
# model.export(format="onnx")


# from ultralytics import YOLO
#
# model = YOLO('./yolo_model/yolov8n.onnx')
# # results = model.track(source="../cat.mp4", conf=0.3, iou=0.5, show=True, classes=[15])
# results = model.track(source="../cat.mp4", tracker='bytetrack.yaml', show=True, classes=[15])