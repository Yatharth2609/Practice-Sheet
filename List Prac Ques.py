#1]
name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
animal = ['Cat', 'Dog', 'Fish', 'Goat']
age = [1, 2, 2, 6]
z = zip(name, animal, age)
for name,animal,age in z:
    print("%s the %s is %s" % (name, animal, age))

#2]
def multiplyList(myList) :
    result = 1
    for x in myList:
         result = result * x
    return result
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))

#3]
list1 = [10, 20, 4, 45, 99]
list1.sort()
print("Smallest element is:", *list1[:1])

#4]
test_list = [5, 6, [], 3, [], [], 9]
print("The original list is : " + str(test_list))
res = [ele for ele in test_list if ele != []]
print("List after empty list removal : " + str(res))

#5]
test_list = [5, 6, [], 3, [], [], 9]
print("The original list is : " + str(test_list))
res = [ele for ele in test_list if ele != []]
print("List after empty list removal : " + str(res))