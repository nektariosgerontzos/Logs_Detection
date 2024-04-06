import pandas as pd
import re

def first_row():
    f = open('C:/Users/Nekos/Desktop/Data Science/python_intro/beeline_consent_query_stderr.txt')
    row_count = 0
    for i in f:
        row_count = row_count+1
        temp = i.split(" ")
        if( ("Query" in temp) and  ("Execution" in temp)):
            print(row_count, " ", temp)
            return row_count
        
# takes a number as parameter and fetches the corresponding line of the file
def desired_line(x):
    f = open('C:/Users/Nekos/Desktop/Data Science/python_intro/beeline_consent_query_stderr.txt')
    row_count = 0
    for i in f:
        row_count = row_count + 1
        temp = i.split(" ")
        if (x == row_count):
            return list(temp)
    return 0


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


def get_data(first_row, last_row):
    dictionary = {}
    f = open('C:/Users/Nekos/Desktop/Data Science/python_intro/beeline_consent_query_stderr.txt')
    num_pattern = r'\d+\.?\d*'
    for i in range(first_row, last_row):
        temp = desired_line(i)
        line = str(temp)
        numeric_values = re.findall(num_pattern, str(temp))
        temp_key = ' '.join(temp[3:5])
        if (temp_key!= ""):
            for i in numeric_values:
                if float(i)>0:
                    dictionary[temp_key] = i
                    
    return dictionary


def save_dict(filepath, dict):
    temp_dict = get_data(80, 90)
    temp_dict = str(temp_dict)
    with open(filepath, 'w') as dict_file:
        dict_file.write(temp_dict)
    print(temp_dict)





my_dict = get_data(80, 90)
save_dict('C:/Users/Nekos/Desktop/Data Science/python_intro/out.txt', my_dict)










