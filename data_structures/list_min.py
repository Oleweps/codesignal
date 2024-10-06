def find_min(nums):
    # TODO: implement the function to find the minimum number from a list
    if not nums:
        return None
    min = nums[0]
    for i in nums[1:]:
        if i < min:
            min = i
    return min