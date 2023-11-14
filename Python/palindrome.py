a = input("enter a word to check palindrome:")
a = a.casefold()
b = reversed(a)
if list(a) == list(b):
    print("The given word is palindrome")
else:
    print("The given word is not a palindrome")

strs = input("Enter a string")
strs = strs.casefold()
if strs == strs[::-1]:
    print("The given word is palindrome")
else:
    print("The given word is not a palindrome")

num = int(input("Enter a value:"))
temp = num
rev = 0
while num > 0:
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
if temp == rev:
    print("This value is a palindrome number!")
else:
    print("This value is not a palindrome number!")
