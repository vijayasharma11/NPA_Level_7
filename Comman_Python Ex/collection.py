my_list =[1,2,3,3,4,5,6]
print(my_list)
new_list = list(set(my_list))
print(new_list)


delete_list = new_list.pop(1)
print(delete_list)
print(new_list)

my_set = {1,2,3,3,4,5,5}
print(my_set)

dict1 = {'a':1,'b':2}
dict2 ={'c':3,'d':4}

dict1.update(dict2)
print(dict1)

merged_dict = {**dict1, **dict2}
print(merged_dict)  

for key in dict1:
    print(key)

for key,value in dict1.items():
    print(f"{key}:{value}")

#my_dict1 = defaultdict(int)
#my_dict1 = ['a'] == 1

my_list.remove(6)
print(my_list)

set1 = {1,2,3,4,5,8}
set2 = {5,4,6,3,7,2}

union_resutl = set1 |set2
print(union_resutl)

intersction_result = set1 & set2
print(intersction_result)

difference_result = set1 - set2
print(difference_result)

subset_result = set1 <= set2
print(subset_result)
