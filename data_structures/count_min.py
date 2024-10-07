# You are given an array of integers. Your task is to write a function in Python that 
# returns the number of times the smallest element appears in the array.

# Please note that built-in methods such as min() or count() should not be used in this task. 
# Your goal is to accomplish this task by iterating over the array elements manually. 
# Try to solve the task by doing just a single list traversal.
def count_min(numbers):
    if not numbers:
        return 0
    # TODO: Implement this function to count the smallest integer in the list.
    mini_num = numbers[0]
    count_min = 1
    
    for i in numbers[1:]:
        if i < mini_num:
            mini_num = i 
            count_min = 1
        elif i == mini_num:
            count_min += 1
    return count_min
print("Test 1:", count_min([3, 1, 4, 1, 5, 1]))
