# staircase.py

'''
Absolutely, below is a Python function called create_staircase that attempts to form a staircase out of the numbers in the input list, and returns False if it can’t.

Each iteration of the while loop fills one step of the staircase, with the progress of the staircase tracked within the subsets variable. So the first iteration fills the subsets list with [1], the second iteration adds [2, 3] to the subsets list, and so on.

At each iteration, the nums list is reduced by removing the elements used for the current step. If at any point the nums list is not empty and the number of remaining elements in the nums list is less than the current step size, then the function returns False since the next step will only be partially filled. If the nums list is emptied without running into this issue, then that means each step was created successfully and therefore a valid staircase was constructed, which is then returned by the function.
'''

def test() :
  print("bite me")

# A incorrectly initialzes step and subsets within While
def create_staircase1(nums) :
  while len(nums) != 0 :
    step = 1
    subsets = []

    if len(nums) >= step :
      subsets.append(nums[0 : step])
      nums = nums[step : ]
      step = step + 1

    else:
      return False

    return subsets

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
  
# test()
a = [1, 2, 3, 4, 5, 6]
b = [1, 2, 3, 4, 5, 6]

# print(create_staircase1(a))
# print(create_staircase2(b))