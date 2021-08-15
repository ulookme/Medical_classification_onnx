import json

from commons import get_model, transform_image
from PIL import Image
import torch
import onnx
import os
import onnxruntime


model_path = os.path.join('models', 'MedNetV3.onnx')
ort_session = onnxruntime.InferenceSession(model_path)
imagenet_class_index = json.load(open('imagenet_class_index.json'))


def to_numpy(tensor):
    return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()

def get_prediction(image_bytes):
    try:
        img_y, img = transform_image(image_bytes)
        ort_inputs = {ort_session.get_inputs()[0].name: to_numpy(img_y)}
        ort_outs = ort_session.run(None, ort_inputs)
        outputs = ort_outs[0]
    except Exception:
        return 404, 'error'
    
    return imagenet_class_index.get(str(outputs.argmax())), outputs.argmax(), img