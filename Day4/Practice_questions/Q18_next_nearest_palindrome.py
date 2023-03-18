def is_palindrome(n):
    if(n==n[::-1]):
        return True
    return False
n=input()
while(True):
    n=str(int(n)+1)
    if(is_palindrome(n)):
        print(n)
        break