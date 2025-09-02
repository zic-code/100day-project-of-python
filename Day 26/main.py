# #list Comprehension
# #new_list = [new_item for item in list]
# numbers = [1,2,3] #list
# # if you want to add 1 for each number usually you have to do like this.
# new_list = []
# for n in numbers:
#     new_n= n + 1
#     new_list.append(n+1)
# print(new_list)
# # but you can do much shortly with list comprehension.
# new_list2 = [n+1 for n in numbers]
# print(new_list2)

# dictionary_comprehension
# new_dict = {new_key: new value for (key,value) in dict.items() if test}
# looping through dictionaries:
# for (key, values) in dict.items():
#     print(key)
#     print(values)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56,76,98 ]
}
#
# for (key, value) in student_dict.items():
#     print(key,value)

import pandas

student_data_frame =pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through  a data frame
for (index,row) in student_data_frame.iterrows():
    if row.student == 'Angela':
        print(row.score)