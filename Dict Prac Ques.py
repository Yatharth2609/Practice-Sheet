#1]
d = { 'a' : 1 , 'b' : 2 }
print ("The value associated with 'c' is : ")
print (d['c'])

#2]
def returnSum(myDict):
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)
    return final
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))

#3]
def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di 
tups = [("akash", 10), ("gaurav", 12), ("anand", 14), 
     ("suraj", 20), ("akhil", 25), ("ashish", 30)]
dictionary = {}
print (Convert(tups, dictionary))

#4]
test_str = 'Dhoni is the best Cricket team Captain!'
print("The original string is : " + str(test_str))
lookp_dict = {"best" : "good and better", "Dhoni" : "all Cricket aspirants"}
temp = test_str.split()
res = []
for wrd in temp:
    res.append(lookp_dict.get(wrd, wrd))
      
res = ' '.join(res)
print("Replaced Strings : " + str(res)) 

#5]
def dictionairy():  
 key_value ={}   
 key_value[2] = 56      
 key_value[1] = 2
 key_value[5] = 12
 key_value[4] = 24
 key_value[6] = 18     
 key_value[3] = 323
 
 print ("Task 1:-\n")
 print ("Keys are")
 for i in sorted (key_value.keys()) :
     print(i, end = " ")
 
def main():
    dictionairy()            
if __name__=="__main__":     
    main()

#6]
test_dict = {"Gfg" : [5, 7, 5, 4, 5],
             "is" : [6, 7, 4, 3, 3], 
             "Best" : [9, 9, 6, 5, 5]}
print("The original dictionary is : " + str(test_dict))
  
max_val = 0
max_key = None 
for sub in test_dict:
    if len(set(test_dict[sub])) > max_val:
        max_val = len(set(test_dict[sub]))
        max_key = sub
print("Key with maximum unique values : " + str(max_key))