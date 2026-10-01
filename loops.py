num = 1
while num <=  5:
    print(num)
    num += 1


# bonus challenge


password = ''

while password != 'python':
    password = input('enter your password:')
print("access granted")

for num in range(2, 21, 2):
    print(num)


number = int(input("enter a number to multiply:"))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")