for i in range(1, 4):
    if i % 2 != 0:
        continue
    print("Even number:", i)

#2
numbers = [54, -41, -8, -43, -10]
for n in numbers:
    if n < 0:
        continue
    print("Positive number:", n)

#3
for i in range(1, 11):
    if i < 10:
        continue
    print( i)

#4
word = "banana"
for ch in word:
    if ch == "n":
        continue
    print(ch, end="")
print() 

#5 exxample
words = ["car", "Apple", "Butter", "Chocolate", "cherry"]
for letters in words:
    if len(letters) < 5:
        continue
    print(letters)