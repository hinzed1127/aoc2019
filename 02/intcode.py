program = open('input.txt')

# https://stackoverflow.com/questions/18332801/how-to-read-an-array-of-integers-from-single-line-of-input-in-python3
arr = list(map(int, program.read().split(',')))

arr[1] = 12
arr[2] = 2

# for index, value in enumerate (arr):
# 	print(index, value)

def add(x, y, output):
	arr[output] = arr[x] + arr[y]

def multiply(x, y, output):
	arr[output] = arr[x] * arr[y]
	

i = 0 

while arr[i] != 99:
	if arr[i] == 1:
		add(arr[i+1], arr[i+2], arr[i+3])
	elif arr[i] == 2:
		multiply(arr[i+1], arr[i+2], arr[i+3])
	else:
		print('Not 1 or 2, something went wrong')
	i += 4

print(arr[0])