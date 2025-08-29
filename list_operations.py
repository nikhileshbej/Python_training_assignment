
# Create an empty list to store scores.
scores = []
print(scores)

# Append the scores: 85, 90, 78, 92, 88)
scores.append(85)
scores.append(90)
scores.append(78)
scores.append(92)
scores.append(88)
print(scores)

# Insert the score 80 at index 3
scores.insert(3, 80)
print(scores)

# Remove the score 92 from the list
scores.remove(92)
print(scores)

# Sort the scores in ascending order
scores.sort()
print(scores)

# Reverse the list
scores.reverse()
print(scores)

#Find and print the maximum and minimum score
max_score = max(scores)
print("max score =", max_score)

min_score = min(scores)
print("min score =", min_score)

# Check if 90 is in the list
index = scores.index(90)
if index > 0:
    print("90 is present")
else:
    print("90 is not present")

# Print the total number of scores
print("Total number of scores = ", len(scores))

# Slice and print the first three scores
sliced_list = scores[0:3]
print(sliced_list)

# Find the last element from the list
print("last element = ", scores[-1])

# Replace the score 100 with new score on the index 2

scores[2] = 100
print("List after replacement = ", scores)

# create a new copied list also
copied_list = scores.copy()
print("Copied list = ", copied_list)
















