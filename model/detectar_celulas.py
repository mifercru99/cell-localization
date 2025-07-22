#================================================================
#
#   File name   : detectar_celulas.py
#   Author      : Miguel Fernandez Cruchaga
#   Created date: 05-01-2022
#   GitHub      : https://github.com/pythonlessons/TensorFlow-2.x-YOLOv3
#   Description : deteccion de celulas en imagenes y videos
#
#================================================================

import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
import cv2
import numpy as np
import tensorflow as tf
from yolov3.utils import detect_image, detect_realtime, detect_video, Load_Yolo_model, detect_video_realtime_mp
from yolov3.configs import *

video_path  = "./testset/VideosTestSet/SCC42B-2.avi"

yolo = Load_Yolo_model()

for x in range(31):
    y = x + 50
    detect_image(yolo, './testset/ImagesTestSet/frame{}.jpg'.format(y), "./testset/deteccion/imagenes/image{}.jpg".format(y), input_size=416, show=False, CLASSES=TRAIN_CLASSES, rectangle_colors=(255,0,0))

detect_video(yolo, video_path, './testset/deteccion/videos/SCC42B-2.avi', input_size=YOLO_INPUT_SIZE, show=False, CLASSES=TRAIN_CLASSES, rectangle_colors=(255,0,0))
