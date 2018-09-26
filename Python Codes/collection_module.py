#Collection Modules in Python

#Counter Object

from collections import Counter

num_list = [1,1,1,3,4,5,3,2,3234,12,24,23,12,12,23,24,5,5,1,5,1]
print(Counter(num_list))
counter_obj = Counter(num_list)
print(counter_obj.most_common(3))

word = 'Hey, my name is Abhijeet what is your name and what are you doing boss what kind of person you are'
my_list = word.split()
print(Counter(my_list))
counter_obj2 = Counter(my_list)
print(counter_obj2.most_common(3))


#DefaultDict

from collections import defaultdict

d = defaultdict(lambda: 0)
print(d['key1'])
print(d['key2'])

print(d)