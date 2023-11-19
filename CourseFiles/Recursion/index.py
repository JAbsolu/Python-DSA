
def sum(nums):
  if len(nums)==1:
    return nums[0]
  else:
    return sum(nums[1:])+nums[0]

print(sum([2,4,6,8,4,3,4,6,1]))

students = {
  1: {
    "first_name": "John",
    "last_name": "Doe",
    "age": 20,
  },
  2: {
    "first_name": "Jane",
    "last_name": "Doe",
    "age": 20,
  },
  3: {
    "first_name": "Jim",
    "last_name": "Doe",
    "age": 20,
  },
  "student4": {
    "first_name": "Jill",
    "last_name": "Doe",
    "age": 20,
  },
  4: {
    "first_name": "Joe",
    "last_name": "Doe",
    "age": 20,
  },
}


def get_full_name(obj):
  if obj[1]:
    print(obj[1]["first_name"]+" "+obj[1]["last_name"])
  else:
     print(get_full_name(obj[1:]) + ", " + obj[1]["first_name"] + " " + obj)

get_full_name(students)