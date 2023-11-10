
def sum(nums):
  if len(nums)==1:
    return nums[0]
  else:
    return sum(nums[1:])+nums[0]

print(sum([2,4,6,8,4,3,4,6,1]))
  