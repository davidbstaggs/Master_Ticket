TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100

def calculate_price(num_o_tickets):
    return num_o_tickets * TICKET_PRICE + SERVICE_CHARGE
while tickets_remaining >= 1:
    print(f"There are currently {tickets_remaining} tickets left!")
    name = input("Hello, and welcome to Ticketmaster, What is your name?  ")
    tickets_wanted = input(f"Nice to meet you {name}, and how many tickets would you like today?  ")
    try:
        tickets_wanted = int(tickets_wanted)
        if tickets_wanted > tickets_remaining:
            raise ValueError(f"There are only {tickets_remaining} tickets remaining.")
    except ValueError as err:
        print(f"Oh no, we ran into an issue ({err}), please try again")
    else:
        print(f"The total for your purchase today, including a $2 service charge, will be {calculate_price(tickets_wanted)}")
        confirm = input(f"Would you like to proceed with your purchase of {tickets_wanted} tickets, {name}?  Y/N  ")
        if confirm.lower() == "y":
            print("SOLD!!")
            tickets_remaining -= tickets_wanted
        else:
            print(f"Thank you for your time, {name}, and we hope the rest of your day is wonderful")
print(f"{name}, thank you for your purchase, tickets are now sold out.")

