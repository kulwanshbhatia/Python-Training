#declare an empty array
user_array=[]

# ask the user to add the size

size = int(input('How many numbers you wana add ... ! '))

for i in range(size):
    num=int(input(f"Enter Value {i+1} : "))
    user_array.append(num)
print(user_array)

# print even and odd no.

for num2 in user_array:
    if(num2%2==0):
        print(f"{num2} is even number ")
    else:
        print(f"{num2} is odd number ")