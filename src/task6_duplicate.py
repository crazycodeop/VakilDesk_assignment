def find_duplicate(nums):
    n = len(nums) - 1 
    arr_sum = sum(nums)
    expected_sum = n * (n + 1) // 2
    return arr_sum - expected_sum

if __name__ == "__main__":
    nums = [1, 3, 4, 2, 5, 5]
    result = find_duplicate(nums)
    print("Duplicate number:", result)
