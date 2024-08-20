# Looping over lists

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)

# Exercise
student_scores = [100, 105, 83, 156, 121, 143, 128]

sum_scores = 0
max = 0

for score in student_scores:
    sum_scores += score
    print(sum_scores, "sum")

    if max < score:
        max = score

    print(max, "max")

# Challenge
num_sum = 0
for number in range(1, 101):
    num_sum += number

print(num_sum)