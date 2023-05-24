def locate_card(nums,target):
	i = 0
	while i<len(nums):
		if nums[i] == target:
			return i
		i+=1
	return -1

def locate_card_bs(nums,target):
	lo,hi = 0,len(nums)-1
	i = 0
	while lo<=hi:
		mid = (lo+hi)//2
		if nums[mid]==target:
			return mid
		else:
			if target > nums[mid]:
				hi = mid-1
			else:
				lo = mid+1

	return -1

print(locate_card_bs([8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],3))