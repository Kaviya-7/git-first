'''num=int(input())
rev_num=0
string=str(num)
rev_num=string[::-1]
print(rev_num)'''


'''lst=[1,5,2,7,3,7,3,8,5,9,2,10]
lst1=[]
for i in lst:
    if i not in lst1:
        lst1.append(i)
print(lst)
print(lst1)'''


'''#with funtion call
def remove_duplicates(input_list):
    unique_list=[]
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
def mn():
    my_list=[1,2,3,3,2,7,4,8,9,7,]
    result=remove_duplicates(my_list)
    print(result)
mn()'''


'''#without function call
def remove_duplicates(input_list):
    unique_list=[]
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list:
my_list=[1,2,3,3,2,7,4,8,9,7,]
result=remove_duplicates(my_list)
print(result)'''
