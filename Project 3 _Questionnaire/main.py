# -*- coding: utf-8 -*-
"""
Created on Sun May  1 14:10:50 2022

@author: Valeriy
"""
import json
import numpy as np

class Ques:             # Object 
   global data_out
   data_out ={}
   def data_load(self):   #Load data from json
     global data_in
     with open("qs_input.json", "r") as read_file:
      data_in = json.load(read_file)
      return data_in
 
   def sett_load(self):   #Load questionnare logic from json
     global sett
     with open("qs_setting.json", "r") as read_file:
      sett = np.array(json.load(read_file))
      return sett

   def data_save(self,data_out):  #Save result in json
     with open("qs_output.json", "w") as write_file:
      json.dump(data_out,write_file)
   
 
   def acc(self,sett,data_in):      #Main questionnare block
    a=0
    while a in range(len(data_in)):
      x=input(data_in[a])           #Input from user
      y=list(data_in[a].values())   #Enumeration of questions
      data_out[int(a)]=x            #Saving result of answer
      if x == y[0][0]:
        a =sett[a,1]
      if x == y[0][1]:
        a =sett[a,2]
        if a == 8:
         print('Quit')
        else:
         pass
      else:
       print('Wrong input')
    return data_out
      
     
     
ques =Ques()
ques.data_load()
ques.sett_load()
data_out =ques.acc(sett,data_in)
ques.data_save(data_out)

