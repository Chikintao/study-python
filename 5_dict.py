#Створити змінну dict_test = {“car”:”Toyota”, “price”:4900, “where”:”EU”} та вивести на екран дані,які знаходяться в ключах car та where
dict_test = {'car':'Toyota', 'price':4900, 'where':'EU'}

print(dict_test.get("car"))
print(dict_test.get("where"))

#За допомогою функції keys() і values() вивести на екран ключі та їх значення

print(dict_test.keys())
print(dict_test.values())

#За допомогою функції items() вивести на екран пари ключ - значення

print(dict_test.items())