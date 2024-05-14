# Random module
import random

# randonint(a, b): random interger between a, b and include a and b
random_int = random.randint(1, 10)
print(random_int)

random_float = random.random()
print(random_float)

rand = random_int * random_float

print(rand)
