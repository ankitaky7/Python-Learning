# List - mutable 'we can change it'

marks = [98, 99, 97, 95, 93, 'A', 92.5]
print(marks, type(marks))

# Length
print(len(marks))

# index
print(marks[0], marks[2])
print(marks[-1]) #last index of the list

# slicing a list - list[st:end], end is not included here
print(marks[0:3])
print(marks[-3:-1])
print(marks[-3:])
print(marks[:3]) 

marks.append(5050)

# to insert at any index
marks.insert(2, 50)

for score in marks:
    print(score)

# to check value is present in list or not
print(50 in marks)

# to clear the list
marks.clear()
print(marks, len(marks)) # to find length use 'len'


# tuple - 'we cannot change or modify it'
nums = (12, 95, 34, 32, 95)
tuple = 23, 43, 12, 34, 23
# nums.clear() cannot perform this kind of operation as it can't be changed
print(nums, type(nums), type(tuple), tuple)
print(nums.count(95))
print(nums.index(95))