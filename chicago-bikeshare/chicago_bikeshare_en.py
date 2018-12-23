
# coding: utf-8

# Here goes the imports
import csv
import matplotlib.pyplot as plt
import datetime as dt
from os import path

# Let's read the data as a list
print("Reading the document...")
filepath = path.abspath(path.join(path.dirname(__file__), "chicago.csv"))
with open(filepath, "r") as file_read:
	reader = csv.reader(file_read)
	data_list = list(reader)
print("Ok!")

# Let's check how many rows do we have
print("Number of rows:")
print(len(data_list))

# Printing the first row of data_list to check if it worked.
print("Row 0: ")
print(data_list[0])
# It's the data header, so we can identify the columns.

# Printing the second row of data_list, it should contain some data
print("Row 1: ")
print(data_list[1])

input("Press Enter to continue...")
# TASK 1
# TODO: Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")

print('\n'.join(map(str, data_list[:20])))

# Let's change the data_list to remove the header from it.
data_list = data_list[1:]

# We can access the features through index
# E.g. sample[6] to print gender or sample[-2]

input("Press Enter to continue...")
# TASK 2
# TODO: Print the `gender` of the first 20 rows

print("\nTASK 2: Printing the genders of the first 20 samples")

for i in range(20):
	print(data_list[i][6])

# Cool! We can get the rows(samples) iterating with a for and the columns(features) by index.
# But it's still hard to get a column in a list. Example: List with all genders

input("Press Enter to continue...")
# TASK 3
# TODO: Create a function to add the columns(features) of a list in another list in the same order

def column_to_list(data, index):
	"""
	Given a matrix, returns designated column as a list.
	Args:
		data: The matrix
		index: The index of the column to be returned as a list
	Returns:
		The desired column as a list.
	"""
	column_list = [item[index] for item in data]
	return column_list


# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(column_to_list(data_list, -2)[:20])

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TASK 3: The list doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
# TASK 4
# TODO: Count each gender. You should not use a function to do that.
male = 0
female = 0
for gender in column_to_list(data_list, -2):
	if gender == 'Male':
		male += 1
	elif gender == 'Female':
		female += 1

# Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Why don't we creeate a function to do that?
# TASK 5
# TODO: Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)
def count_gender(data_list):
	"""
	Counts how many Males and Females are there in the gender column (index=-2) of the data matrix.
	Args:
		data_list: The data matrix
	Returns:
		A list of two items containing the count of Males and Females
	"""
	count_male, count_female = 0, 0
	genders = column_to_list(data_list, -2)
	for gender in genders:
		if gender == 'Male':
			count_male += 1
		elif gender == 'Female':
			count_female += 1
	return [count_male, count_female]


print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we can count the users, which gender use it the most?
# TASK 6
# TODO: Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.
def most_popular_gender(data_list):
	"""
	Uses count_gender function to determine the most popular gender.
	Args:
		data_list: The data matrix
	Returns:
		"Equal", when the gender count is equal
		"Male", if Male is the predominant gender
		"Female", if Female is the predominant gender
	"""
	males, females = count_gender(data_list)
	answer = "Equal" if males == females else "Male" if males > females else "Female"
	return answer


print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

# If it's everything running as expected, check this graph!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 7
# TODO: Plot a similar graph for user_types. Make sure the legend is correct.
print("\nTASK 7: Check the chart!")

def count_user_type(data_list):
	"""
	Counts how many Subscriber, Customer and Dependent are there in
	the user type column (index=-3) of the data matrix.
	Args:
		data_list: The data matrix
	Returns:
		A list of three items containing the counts of Subscriber, Customer and Dependent
	"""
	count_subscriber, count_customer, count_dependent = 0, 0, 0
	user_type_list = column_to_list(data_list, -3)
	for user_type in user_type_list:
		if user_type == 'Subscriber':
			count_subscriber += 1
		elif user_type == 'Customer':
			count_customer += 1
		elif user_type == 'Dependent':
			count_dependent += 1
	return [count_subscriber, count_customer, count_dependent]

