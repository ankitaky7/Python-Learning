# mutable data types are generally slower than immutable data types

# Dictionary - mutable
# word => meaning 
# {key => val}

marks = {'Math': 99, 'Physics': 101, 'Chemistry': 98}
marks['Math'] = 95
print(marks, type(marks))
print(marks['Chemistry'], marks['Physics'])

for key in marks:
    print(key + ':', marks[key])