def monotonicIncreasing(nums):
    stack = []

    for num in nums:
        while stack and stack[-1] > num:
            stack.pop()
        stack.append(num)

    return stack

nums = [3, 1, 4, 1, 5, 9, 2, 6]
result = monotonicIncreasing(nums)
print("Monotonic increasing stack: ", result)

def monotonicDecrasing(nums):
    stack = []

    for num in nums:
        while stack and stack[-1] < num:
            stack.pop()
        stack.append(num)
    
    return stack

result = monotonicDecrasing(nums)
print("Monotonic decreasing stack: ", result)