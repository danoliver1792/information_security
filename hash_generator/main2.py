import hashlib

string = input("Enter the text: ")

menu = int(input(''' -- menu --
choose hash type: 
[ 1 ] MD5
[ 2 ] SHA1
[ 3 ] SHA256
[ 4 ] SHA512
enter the number to generate: '''))

if menu == 1:
    result = hashlib.md5(string.encode('utf-8'))
    print(f"The hash of the string is: {result.hexdigest()}")
elif menu == 2:
    result = hashlib.sha1(string.encode('utf-8'))
    print(f"The hash of the string is: {result.hexdigest()}")
elif menu == 3:
    result = hashlib.sha256(string.encode('utf-8'))
    print(f"The hash of the string is: {result.hexdigest()}")
elif menu == 4:
    result = hashlib.sha512(string.encode('utf-8'))
    print(f"The hash of the string is: {result.hexdigest()}")
else:
    print("Error! Enter a valid number")
