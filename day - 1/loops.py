# Create a list of your 5 favorite movies, and use a loop to print them.

fav_movies = ["interstellar", "atmapaphlet", "blackmail", "lunch box", "border"]

for movie in fav_movies:
    print(movie)


# ✅ Mini Task 2:
# Ask the user to enter 5 numbers, store them in a list, then:

numbers = []

for i in range(1, 5):
    number = int(input("Enter a number"))
    numbers.append(number)
    

# Print the list

for num in numbers:
    print(num)

# Print the sum

sum = 0

for num in numbers:
    sum += num

print("Sum is ", sum)


# Print the average

print("Average is ", sum / len(numbers))

# Print the maximum

max = numbers[0]

for num in numbers:
    if max < num:
        max = num

print("Max is ", max)