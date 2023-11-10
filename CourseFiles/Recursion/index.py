
def FindTarget(nums, num):
  low = 0
  mid = len(nums) - 1/ 2
  high = len(nums) - 1

  if (num > mid):
    low = mid + 1
    mid = (high - low) / 2
  