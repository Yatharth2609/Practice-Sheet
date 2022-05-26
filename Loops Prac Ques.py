#1]
so=0
se=0
for i in range(12,38):
   if i % 2==0:
      se=se+i
   else:
      so=so+i
print("Sum of all even numbers is ",se)
print("Sum of all odd numbers is ",so)

#2]
for i in range(1,21):
   if i%2!=0 and i%3!=0:
       print(i)

#3]
num=1
i=-1
s=0
while(num!=0):
   num=int(input("Enter any number"))
   s=s+num
   i=i+1
print("Average of numbers entered by you is ",s/i)

#4]
num1 = int(input("Enter any number : "))
r=0
rnum=0
while(num1!=0):
    r = num1 % 10
    rnum = rnum * 10 + r
    num1 = num1//10
print("Reverse number is : ", rnum)

#5]
num1 = input("Enter any number : ")
p=0
L = len(num1)
L1 = list(num1)
i = 0
while(i < L):
   p = p + int(L1[i])**3
   i = i + 1
if int(num1) == p:
    print("Number is Armstrong")
else:
   print("Number is not Armstrong")

#6]
ch = 'Y'
sum = 0
while ch.upper() == 'Y':
     num = int(input("Enter any number  : "))
     sum = sum + num
     ch=input("Do you wish to continue(Y,N)?: ")    
print("Sum of all the numbers is  : ", sum)