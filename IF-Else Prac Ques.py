#1]
amt=0
n=int(input("Enter number of electric units:"))
if n<=100:
     amt=0
if n>100 and n<=200:
     amt=(n-100)*5
if n>200:
     amt=500+(n-200)*10
print("Amount to be paid :",amt)

#2]
num=int(input("Enter any number"))
ld=num%10
if ld%3==0:
     print("Last digit of number is divisible by 3 ")
else:
     print("Last digit of number is not divisible by 3 ")

#3]
tax = 0
pr=int(input("Enter the price of bike"))
if pr > 100000:
     tax = 15/100*pr
elif pr >50000 and pr <=100000:
     tax = 10/100*pr
else:
     tax = 5/100*pr
print("Tax to be paid ",tax)

#4]
city = input("Enter name of the city")
if city.lower()=="delhi":
    print("Monument name is : Red Fort")
elif city.lower()=="agra":
    print("Monument name is : Taj Mahal")
elif city.lower()=="jaipur":
    print("Monument name is : Jal Mahal")
else:
    print("Enter correct name of city")

#5]
na=0
d=0
mp=int(input("Enter marked price"))
if mp > 10000:
     d = 20/100*mp
if mp > 7000 and mp <= 10000:
     d = 15/100*mp
if mp <= 7000:
     d = 10/100*mp
na = mp-d
print("Net amount to pay ", na)

#6]
nd = int(input("Enter number of days "))
if nd <= 5:
    amt = nd * 2
elif nd >=6 and nd <=10:
    amt = nd * 3
elif nd >= 11 and nd <= 15:
    amt = nd * 4
else:
    amt = nd * 5
print("Total amount to pay is ", amt)

