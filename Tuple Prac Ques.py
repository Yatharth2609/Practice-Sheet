#1]
tuplex = (4, 8, 3) 
print(tuplex)
n1, n2, n3 = tuplex
print(n1 + n2 + n3) 
n1, n2, n3, n4= tuplex 

#2]
tuplex = ("y", "a", "t", "h", "a", "r", "t", "h")
print(tuplex)
item = tuplex[3]
print(item)
item1 = tuplex[-4]
print(item1)

#3]
test_list = [5, 6, 7]
print("The original list is : " + str(test_list))
test_tup = (9, 10)
test_list += test_tup

#4]
test_tup = (7, 8, 9, 1, 10, 7) 
print("The original tuple is : " + str(test_tup)) 
res = sum(list(test_tup))
print("The summation of tuple elements are : " + str(res)) 

#5]
import collections 
Output = collections.defaultdict(int)
Input = [[('hi', 'bye')], [('Geeks', 'forGeeks')],
         [('a', 'b')], [('hi', 'bye')], [('a', 'b')]]
for elem in Input:
      Output[elem[0]] += 1
print(Output)