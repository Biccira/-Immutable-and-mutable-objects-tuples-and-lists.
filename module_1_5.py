immutable_var = 1, 2, True, 'Hello'
print(immutable_var)
# immutable_var[0] = 200
# print(immutable_var) - попытались изменить кортеж, но он являесться не изеняемым, в отличие от списка, но в кортеж можно добавить список который можно будет изменить.
immutable_var = [1,2], 2 , 3
print(immutable_var)
immutable_var[0][0] = 3
print(immutable_var) # добавление списка
mutable_list = [1, 2, True, 'Hello']
print(mutable_list)
mutable_list[0] = 5
print(mutable_list) # список
