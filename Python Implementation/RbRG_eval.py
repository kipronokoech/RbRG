#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from shapely.geometry import Polygon,Point
import matplotlib.pyplot as plt
import shapely
import cv2 as cv
import os
import gc


def evaluation2(ground,refined,iou_value):
  """
  ground-array for ground-truth anotations;
  refined- Image. Output of RbRG;
  iou_value - IoU threshold value
  """
  try:
    img=cv.imread(refined)
    img=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    #MORPHOLOGICAL OPENING TO FILL HOLES
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(10,10))
    img = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)

    # FINDING CONTOURS using findContours on OpenCV.
    thresh, im_bw = cv.threshold(np.uint8(img), 127, 255, cv.THRESH_BINARY) #im_bw: binary image
    _,contours, hierarchy = cv.findContours(im_bw,cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    def set_contours(contour):
      """
      This functions performs squeezing of contour array, that is, 
      applying set_contours on an array entry of the form (r,1,c) yields (y,c)
      """
      contours_res=[]
      for i in range(len(contour)):
        contours_res.append(np.squeeze(contour[i],1))
      return np.array(contours_res)


    pts=set_contours(contours)
    pp=[]
    #This for-loop is used to reverse the co-ordinates in element-wise manner, that is,
    #the contour co-ordinates are read as (y,x) and therefore we apply the loop to make is (x,y)
    for i in range(len(pts)):
        p=np.int32(pts[i])
        p=p.tolist()
        for j in range(len(p)):
            p[j].reverse()
        p=np.array(p)
        pp.append(p)
    preds=np.array(pp)

    # pred="/content/gdrive/My Drive/Research Project/Results/11444-28-95/11444-28-95_contours.npy"
    truth=np.squeeze(np.load(ground, allow_pickle=True))

    # preds=set_contours(preds)
    prob=[]
    #this for-loop calculates the actual IoU for every fruit intance,
    #first with predictions  as the inference ,
    #second, ground-truths as the inference
    for i in range(len(preds)):
        f1=preds[i]
        f1=shapely.geometry.Polygon(f1)
        f1_radius=np.sqrt((f1.area)/np.pi)
        f1_buffered=shapely.geometry.Point(f1.centroid).buffer(f1_radius*500)
        cont=[]
        #print("#########################################################")
        for i in range(len(truth)):
          ff=shapely.geometry.Polygon(np.squeeze(truth[i]))
          if f1_buffered.contains(ff)== True:
            iou=(ff.intersection(f1).area)/(ff.union(f1).area)

            #print(iou)
            #print("##############################")
            cont.append((iou))
            #print(f1_buffered.centroid)
        prob.append(cont)
    tp1=0
    fp=0
    fp1=0
    tp=0
    #fn1=0
    for t in prob:
      if sum(i > .0 for i in t)>1 and np.sum(t)>=iou_value:
        tp=tp+sum(i > .0 for i in t)
      elif sum(i >= iou_value for i in t)>=1:
        tp1=tp1+1
      elif sum(i > .0 for i in t)>=1 and np.sum(t)<iou_value :
        fp1=fp1+1
      elif np.max(t)==0:
        fp=fp+1
      # elif sum(i > .0 for i in t)>=1 and np.sum(t)<iou_value:
      #   fn1=fn1+1

    prob1=[]
    for i in range(len(truth)):
        f1=truth[i]
        f1=shapely.geometry.Polygon(f1)
        f1_radius=np.sqrt((f1.area)/np.pi)
        f1_buffered=shapely.geometry.Point(f1.centroid).buffer(f1_radius*500)
        cont1=[]
        #print("#########################################################")
        for i in range(len(preds)):
          ff=shapely.geometry.Polygon(np.squeeze(preds[i]))
          if f1_buffered.contains(ff)== True:
            iou=(ff.intersection(f1).area)/(ff.union(f1).area)
            #print(iou)
            #print("##############################")
            cont1.append((iou))
            #print(f1_buffered.centroid)
        prob1.append(cont1)
    def CheckLess(list1,val):
      return(all(x< val for x in list1))
    fn2=0
    for t in prob1:
    #print(t)
      if np.sum(t)==0:#CheckLess(t,iou_value)==True and np.sum(t)<iou_value:
        fn2=fn2+1
    tp=tp+tp1
    fp=fp+fp1
    fn=fn2
    #fn=fn+fn2
    print("---------------------------------------------------------------------------------")
    print("\t |TP:",tp,"\t |FP:",fp,"\t |Missed:",fn,"\t GT",truth.shape[0])
    precision=round(tp/(tp+fp),3) 
    recall=round(tp/(truth.shape[0]),3)
    f1= round(2*((precision*recall)/(precision+recall)),3)
    print("Precision:",precision,"\t Recall:",recall, "\t F1",f1)#,"\tGT:",truth.shape[0],"\t PD:",preds.shape)
  except:
    pass


# In[ ]:




