def eratosthenes(n):
    nums = [i for i in range(2, n + 1)]
    x = 0
    f = 2
    end_1 = []
    while x < len(nums):
        f = nums[x]
        end = []
        for i in range(len(nums)):
            if nums[i] % f != 0 or nums[i] == f:
                end.append(nums[i])
            else:
                end_1.append(nums[i])
        nums = end
        x += 1
    print(*end_1)
eratosthenes(15)