import random
print("random():", random.random())
print("random():", random.random())

import random
print("uniform(1,10):", random.uniform(1,10))
print("uniform(1,10):", random.uniform(1,10))

import random
print("randint(1,6):", random.randint(1,6))
print("randint(1,6):", random.randint(1,6))

import random
print("choice([1,2,3,4,5,6]):", random.choice([1,2,3,4,5,6]))
print("choice([1,2,3,4,5,6]):", random.choice([1,2,3,4,5,6]))
print("choice('python'):", random.choice([1,2,3,4,5,6]))
print("choice('python'):", random.choice("python"))

import random
list1=[15,23,4,88,7]
print("원래의 리스트:", list1)
random.shuffle(list1)
print("순서가 변경된 리스트:", list1)
