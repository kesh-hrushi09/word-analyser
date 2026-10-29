user = input("Enter a word: ")

r = user[::-1]
U = user.upper()
l = len(user)
middle = l // 2
m = user[middle]
f = ord(user[0])

if user == r:
    is_palindrome = True
else:
    is_palindrome = False
    
print(f" reversed: {r}")
print(f" Uppercase: {U}")
print(f" length: {l}")
print(f" middle character: {m}")
print(f"first letter character code: {f}")
print(f" palindrome: {is_palindrome}")