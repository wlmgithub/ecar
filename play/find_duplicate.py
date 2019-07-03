
#https://leetcode.com/problems/find-the-duplicate-number/discuss/314940/Python-Bit-Manipulation-(68ms)


def findDuplicate(nums):
	b = 0 << (len(nums)-1)
	for n in nums:
		a = b | 1 << (n-1)
		if a == b: return n
		else: b = a

def findDuplicate_2(nums):
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break

        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


def findDuplicate_3(nums):
        return (sum(nums) - sum(set(nums)))//(len(nums) - len(set(nums)))



def findDuplicate_4(nums):
        from collections import Counter
        return Counter(nums).most_common(1)[0][0]


nums = [2,3,1,3,4]

print(nums, findDuplicate(nums), 'using bit')
print(nums, findDuplicate_2(nums), 'using tortoise/hare')
print(nums, findDuplicate_3(nums), 'using sum')
print(nums, findDuplicate_4(nums), 'using Counter')
