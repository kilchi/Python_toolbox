# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 18:26:50 2018

@author: yp6ir
"""

import os
import numpy as np
import matplotlib.pyplot as plt

from keras.applications import VGG16
from keras import backend as K
from keras.preprocessing import image

model = VGG16(weights='imagenet',
              include_top=False)

layer_name = 'block3_conv1'
filter_index = 0

layer_output = model.get_layer(layer_name).output
loss = K.mean(layer_output[:,:,:, filter_index])

img_path = '/Users/Aki/Anaconda3/aki.jpg'
img = image.load_img(img_path, target_size=(474, 291))
img_tensor = image.img_to_array(img)
img_tensor /= 255.

#shape:(1,150,150,3)
print(img_tensor.shape)

plt.imshow(img_tensor[0])
plt.show()

def deprocess_image(x):
    x -= x.mean()
    x /= (x.std() + 1e-5)
    x *= 0.1
    
    x *=0.1
    
    x += 0.5
    x = np.clip(x, 0, 1)
    
    x *= 255
    x = np.clip(x, 0, 255).astype('uint8')
    return x



def generate_pattern(layer_name, filter_index, size=150):
    layer_output = model.get_layer(layer_name).output
    loss = K.mean(layer_output[:,:,:,filter_index])
    
    grads = K.grdients(loss, model.input)[0]
    grads /= (K.sqrt(K.mean(K.square(grads))) + 1e-5)
    iterate = K.function([model.input], [loss, grads])
    input_img_data = np.random.random((1, size, size, 3)) * 20 + 128.
    
    step = 1.
    for i in range(40):
        loss_value, grads_value = iterate([input_img_data])
        input_img_data += grads_value * step
    
    img = input_img_data[0]
    return deprocess_image(img)    
    
plt.imshow(generate_pattern('block3_conv1', 0))    
