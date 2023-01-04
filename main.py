from random import choice

# variable to store amount of choices
user_answer = int(input('How many options do you want to pick from?: '))
user_list = []

# for loop that runs for commanded number of times
for num in range(user_answer):
    user_list.append(str(input('Enter option: ')))

print(choice(user_list))