palindrome = lambda x: x == x[::-1]

strings = ["malayalam", "red","madam","hi"]

palindromes = list(filter(palindrome, strings))

if palindromes:
    print("Palindromes :",palindromes)
else:
    print("No palindromes.")
