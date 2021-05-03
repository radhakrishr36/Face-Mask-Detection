from keras.applications.resnet50 import ResNet50, preprocess_input
from keras.preprocessing import image
from keras.layers import Dense, Reshape
from keras.models import Model
import keras
import numpy as np
from keras.applications import vgg16
from scipy import spatial


vgg = vgg16.VGG16(include_top=False, weights='imagenet', 
                                     input_shape=(150,150,3))

output = vgg.layers[-1].output
output = keras.layers.Flatten()(output)
vgg_model = Model(vgg.input, output)


def get_feature(img_val):
    try:
        img=np.array(img_val)
        img= np.expand_dims(img_val,axis=0)
        feature=vgg_model.predict(img)[0]
        return feature  
    
    except Exception as e:
        print(e)
        return [0,0,0]


def get_image(image_path):
    try:
        path= image_path
        img = image.load_img(path, target_size=(150,150))
        img = image.img_to_array(img)
        img = img/255
        #print(len(img))
        return img
    except Exception as e:
        print('Exception in get_image',e)
        return [0,0,0]


def find_similarity(input_image,manoj,abhishikth):

    feature_manoj=get_feature(get_image(manoj))
    feature_abhishikth=get_feature(get_image(abhishikth))

    feature_input=get_feature(get_image(input_image))


    result_m = 1 - spatial.distance.cosine(feature_input, feature_manoj)
    result_abhi= 1 - spatial.distance.cosine(feature_input, feature_abhishikth)


    if result_m>result_abhi:

        return 'Manoj'

    else:

        return 'abhishikth'

# input='C:/Users/Radha/Desktop/Notes/Jerome/Face-Mask-Detection-master/Face-Mask-Detection-master/sample_images/manoj.jpg'
# manoj="C:/Users/Radha/Desktop/Notes/Jerome/Face-Mask-Detection-master/Face-Mask-Detection-master/sample_images/manoj.jpg"
# abhishikth="C:/Users/Radha/Desktop/Notes/Jerome/Face-Mask-Detection-master/Face-Mask-Detection-master/sample_images/abij.jpg"

# print(find_similarity(input,manoj,abhishikth))




