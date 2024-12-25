#Write a program to check whether the given tuple - (1,2,3,3,2,1) is a palindrome or not. If it's a palindrome, then it is the same after being reversed.

def palin(r):
    f=len(r)-1
    s=0
    while s<f:
        if r[s]!=r[f]:
            return False
        s += 1
        f -= 1
    return True
r=(1,2,3,3,2,1)
if palin(r):
    print("This is a palindrome")
else:
    print("This is not a palindrome")        