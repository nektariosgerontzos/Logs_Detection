import pandas as pd
import re


def desired_line(x):
    f = open('C:/Users/Nekos/Desktop/Data Science/python_intro/beeline_consent_query_stderr.txt')
    row_count = 0
    for i in f:
        row_count = row_count + 1
        temp = i.split(" ")
        if (x == row_count):
            return list(temp)
    return 0


def first_row():
    f = open('C:/Users/Nekos/Desktop/Data Science/python_intro/beeline_consent_query_stderr.txt')
    row_count = 0
    for i in f:
        row_count = row_count+1
        temp = i.split(" ")
        if( ("Task" in temp) &  ("Execution" in temp) & ("Summary\n" in temp)):
            #print(row_count, " ", temp)
            return row_count
        
def find_last_line():
    row = first_row() +4

    line = row +1
    while (True):
        tmp = desired_line(line)
        if ('-' in str(tmp)):
            print(line)
            return line
        else:
            line = line +1


def get_nested_keys():
    header = first_row() + 2
    tmp = desired_line(header)
    cleaned = []
    for item in tmp:
        if( (item != "") & (item!="INFO") & (item!=":") ):
            cleaned.append(item)
    
    #print(cleaned)
    return(cleaned)

def get_outter_keys(first_row, last_row):
    outter = []
    for row in range(first_row, last_row):
        temp = desired_line(row)
        filtered_data = list(filter(lambda x: x != "", temp))
        #print(row ," ", filtered_data)
        outter.append(filtered_data[2] + " " + filtered_data[3])
    print(outter)
    return outter

def get_data(first_row, last_row):
    dictionary_temp = {}
    outter = get_outter_keys(first_row, last_row)
    f = open('C:/Users/Nekos/Desktop/Data Science/python_intro/beeline_consent_query_stderr.txt')
    #num_pattern = r'[0123456789.]+' can't fix it now
    keys = get_nested_keys()
    for row in range(first_row, last_row):
        my_dict = {}
        temp = desired_line(row)
        numeric_values = str(temp)
        cleaned = []
        for item in temp:
            #print(item)
            if( (item != "") & (item!="INFO") & (item!=":") & (item!="Map") & (item!="Reducer")):
                cleaned.append(item)
            
        #print("Cleaned is: ", cleaned, "and length is: ", len(cleaned))
        for i in range(1, len(keys)):
            #print(keys[i], " AND ", cleaned[i])
            my_dict[keys[i]] = cleaned[i]
        #print(row)
        #print(my_dict)
        dictionary_temp[outter[row-first_row]] = my_dict
    print(dictionary_temp)
    return dictionary_temp

def save_dict(filepath, dict):
    temp_dict = dict
    temp_dict = str(temp_dict)
    with open(filepath, 'w') as dict_file:
        dict_file.write(temp_dict)
    print(temp_dict)



start = first_row() +4
end = find_last_line()
final = get_data(start, end)
save_dict("C:/Users/Nekos/Desktop/Data Science/python_intro/out_2.txt", final)





























