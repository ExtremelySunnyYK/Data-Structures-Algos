# binary search
# bianry search is a search algorithm that finds the position of a target value within a sorted array.
# The algorithm works by searching the middle element of an array,
# comparing the target value to the middle element, and swapping the target value with the middle element if the target value is greater than the middle element.
# The algorithm repeats this process until the target value is found or the array is empty.
# The algorithm is a divide and conquer algorithm.

def binary_search(nums: List[int], target: int) -> int: ):
    mid=len(nums) // 2
    if nums[mid] == target:
        return mid

    if nums[mid] > target:
        return binary_search(nums[:mid], target)
    else:
        return binary_search(nums[mid+1:], target) + mid + 1


def binarySearchIterative(left, right, nums, target):
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1