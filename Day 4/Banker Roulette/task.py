import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
len_of_friends = len(friends)-1
print(friends[random.randint(0,len_of_friends)])
print(random.choice(friends))