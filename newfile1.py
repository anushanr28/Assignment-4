#max of 3 numbers
def max(a,b,c):
	if a>=b and a>=c:
		print(" max of three numbers is",a)
	elif b>=a and b>=c:
		print("max of three number is",b)
	else:
		print("max of three numbers is ",c)
max(9,6,10)

#reverse a string
a=str(input("Enter a string: "))
print("Reverse of the string is: ")
print(a[::-1])

#Prime number or not
num = int(input("enter a number: "))
for i in range(2, num):
	if num % i  == 0:
		print(num," is a not prime number")
		break
else:
	print(num,"is a prime number")

#Palindrome or not using try,expect,finally and else statements 
try:
	num=int(input("Enter a number:"))
except Exception as ValueError:
	print('Invalid input enter a integer')
else:
	temp=num
	rev=0
	while(num>0):
	   	dig=num%10
	   	rev=rev*10+dig
	   	num=num//10
	if(temp==rev):
		print('The number is palindrome')
	else:
		print('Not a palindrome')
finally:
	print('program executed')
	
#Sum of squares of first n natural numbers
def squaresum(n) : 
     return (n * (n + 1) * (2 * n + 1)) // 6
n = int(input('Enter the number:'))
print(squaresum(n)) 
