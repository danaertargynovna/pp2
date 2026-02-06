#1
word = "python"
for snake in word:
    print(snake)
#2
for i in range(3):
    print(i)

#3
colors = ["blue", "green"]
shapes = ["circle", "square"]
for color in colors:
    for shape in shapes:
        print(color, shape)
#4
numbers = [1, 2, 3, 4]
for num in numbers:
    print(num)
#5
total = 0
for i in range(1, 11):
    if i % 2 == 0:
        total += i
print("Even sum =", total)


