import random

numbers = [1, 2, 3, 4, 5, 9, 10]

random_num = random.choices(numbers, k=2)
print(random_num)

def get_sum(nums):
  sum = 0
  for num in nums:
    sum = num + sum
  print(f'The sum is {sum}')
  return sum


get_sum(numbers)
