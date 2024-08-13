# find the largest and smallest meaning in the dictionary:
dict1 = {
    'piece':'portion of an object or of material,produced by cutting',
    'patch':'a piece of cloth or other material used mend or stengthen a torn or weak point',
    'area': 'a region or part of  a town , a country or the world',
    'visit':'go to see and spend time with (someone)',
    'with':'having or possessing',
    'small':'less than normal'
}
#way1
list1 = list(dict1.keys())
list2 = list(dict1.values())
lens = [len(i) for i in list2]
max_length = max(lens)
min_length = min(lens)

max_index=lens.index(max_length)
min_index=lens.index(min_length)
print(list1[max_index])
print(list1[min_index])

#way2
maxlength=max(len(dict1[i]) for i in dict1)
for i in dict1:
    if len(dict1[i])==maxlength:
        print(i)
minlength = min(len(dict1[i]) for i in dict1)
for i in dict1:
    if len(dict1[i])==minlength:
        print(i)


#
# length=0
# for i in dict1:
#     if(len(dict1[i])>length):
#         length=len(dict1[i])
# print(length)
# for i in dict1:
#     if(len(dict1[i])==length):
#         print(i)
#
# for i in dict1:
#     length=len(dict1[i])
#     print(length)
#     if(length>len(dict1[i+1])):

# print(length)
# for i in dict1:
#     if(len(dict1[i])==length):
#         print(i)