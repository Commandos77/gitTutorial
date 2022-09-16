import json

class Calc:             # Object 
   global data_out
   data_out ={}
   def data_load(self):   #Load data from json
     global data_in
     with open("input_js.json", "r") as read_file:
      data_in = json.load(read_file)
      return data_in
 
   def rul_load(self):   #Load calculation coefficients from json
     global rules
     with open("calc_rules.json", "r") as read_file:
      rules = json.load(read_file)
      return rules

   def data_save(self,data_out):  #Save result in json
     with open("output_js.json", "w") as write_file:
      json.dump(data_out,write_file)
   
 
   def acc(self,rules,data_in):   #Main calculation block
    data_out ={}
    for a in data_in:
     y = a['convert_to']
     z = a['unit']
     
     for b in rules:
      c = b['unit_in']
      d = b['unit_out']
      if d == y and c == z:
           result =float(a['value'])*float(b['calc'])
           data_out[c]=result
           print(data_out)
      else:
         pass
    return data_out   
 
calc=Calc()
calc.data_load()
calc.rul_load()
r=calc.acc(rules,data_in)
calc.data_save(r)
