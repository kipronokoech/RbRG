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


def evaluation1(ground,pred,iou_value):
  """
  ground= array of ground-truth contours.
  preds = array of predicted contours.
  iou_value= iou treshold for TP and otherwise.
  """
  truth=np.squeeze(np.load(ground, allow_pickle=True))
  preds=np.squeeze(np.load(pred, allow_pickle=True))
  def CheckLess(list1,val):
    return(all(x<=val for x in list1))

  prob1=[]
  for i in range(len(preds)):
      f1=preds[i]
      f1=shapely.geometry.Polygon(f1)
      f1_radius=np.sqrt((f1.area)/np.pi)
      f1_buffered=shapely.geometry.Point(f1.centroid).buffer(f1_radius*500)
      cont=[]
      for i in range(len(truth)):
        ff=shapely.geometry.Polygon(np.squeeze(truth[i]))
        if f1_buffered.contains(ff)== True:
          iou=(ff.intersection(f1).area)/(ff.union(f1).area)   
       
          cont.append((iou))

      prob1.append(cont)

  fp=0

  for t in prob1:
    if CheckLess(t,iou_value)==True:
      fp=fp+1
    
  prob2=[]
  for i in range(len(truth)):
      f1=truth[i]
      f1=shapely.geometry.Polygon(f1)
      f1_radius=np.sqrt((f1.area)/np.pi)
      f1_buffered=shapely.geometry.Point(f1.centroid).buffer(f1_radius*500)
      cont=[]

      for i in range(len(preds)):
        ff=shapely.geometry.Polygon(np.squeeze(preds[i]))
        if f1_buffered.contains(ff)== True:
          iou=(ff.intersection(f1).area)/(ff.union(f1).area)
        
          cont.append((iou))
          
      prob2.append(cont)
  missed=0
  tp=0
  for t in prob2:
    if np.sum(t)==0:
      missed=missed+1
    elif CheckLess(t,iou_value)==False:
      tp=tp+1
  
  print("----------------------------------------------------------------")
  print("\t TP:",tp,"\t FP:",fp,"\t Missed:",missed,"\t GT:",truth.shape[0])
  precision=round(tp/(tp+fp),3) 
  recall=round(tp/(truth.shape[0]),3)
  f1= round(2*((precision*recall)/(precision+recall)),3)
  print("Precall:",precision,"\t Recall:",recall, "\t F1 score:",f1)
  


# In[ ]:




