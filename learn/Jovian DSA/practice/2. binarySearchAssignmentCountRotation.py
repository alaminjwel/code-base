def count_rotations_linear(nums):
	if len(nums)==0:
		return -1
	if len(nums)==1:
		return 0
	if(nums[0]<nums[-1]):
		return 0
	position = 0
	while position<len(nums):
		if position>0 and nums[position]<nums[position-1]:
			return position
		position+=1
	return -1


def count_rotations(nums):
	if len(nums)==0:
		return -1
	if len(nums)==1:
		return 0
	if nums[0]<=nums[-1]:
		return 0
	lo,hi = 0,len(nums)-1
	position=0
	while lo<=hi:
		mid = (lo+hi)//2
		mid_number = nums[mid]
		if mid_number<nums[mid-1]:
			return mid-1 if mid_number<0 else mid
		else:
			if mid_number<=nums[hi]:
				hi=mid-1
			else:
				lo=mid+1
	return -1


print(count_rotations([19, 25, 29, 3, 5, 6, 7, 9, 11, 14]))
# print(count_rotations([3,-1,-2,0,1]))
# print(count_rotations([4,5,6,7,8,-1,-2,-3,0,1,2,3]))