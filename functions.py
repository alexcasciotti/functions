def binary_search(list, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(list) - 1
    if(low > high):
        return -1
    mid = (low + high) // 2
    if(list[mid] == target):
        return mid
    if(list[mid] < target):
        new_low = mid + 1
        return binary_search(list, target, new_low, high)
    if(list[mid] > target):
        new_high = mid - 1
        return binary_search(list, target, low, new_high)