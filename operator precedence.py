a=6
b=8
c=75
d=10

print(a+c/d)
print(c-d/a)
print(b/d*c)
print(d%a-b)

# task 2

#write to check a number is divisible by another number

num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))

calc = num1 % num2
if calc == 0:
    print("this number is divible")
else:
    print("this number isn't divisible")


# task 3

# The mean of 40 numbers is 38. Later on, I detected that I misread the number 56 as 36. Find the correct mean of given numbers.

sum = (40*38)+56-36
mean = sum/40
print(mean)
