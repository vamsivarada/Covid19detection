# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 00:20:49 2020

@author: vamsi
"""

import tensorflow as tf 
import numpy as np
def test_covid(imagePath):
    # load json and create model
    loaded_model = tf.keras.models.load_model('model.model')
    print("Loaded model from disk")

    import cv2
    image = cv2.imread(imagePath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))
    predIdxs = loaded_model.predict(image.reshape(1,224,224,3), batch_size=5)
    print(predIdxs)
    predIdxs = np.argmax(predIdxs, axis=1)
    print(predIdxs)
    if predIdxs[0] ==0:
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Covid-detection-kit", "Covid Confirmed Recover Soon!!!")
        root.destroy()
    else:
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Covid-detection-kit", "You Are Safe from Covid")
        root.destroy()
if __name__ == '__main__':
    imagePath = r'C:/Users/vamsi/PycharmProjects/Detect-CoronaVirus-Tensorflow-master/dataset/covid/auntminnie-b-2020_01_28_23_51_6665_2020_01_28_Vietnam_coronavirus.jpeg'
    test_covid(imagePath)