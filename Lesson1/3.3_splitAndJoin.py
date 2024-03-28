#Створити змінну split_test = “This is Split Test” і розділити її по пробілам за допомогою функції split(), а потім об'єднати у строку за допомогою функції join() у змінну string_join

split_test = "This is Split Test"
split_test = split_test.split() 
print(split_test)
split_join = " ".join(split_test)
print(split_join)

#4.4 Визначити довжину рядку рядку string_join за допомогою функції len()
split_join_len = len(split_join)
print(split_join_len)