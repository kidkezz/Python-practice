#writing efficient code with python
#When we want to make an efficient unpacking of a list we can use the "*" to unpack a range or an enumerate, or some object, in general, for example, it would be useful in case of passing a number of parameters to a function is quite useful.
nums = range(6)
print(nums)
print(type(nums))


nums_list = list(nums)
print(nums_list)

num_list2 = [*range(0,6,1)]
print(nums_list)



#other examples of how * is very useful in the majority of cases
names = ['Luis', 'Juan', 'Jose', 'Julian']
indexed_names = []

for i, name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name)
print(indexed_names)

indexed_names_com = [(i,name) for i, name in enumerate(names)]
print(indexed_names_com)

indexed_names_un = [*enumerate(names)]
print(indexed_names_un)    

#unpacking a map object

names_map = map(str.upper, names)
print(type(names_map))

names_upp = [*names_map]
print(names_upp)








    
    