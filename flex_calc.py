# Declaration
number_1 = 10
number_2 = 20
number_3 = 30
number_4 = 40
number_5 = 50

# List is a collection of variables
# Consecutive Boxes Allocated
list_of_numbers = [10, 20, 30, 40, 50]


user_is_giving_input = True
# Input (Dry Run)
while user_is_giving_input:  # 1) True True True False
  user_input = input("Enter the number: ")  # 1 2 3
  if user_input != "done":
    list_of_numbers.append(int(user_input))
  else:
    user_is_giving_input = False


# Process

# Output (Result)
print("The last number is: ", list_of_numbers[len(list_of_numbers)-1])
