import pandas as pd
import re



def desired_line(x):
    f = open('C:/Users/Nekos/Desktop/Data Science/python_intro/beeline_consent_query_stderr.txt')
    row_count = 0
    for i in f:
        row_count = row_count + 1
        temp = i.split(" ")
        if (x == row_count):
            #print("Word is: ",temp[3])
            return list(temp)
    return 0


def read_headers(first, last):
    all_headers = []
    row_of_header = []
    for row in range(first, last):
        temp = desired_line(row)
        #print(temp)
        if (temp[3] != ""):
            row_of_header.append(row)
            if (len(temp) == 3):
                #print(temp[3])
                all_headers.append(temp[3])
            else:
                #print(''.join(temp[3:]))
                all_headers.append(''.join(temp[3:]))
    #print(row_of_header)
    return all_headers, row_of_header


all_headers, rows_of_headers = read_headers(102, 303)
#print(rows_of_headers)

def get_data(start, end):
    my_dict = {}
    for row in range(start+1, end):
        temp = desired_line(row)
        key = ''.join(filter(lambda x: x!=":", temp[-2]))
        numeric_value = ''.join(filter(str.isdigit, temp[-1]))
        #print("Title: ", key)
        #print("Value: ", numeric_value)       
        my_dict[key] = numeric_value

    return my_dict



def main():
    final_dict = {}
    for i in range(1, len(all_headers)):
        start = rows_of_headers[i-1]
        end = rows_of_headers[i]
        nested = get_data(start, end)
        #print("Key: ", all_headers[i-1])
        #print("Value: ", nested)
        final_dict[all_headers[i-1]] = nested
    
    print(final_dict)
    return final_dict
     

def save_dict(filepath, dict):
    temp_dict = dict
    temp_dict = str(temp_dict)
    with open(filepath, 'w') as dict_file:
        dict_file.write(temp_dict)
    print(temp_dict)


dict = main()

save_dict("C:/Users/Nekos/Desktop/Data Science/python_intro/out_3.txt", dict)




