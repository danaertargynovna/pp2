#1 example
numbers = [55, 57, 58, 7, 10, 9]
for num in numbers:
    if num % 2 == 0:
        print("First even number", num)
        break
#2 example 
week=['Monday','Tuesday','Wensday','Thursday','Friday','Satutday','Sunday']
for days in week:
    if days=='Sunday':
        print("Weekend")
        break
#3 example
fruits=['banana','cherry','strawberry','bahandi']
for imposter in fruits:
    if imposter=='bahandi':
        print("it is not fruit",imposter)

#4 example 
for i in range(1, 21):
    if i % 7 == 0:
        print("First number divisible by 7 found:", i)
        break
#5 example
numbers = [5, 7, 8, -1, 10]
for n in numbers:
    if n < 0:
        print("Negative number found:", n)
        break