# Solution for Q2

def is_palindrome(num: int):
    if num<0:
        return False
    return num==int(str(num)[::-1])

#Use case 1
print("Use case 1:")
x1=121
print(is_palindrome(num=x1))

#Use case 2
print("Use case 2:")
x2=-121
print(is_palindrome(num=x2))

#Use case 3
print("Use case 3:")
x3=10
print(is_palindrome(num=x3))