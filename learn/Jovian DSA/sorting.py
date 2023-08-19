import random

def bubble_sort(nums):
	for _ in range(len(nums)-1):
		for i in range(len(nums)-1):
			if(nums[i]>nums[i+1]):
				nums[i],nums[i+1] = nums[i+1],nums[i]
	return nums



def insertion_sort(nums):
	for i in range(len(nums)):
		cur = nums[i]
		j = i-1
		while j>=0 and nums[j]>cur:
			nums[j+1] = nums[j]
			j-=1
		nums[j+1] = cur
	return nums



def merge_sort(nums):
	n = len(nums)
	if n<2:
		return nums

	mid = n//2
	left = nums[:mid]
	right = nums[mid:]
	left = merge_sort(left)
	right = merge_sort(right)
	return merge(left,right)

def merge(left,right):
	lc = len(left)
	rc = len(right)
	l = r = 0
	merged = []
	while l<lc and r<rc:
		if left[l]<=right[r]:
			merged.append(left[l])
			l+=1
		else:
			merged.append(right[r])
			r+=1
	while l<lc:
		merged.append(left[l])
		l+=1

	while r<rc:
		merged.append(right[r])
		r+=1

	return merged



def quick_sort(nums,start=0,end=None):
	if end is None:
		end = len(nums)-1

	if start<end:
		pivot = quick_partition(nums,start,end)
		quick_sort(nums,start,pivot-1)
		quick_sort(nums,pivot+1,end)
	return nums

def quick_partition(nums,start=0,end=None):
	if end is None:
		end = len(nums)-1
	L = start
	R = end-1
	while R>L:
		if nums[L]<=nums[end]:
			L +=1
		elif nums[R]>nums[end]:
			R -=1
		else:
			nums[L],nums[R] = nums[R],nums[L]
	if nums[L]>nums[end]:
		nums[L],nums[end] = nums[end],nums[L]
		return 1
	else:
		return end




in_list = list(range(30))
random.shuffle(in_list)
print(bubble_sort(in_list))
print(insertion_sort(in_list))
print(merge_sort(in_list))
print(quick_sort(in_list))
