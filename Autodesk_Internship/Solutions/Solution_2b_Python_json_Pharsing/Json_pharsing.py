# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 21:44:17 2023

@author: Kavin
"""
import json 

with open("p_ex_1_runtime_parsing.json") as j:
    data = json.load(j)

software_runtime = {}
operation_runtime = {}

#readin the individual options 

for i in range(len(data)):
    try:
        
        software=data[i]['software']
        operation = data[i]['operation']
        runtime=data[i]['length']
        
        if software in software_runtime:
            software_runtime[software]=+runtime
        else:
            software_runtime[software]=runtime
            
        if operation in operation_runtime:
            operation_runtime[operation]=+runtime
        else:
            operation_runtime[operation]=runtime
        
    except TypeError:
        print("Improper data type for length in object number -- ",i+1," --  Phrased value -->  ", runtime)
    
    except KeyError:
        print("Misssing key in object number -- ",i+1)
        
longest_operation = max(software_runtime, key=software_runtime.get)
sorted_software = sorted(software_runtime, key=software_runtime.get, reverse=True)   

print()  
print("-------------------------------------------- RESULTS -------------------------------------------------")
print()
print()
print("The program with the longest runtime is  ---  ",longest_operation,"   ---")
print()
print("List of the softwares sorted in descending order by sum of runtimes   ---   ",sorted_software,"   ---")
        
        
            
            
        
    
    
    
    
    