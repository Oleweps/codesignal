# You are given an array of integers. Your job is to return the count of even and odd integers in the
# given array without using any built-in Python methods.

# Your function should return a tuple in the format (even_count, odd_count), where even_count represents the number of even
# integers and odd_count represents the number 
# of odd integers 
# in the provided array

def solution(nums):
    # TODO: implement the function to return a tuple (even_count, odd_count)
    even = 0
    odd = 0
    
    #iterate through the list of integers
    for i in nums:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
            
    return (even, odd)