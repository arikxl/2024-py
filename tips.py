bill = float(input("How much is the bill? $" ))

percentage = int(input("what percentage tip do you want to pay? 10, 12 or 15? "))

total_tip = percentage /100 * bill
total_bill = bill + total_tip

friends = int(input("How many friends splits the bill? "))

personal_pay = round(total_bill/friends, 2)

print(f"Each friend need to pay: ${personal_pay}")