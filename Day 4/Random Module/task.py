import random
import my_module

# random_int = random.randint(1,10)
#
# print(random_int)
# print(my_module.my_favorite_number)
#
#
# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)
#
#
# random_float = random.uniform(1,10)
#
# print(random_float)


random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("Head")
else:
    print("tail")