user_type_list = column_to_list(data_list, -3)
types = ["Subscriber", "Customer", "Dependent"]
quantity = count_user_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('User Type')
plt.xticks(y_pos, types)
plt.title('Quantity by User Type')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 8
# TODO: Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Because there are len(data_list) - (935854 + 298784) = 316868 entries where gender is not available."
print("Answer:", answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Let's work with the trip_duration now. We cant get some values from it.
# TASK 9
# TODO: Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().

def get_median(data):
	"""
	Calculate the median value of a list of floats.
	Args:
		data: The list of floats
	Returns:
		The median value of a list
	"""
	middle = len(data) // 2
	data.sort()
	if len(data) % 2 > 0:
		return data[middle]
	elif len(data) % 2 == 0:
		return (data[middle] + data[~middle]) / 2.0

trip_duration_list = column_to_list(data_list, 2)
trip_duration_list = [float(duration) for duration in trip_duration_list]

min_trip = float('inf')
max_trip = 0
mean_trip = 0
median_trip = get_median(trip_duration_list)

for item in trip_duration_list:
	duration = float(item)
	mean_trip += duration
	min_trip = duration if min_trip > duration else min_trip
	max_trip = duration if max_trip < duration else max_trip

mean_trip = mean_trip / len(trip_duration_list)

print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 10
# Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# TODO: Check types how many start_stations do we have using set()
user_types = set(column_to_list(data_list, 3))

print("\nTASK 10: Printing start stations:")
print(len(user_types))
print(user_types)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(user_types) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# def new_function(param1: int, param2: str) -> list:
"""
Example function with annotations.
Args:
	param1: The first parameter.
	param2: The second parameter.
Returns:
	List of X values

"""

input("Press Enter to continue...")
# TASK 12 - Challenge! (Optional)
# TODO: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it?")
answer = "yes"

def count_items(column_list):
	"""
	Counts distinct types in a list.
	Args:
		column_list: The list to count items from
	Returns:
		A list of the distinct types and a list of each respective count
	"""
	item_types = list(set(column_list))
	count_items = [0] * len(item_types)
	for item in column_list:
		for i, atype in enumerate(item_types):
			if atype == item:
				count_items[i] += 1
				break
	return item_types, count_items


if answer == "yes":
	# ------------ DO NOT CHANGE ANY CODE HERE ------------
	column_list = column_to_list(data_list, -2)
	types, counts = count_items(column_list)
	print("\nTASK 11: Printing results for count_items()")
	print("Types:", types, "Counts:", counts)
	assert len(types) == 3, "TASK 11: There are 3 types of gender!"
	assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
	# -----------------------------------------------------


# -------------------- EXTRA TASKS --------------------
# EXTRA TASK #1 Plot a histogram of the age distribution

def get_duration_by_age(data_list, min_age=0, max_age=120):
	"""
	Calculates the age for the entries where Birth Year is available,
	and create a tuple containing age and trip duration.
	Args:
		data_list: The data matrix
		min_age: A threshold for the minimum age
		min_age: A threshold for the maximum age
	Returns:
		A list of tuples formed by age and trip duration
	"""
	results = []
	current_year = dt.datetime.now().year
	for row in data_list:
		birth_year = row[-1]
		if birth_year == '':
			continue
		age = current_year - round(float(birth_year))
		# Filter by min and max ages
		if age > max_age or age < min_age:
			continue
		trip_duration = round(float(row[2]))
		results.append((age, trip_duration))
	return results

duration_by_age_lst = get_duration_by_age(data_list)
ages_lst, duration_lst = zip(*duration_by_age_lst)

# Plot Histogram from 0 to 120 years old
plt.hist(ages_lst, bins=50, color='green', edgecolor='black')
plt.ylabel('Quantity')
plt.xlabel('Age')
plt.title('Histogram of Age Distribution')
plt.show(block=True)

# From the histogram we conclude that there aren't many records
# outside the range of 18 to 70 years old
# Let's plot another histogram within those constraints

duration_by_age_lst = get_duration_by_age(data_list, min_age=18, max_age=70)
ages_lst, duration_lst = zip(*duration_by_age_lst)

plt.hist(ages_lst, bins=50, color='green', edgecolor='black')
plt.ylabel('Quantity')
plt.xlabel('Age')
plt.title('Histogram of Age Distribution')
plt.show(block=True)

# Task: Plot the average duration trip per age using a bar chart

count_by_age = count_items(ages_lst)

mean_duration_by_age = []
for i, age in enumerate(count_by_age[0]):
    duration_sum_by_age = sum([item[1] for item in duration_by_age_lst if item[0] == age])
    mean = duration_sum_by_age // count_by_age[1][i]
    mean_duration_by_age.append((age, round(mean)))

x = [i[0] for i in mean_duration_by_age]
y = [i[1] for i in mean_duration_by_age]
plt.bar(x, y)
plt.ylabel('Average Trip Duration')
plt.xlabel('Age')
plt.title('Bar Chart of Average Trip Duration by Age')
plt.show(block=True)