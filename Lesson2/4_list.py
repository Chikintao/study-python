#Створити змінну list_append = [1,2,3] і за допомогою функції append() додати туди спочатку 4, потім 5
list_append = [1,2,3]
list_append.append(4)
list_append.append(5)

print(list_append)

#Створити змінну list_extend = [4,5,6] і розширити цей список іншим за допомогою функції extend()
list_extend = [4,5,6]
list_extend.extend(list_append)
#list_append.extend(list_extend)

print(list_extend)

#Визначити індекс елемента 6 у списку list_extend за допомогою функції index()

ind = list_extend.index(6)
print(ind)

#Визначити довжину списку list_append за допомогою функції len()
print(len(list_extend))