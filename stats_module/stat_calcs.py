""" This module implements simple statistics functions. """

from math import sqrt

def getNumbers():
    """ This function gets numbers from a user and returns it in a list."""
    nums = []     # start with an empty list

    # sentinel loop to get numbers
    xStr = input("Enter a number (<Enter> to quit) >> ")
    while xStr != "":
        x = float(xStr)
        nums.append(x)   # add this value to the list
        xStr = input("Enter a number (<Enter> to quit) >> ")
    return nums

def mean(nums) :
    """ This function takes a list of numbers as a parameter
        and returns the mean."""
    sum = 0.0  # initialize the sum to 0
    for num in nums:
        sum = sum + num  # increment the sum
    return sum / len(nums)


def stdDev(nums, xbar):
    """ This function takes a list of numbers and a mean as parameters
        and returns the sample standard deviation."""
    sumDevSq = 0.0 # initialize the sum of deviation squares to 0
    for num in nums:
        dev = xbar - num # deviation from mean
        sumDevSq = sumDevSq + dev * dev # increment
    return sqrt(sumDevSq/(len(nums)-1))


def median(nums):
    """ This function takes a list of numbers as a paremeter
        and returns the median."""
    nums.sort() # sort the numbers
    size = len(nums)
    midPos = size // 2 # middle position (by integer division by 2)
    if size % 2 == 0: # even
        median = (nums[midPos] + nums[midPos-1]) / 2
    else: # odd
        median = nums[midPos]
    return median

def geometricMean(nums):
    """This function takes a list of numbers as a parameter
    and returns the geometric mean"""
    n = len(nums) #Set n to the length of the list - how man numbers were provided by the user
    for i in range(len(nums)):
        if i == 0:
            product = nums[i] #If first value set product to that value
        else:
            product = product * nums[i] #multiply the current value of product by the next number in the list

    return product**(1/n)

def harmonicMean(nums):
    """This function takes a list of numbers as a parameter
    and returns the harmonic mean"""
    n = len(nums) #Set n to the length of the list provided 
    sum = 0.0 #initialize sum with a value of 0
    for num in nums:
        sum = sum + (1/num) #Add 1/curent number to the current sum value
    
    return n/sum

def innerProduct(nums1, nums2):
    """This function takes two lists (same length) of numbers as a parameter
    and returns the inner product"""
    innerProduct = 0.0 #Initialize innerProduct with a value of 0
    for i in range(len(nums1)):
        innerProduct = innerProduct + (nums1[i] * nums2[i]) #Add the product of the current ith number from each list to the innerProduct value

    return innerProduct



    


    
