import numpy as np
import cv2
import sys
import pandas as pd
import pickle
import math as m
import tkinter
import csv, glob
import yaml
import os, sys
from tkinter.filedialog import askopenfilename

annotation_type = input("[NOTE.....] If you are trying to store positive examples, enter yes; else type no: ")
ix,iy = -1,-1
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy
    if event == cv2.EVENT_LBUTTONDBLCLK:
        ix,iy = x,y

# Read the yml configuration file to iddentify the root directory
with open("config.yml", "r") as stream:
    config_data= yaml.safe_load(stream)
path = config_data["root_dir"]
grab_size = int(config_data["annotation_size"])
root = tkinter.Tk()
movieName =  askopenfilename(filetypes=[("Video files","*")])
cap = cv2.VideoCapture(movieName)
nframe =cap.get(cv2.CAP_PROP_FRAME_COUNT)
i=0
steps= nframe/20
if annotation_type == "yes":
    while(cap.isOpened() & (i<(nframe-steps))):
      i = i + steps
      print("[UPDATING.....]{}th/{} frame detected and stored".format(i, nframe))
      cap.set(cv2.CAP_PROP_POS_FRAMES,i)
      ret, img = cap.read()
      cv2.namedWindow('image')
      cv2.setMouseCallback('image',draw_circle)
      counter = 0
      while(1):
          counter+=1
          cv2.imshow('image',img)
          k = cv2.waitKey(20) & 0xFF
          if k == 27:
              break
          elif k == ord('a'):
              crop_img = img[iy-grab_size:iy+(grab_size),ix-grab_size:ix+(grab_size)]
              cv2.imwrite(path + "yes/yes{}.jpg".format(counter), crop_img)
      cv2.destroyAllWindows()
elif annotation_type == "no":
    while(cap.isOpened() & (i<(nframe-steps))):
      i = i + steps
      print("[UPDATING.....]{}th/{} frame detected and stored".format(i, nframe))
      cap.set(cv2.CAP_PROP_POS_FRAMES,i)
      ret, img = cap.read()
      cv2.namedWindow('image')
      cv2.setMouseCallback('image',draw_circle)
      counter = 0
      while(1):
          counter+=1
          cv2.imshow('image',img)
          k = cv2.waitKey(20) & 0xFF
          if k == 27:
              break
          elif k == ord('a'):
              crop_img = img[iy-grab_size:iy+(grab_size),ix-grab_size:ix+(grab_size)]
              cv2.imwrite(path + "no/no{}.jpg".format(counter), crop_img)
      cv2.destroyAllWindows()
