print('Welcome to the tip calculator!')

total_bill = input('What was the total bill?\n')
tip_amount = input('How much tip would you like to give? 10, 12, or 15?\n')
num_guests = input('How many people to split the bill?\n')

pay_per_person = (float(total_bill)+float(tip_amount)) / float(num_guests)

print(f'Each person should pay: ${pay_per_person}') 

#done