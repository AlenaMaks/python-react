# 2 задание
dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}
keys = set(dct.keys())
values = set()
for key in keys:
    values.add(dct.get(key))
print(f"Множество ключей: {keys}")
print(f"Множество значений: {values}")
print(f"Объединение множеств: {set(list(keys) + list(values))}")
