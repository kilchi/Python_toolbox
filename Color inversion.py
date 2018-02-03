

import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing import image

img_path = '/Users/Aki/Anaconda3/aki.jpg'
img = image.load_img(img_path, target_size=(474, 291))
img_tensor = image.img_to_array(img)
img_tensor /= 255.

#shape:(1,474,291,3)
print(img_tensor.shape)

plt.imshow(img_tensor)
plt.show()
