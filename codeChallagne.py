x = [2,5,7,9,0,6,8,5]
min = min(x)
max = max(x)

for i in range(min+1, max):
    if i not in x:
        print(i)

#------------------------------------------

n = 15
num1 = 0
num2 = 1
next_number = num2  
count = 1

while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print() 
