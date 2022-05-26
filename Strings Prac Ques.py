#1]
def palindrome(a):
    mid = (len(a)-1)//2     
    start = 0
    last = len(a)-1
    flag = 0
    while(start <= mid):
        if (a[start]== a[last]):
             
            start += 1
            last -= 1
             
        else:
            flag = 1
            break;
    if flag == 0:
        print("The entered string is palindrome")
    else:
        print("The entered string is not palindrome")

#2]
def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["PHP", "Exercises", "Backend"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])

#3]
def odd_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

print(odd_values_string('abcdef'))
print(odd_values_string('python'))

#4]
str1 = "Yatharth"
char_dict = dict()
for char in str1:
    count = str1.count(char)
    char_dict[char] = count
print('Result:', char_dict)

#5]
str_list = ["Sam", "Jon", "", "Henriken", None, "Eric", ""]
res_list = []
for s in str_list:
    if s:
        res_list.append(s)
print(res_list)