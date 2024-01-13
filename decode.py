# decode.py

'''
  Absolutely! Below is a Python function that attempts to form the input array into a staircase. Each iteration of the while loop fills one step of the staircase by appending the current step to the subsets list. If the nums list has less elements than the necessary step amount for a given iteration, then the array isn't a staircase and the function returns False, otherwise it returns the staircase.
  '''
def create_staircase2(nums) :
  step = 1
  subsets = []

  while len(nums) != 0 :
      
    if len(nums) >= step:
      subsets.append(nums[0 : step])
      nums = nums[step : ]
      step = step + 1

    else:
      return False
      
  return subsets

