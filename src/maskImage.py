#!/usr/bin/env python
# coding: utf-8

import os
import sys
import skimage.io
import newVisualize
import time


startTime = time.time()
# Import Mask RCNN
sys.path.append("D:/Mask_RCNN-master")  # To find local version of the library
from mrcnn import utils
import mrcnn.model as modellib

# Import COCO config
sys.path.append("D:/Mask_RCNN-master/samples/coco")  # To find local version
import coco

# Directory to save logs and trained model
moodelDir = 'modelData'
modelPath = 'C:/Users/rivas/OneDrive/School/5 - Fall 2019/CS 4361/Final Project/mask_rcnn_coco.h5'

class InferenceConfig(coco.CocoConfig):
    # Set batch size to 1 since we'll be running inference on
    # one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

config = InferenceConfig()
config.display()

# Create model object in inference mode.
model = modellib.MaskRCNN(mode="inference", model_dir=moodelDir, config=config)

# Load weights trained on MS-COCO
model.load_weights(modelPath, by_name=True)

# COCO Class names
# Index of the class in the list is its ID
class_names = ['', 'person', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
               '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
               '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
               '', '', '', '', '', '']

# Load a random image from the images folder
srcName = 'Vic-4'

destName = 'testOutput/' + srcName + '_segmented.jpg'
image = skimage.io.imread('testInput/' + srcName +  '.jpg')


print('Running detection...')
# Run detection
results = model.detect([image], verbose=1)

print('Saving Image...')
# Visualize results
r = results[0]
newVisualize.save_image(image, r['rois'], r['masks'], r['class_ids'],
                            class_names, r['scores'], dest=destName)
endTime = time.time() - startTime

print('Image Saved.')

print('elapsed time:', endTime)