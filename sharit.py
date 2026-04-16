print("Try programiz.pro")
def fac(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fac(n-1)
def trailingzero(n):
    x = fac(n)
    count = 0
    while(n%10 == 0):
        count = count+1
        n = n/10
    return count
number = int(input("Enter a number : "))
x = fac(number)
print(f"Factorial {x}")
y = trailingzero(x)
print(f"Trailing Zero {y}")
