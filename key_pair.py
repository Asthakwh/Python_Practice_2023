#combine 2 dictionories

from collections import Counter
d1 = {'key1': 50, 'key2': 100, 'key3':200}
d2 = {'key1': 300, 'key2': 400, 'key3':250}
new_dict = Counter(d1) + Counter(d2)
print(new_dict)