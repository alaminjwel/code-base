# QUESTION 1: You're working on a new feature on Jovian called "Top Notebooks of the Week". 
# Write a function to sort a list of notebooks in decreasing order of likes. 
# Keep in mind that up to millions of notebooks can be created every week, 
# so your function needs to be as efficient as possible.

class Notebook:
	def __init__(self, title, username, likes):
		self.title, self.username, self.likes = title, username, likes

	def __repr__(self):
		return 'Notebook <"{}/{}" {} likes>\n'.format(self.username, self.title, self.likes)

def merge_sort(obj):
	n=len(obj)
	if(n<2):
		return obj
	mid = n//2
	left = obj[:mid]
	right = obj[mid:]
	left = merge_sort(left)
	right = merge_sort(right)
	return merge(left,right)

def merge(left,right):
	lc,rc,l,r=len(left),len(right),0,0
	merged = []
	while l<lc and r<rc:
		if left[l].likes >= right[r].likes:
			merged.append(left[l])
			l+=1
		else:
			merged.append(right[r])
			r+=1
	return merged+left[l:]+right[r:]



nb0 = Notebook('pytorch-basics', 'aakashns', 373)
nb1 = Notebook('linear-regression', 'siddhant', 532)
nb2 = Notebook('logistic-regression', 'vikas', 31)
nb3 = Notebook('feedforward-nn', 'sonaksh', 94)
nb4 = Notebook('cifar10-cnn', 'biraj', 2)
nb5 = Notebook('cifar10-resnet', 'tanya', 29)
nb6 = Notebook('anime-gans', 'hemanth', 80)
nb7 = Notebook('python-fundamentals', 'vishal', 136)
nb8 = Notebook('python-functions', 'aakashns', 74)
nb9 = Notebook('python-numpy', 'siddhant', 92)
notebooks = [nb0, nb1, nb2, nb3, nb4, nb5,nb6, nb7, nb8, nb9]
print(merge_sort(notebooks))