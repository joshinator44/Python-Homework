#! /usr/bin/env python3

# display a welcome message
print("The Test Scores Program\n")
print("Enter all test scores")
print("Enter 'Exit' to quit")
print("=" * 25)

# get scores from the user

total_score = 0
total_score += int(input("Enter test score: "))
total_score += int(input("Enter test score: "))
total_score += int(input("Enter test score: "))
#calculate the average
average_score = round(total_score / 3)

# format and display the results

print("=" * 25)
print("Total score: ", total_score,
      "\nAverage Score: ", average_score)
 
# end the application
print("\nBye")

