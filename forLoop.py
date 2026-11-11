# for loop

nums = range(2) # 0 to 4

for i in nums:
    print(i)

for i in range(5,1001):
    print(i)

print("multiples of 3 from 1 to 50")
for i in range(1, 51):
    if i == 21:
        continue
    if(i % 3 == 0):
        print(i)

print("Out of Loop")