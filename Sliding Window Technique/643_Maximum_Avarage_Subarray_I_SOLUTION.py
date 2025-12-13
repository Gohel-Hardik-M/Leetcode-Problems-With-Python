'''            
                                                                  PROBLEM STATEMENT 
                                                                  _________________
                                                                  
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000

'''

# SOLUTION CODE :

def MaxAvarage(arr , k):
  # k --->window size 
  # arr -->>array (COntaining Elements)
  window_sum = 0
  for i in range(0,k):
    window_sum += arr[i]

  max_sum = window_sum
  
  for i in range(k , len(arr)):
    window_sum += arr[i]  - arr[i-k]
    if window_sum > max_sum :
      max_sum = window_sum 

  return max_sum/k 
  
    






