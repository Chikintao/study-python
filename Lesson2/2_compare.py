#Використати вивченні оператори та порівняти між собою числа, рядки, булеві значення, списки, словники, кортежи

num1 = 12
num2 = -5
print(num2<num1)

str1 = "Max"
str2 = "Olya"
print(str1>str2)

bool1 = True
bool2 = False
print(bool1 > bool2)

list1 = {"running", "art", "programming"} 
list2 = {"running", "art", "programming","swimming"} 
print(list1 > list2)

my_info = {"name":"Max", "age": 25, "city": "Kiev"}
my_info2 = {"name":"Max", "age": 25}
print(my_info == my_info2) # < > не підтримуються для словників

tuple1 = ("running", "art", "programming" )
tuple2 = ("running", "art", "programming","swimming" )
print(tuple1 > tuple2)
