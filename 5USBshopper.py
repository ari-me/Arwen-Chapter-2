#Chapter 2 - Exercise 5
#The word problem:
print("A girl heads to a computer shop to buy some USB sticks.\nShe loves USB sticks and wants as many as she can get for 50$. They are 6$ each.\nHow many USB sticks can she buy and how many will she have left?")
#The equation:
girls_money, usb_price = 50, 6 #The given
usb_sticks = girls_money//usb_price #How many USB sticks she can buy
remaining_money = girls_money % usb_price #How much money she will have left
print(f"\tTHE ANSWER: \n\tShe can buy {usb_sticks} USB sticks and will have {remaining_money}$ left.")