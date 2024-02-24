# Given an array of positive integers a, your task is to calculate the sum of every possible a[i] ∘ a[j], where a[i] ∘ a[j] is the concatenation of the string representations of a[i] and a[j] respectively.

# Example

# For a = [10, 2], the output should be solution(a) = 1344.

# a[0] ∘ a[0] = 10 ∘ 10 = 1010,
# a[0] ∘ a[1] = 10 ∘ 2 = 102,
# a[1] ∘ a[0] = 2 ∘ 10 = 210,
# a[1] ∘ a[1] = 2 ∘ 2 = 22.
# So the sum is equal to 1010 + 102 + 210 + 22 = 1344.

# For a = [8], the output should be solution(a) = 88.

# There is only one number in a, and a[0] ∘ a[0] = 8 ∘ 8 = 88, so the answer is 88.


#8 hidden tests didn't pass
def solution(a):
    pairs=[]
    ans =0
    for i in range(len(a)):
        for j in range(len(a)):
            pairs.append([str(a[i]), str(a[j])])
    for nums in pairs:
        curr = ""
        curr+=nums[0]
        curr+=nums[1]
        ans +=int(curr)
    return ans


def otherSolution(a):
    count = 0
    tmp = 0
    # sum of right hand sides
    for i in range(len(a)):
        for j in range(len(a)): 
            count += a[j]

    for i in range(len(a)):
        for j in range(len(a)): 
            count += a[j] * offset(a[j])

    return count

#pass all tests
def solution(a):
    lowSum = 0
    cnt = 0
    for i in range(len(a)):
        lowSum += a[i];

    cnt += lowSum * len(a)

    for j in range(len(a)): 
        size = len(str(a[j]))
        offset = iPower(10, size)
        cnt = cnt + lowSum * offset

    return cnt

def iPower(base, power):
    result = 1
    for i in range(1,power+1):
        result *= base
    return result