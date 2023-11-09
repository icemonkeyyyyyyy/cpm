def find_pair(nums, s):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == s:
            return nums[left], nums[right]
        elif current_sum < s:
            left += 1
        else:
            right -= 1

    return None


x = [4, 5, 8, 9, 12, 16, 18]
s = 16

pair = find_pair(x, s)
if pair:
    print(pair)
else:
    print("Пары нету")

