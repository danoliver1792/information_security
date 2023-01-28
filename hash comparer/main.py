import hashlib

file_one = "a.txt"
file_two = "b.txt"

hash_one = hashlib.new("ripemd160")

# file to compare to hash
hash_one.update(open(file_one, "rb").read())

hash_two = hashlib.new("ripemd160")

hash_two.update(open(file_two, "rb").read())

# comparison
if hash_one.digest() != hash_two.digest():
    print(f"The file {file_one} is different from {file_two}")
else:
    print(f"The file {file_one} equals {file_two}")
