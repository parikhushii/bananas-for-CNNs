from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import matplotlib.pyplot as plt
img = keras.preprocessing.image.load_img("C:\Users\khush\OneDrive\Documents\ScienceFair2022\LeafDatabase\Validation\Fusarium\fusarium101.jpg", target_size= (244,244))
img_tensor = keras.preprocessing.image.img_to_array(img)
img_tensor = np.expand_dims(img_tensor, axis=0)
#Uses ImageDataGenerator to flip the images
datagen = ImageDataGenerator(width_shift_range=[-100, 100],          
                    height_shift_range=[-100, 100], 
                    rotation_range=120, brightness_range=[0.2, 1.5],
                    zoom_range = [0.3, 1.5] ,shear_range=50)
#Creates our batch of one image
pic = datagen.flow(img_tensor, batch_size =1)
plt.figure(figsize=(16, 16))
#Plots our figures
for i in range(1,17):
   plt.subplot(4, 4, i)
   batch = pic.next()
   image_ = batch[0].astype(‘uint8’)
   plt.imshow(image_)
plt.show()
