import hashlib

# passing string that will be hashed
string = input("Enter the text: ")
result = hashlib.md5(string.encode('utf-8'))

print(f"The hash og the string is: {result.hexdigest()}")
