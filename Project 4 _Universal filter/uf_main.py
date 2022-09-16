# -*- coding: utf-8 -*-
"""
Created on Sun May  1 14:10:50 2022

@author: Valeriy
"""

import json

class Ufit:             # Object 
   global data_out
   data_out ={}
   def data_load(self):   #Load data from json
     global data_in
     with open("uf_data.json", "r") as read_file:
      data_in = json.load(read_file)
      return data_in
   def include(self,data_in,rule):    #filter and sort base including data by rule
     user_data=data_in['data']
     key_col ="".join(rule[0][0].keys())
     key_val =rule[0][0].get(key_col)
     sort_rule =rule[1][0]
     include_result=sorted(list(filter(lambda x:x[key_col]==key_val,user_data)), key=lambda d: d[sort_rule])
     return include_result
     
   def exclude(self,data_in,rule):    #filter and sort base including data by rule
     user_data=data_in['data']
     key_col ="".join(rule[0][0].keys())
     key_val =rule[0][0].get(key_col)
     sort_rule =rule[1][0]
     exclude_result=sorted(list(filter(lambda x:x[key_col]!=key_val,user_data)), key=lambda d: d[sort_rule])
     return exclude_result
     
     
   def data_save(self,data_out):  #Save result in json
     with open("uf_output.json", "w") as write_file:
      json.dump(data_out,write_file)
    
   def main_block(self,data_in):
     
     for x in range(len(data_in['condition'])):
      
       rule=list(data_in['condition'][x].values())#Extract rules of filtering
       
       filtr_type =list(data_in['condition'][x].keys())[0]      #Extract all type of filter
       
       if filtr_type=='exclude':                                  #Tree of operations
          out = ufit.exclude(data_in,rule)
          data_out[filtr_type]=out
       if filtr_type =='include':
          out = ufit.include(data_in,rule)
          data_out[filtr_type]=out
       else:
         pass
       
     return data_out
     

     
ufit =Ufit()
ufit.data_load()
data_out=ufit.main_block(data_in)
ufit.data_save(data_out)



