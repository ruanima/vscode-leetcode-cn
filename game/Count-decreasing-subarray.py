'''

You are given an array of integers arr. Your task is to count the number of contiguous subarrays, such that elements of the subarray are arranged in strictly decreasing order.

For example, if arr = [9, 8, 4, 9, 3], then the subarray [9, 8, 4] meets the criteria (9 > 8 > 4), but the subarray [8, 4, 9] does not.

Example

For arr = [9, 8, 7, 6, 5], the output should be solution(arr) = 15.

All contiguous subarrays satisfy the condition of problem, because all elements of the array are arranged in decreasing order. There are 15 possible contiguous subarrays, so the answer is 15.

For arr = [10, 10, 10], the output should be solution(arr) = 3.

Since all of the elements are equal, the subarrays can't be in strictly decreasing order unless they contain only one element. There are 3 possible subarrays containing one element, so the answer is 3.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer arr

An array of integers.

Guaranteed constraints:
1 ≤ arr.length ≤ 105,
-109 ≤ arr[i] ≤ 109.

[output] integer64

Return the number of contiguous subarrays with elements in strictly decreasing order.

'''

# [Python 3] Syntax Tips

# # Prints help message to the console
# # Returns a string
# def helloWorld(name):
#     print("This prints to the console when you Run Tests")
#     return "Hello, " + name

def solution(arr: list) -> int:
    if len(arr) < 2:
        return len(arr)
    i = 0
    j = 1
    count = 0
    length = 1
    while j < len(arr):
        if arr[j] < arr[i]:
            j += 1
        else:
            length = j - i
            count += (length+1)*length//2
            i = j
            j += 1
    length = j-i
    return count + (length+1)*length//2

print(solution([9, 8, 7, 6, 5, 9, 8, 7]))
