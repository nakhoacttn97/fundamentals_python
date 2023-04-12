'''
Created on Feb 13, 2017

@author: KTPHUONG
'''
import csv

def read_csv_file(filename):    
    f = open(filename)    
    for row in csv.reader(f):        
        print(row)    
    f.close()


def read_csv_file_to_list(filename):    
    f = open(filename)  
    data = []  
    for row in csv.reader(f):        
        data.append(row)    
    f.close()
    return data

def read_csv_file_column(filename):    
    f = open(filename)    
    for row in csv.reader(f):        
        print(row[0], '\t', row[1])    
    f.close()    

def write_csv_file(filename, listContent):  
    f = open(filename,'a', newline='')      
    for item in listContent:        
        csv.writer(f).writerow(item)
    f.close()
    