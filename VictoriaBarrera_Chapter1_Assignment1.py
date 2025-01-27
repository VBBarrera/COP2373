# Victoria Barrera Exercise 1.
def sell_tickets(available_tickets):

    # This function prompts the user for the desired number of tickets and checks that the purchase is valid.

    while True:
        try:
            desired_tickets = int(input("Please enter the number of tickets you would like to buy (Max 4): "))

            # Check if the number of tickets bought is in the range of 4.
            if desired_tickets < 1 or desired_tickets > 4:
                print("Up to 4 tickets can be bought.")
            elif desired_tickets > available_tickets:
                print(f"Only {available_tickets} tickets are left.")
            else:
                available_tickets -= desired_tickets
                print(f"Remaining tickets: {available_tickets}")
            break
        except ValueError:
            print('Invalid number of tickets.')
    return available_tickets


# The main function contains an accumulator that keeps count of the buyers.
def main():

    # sets the number of total tickets and accumulator.
    total_tickets = 20
    buyers_count = 0

    # The variable accumulates the buyers, and the loop continues until there are no more tickets.
    while total_tickets > 0:
        buyers_count += 1
        total_tickets = sell_tickets(total_tickets)

    # Print the results.
    print("\nAll tickets have been sold.")
    print(f"Total number of buyers: {buyers_count}")


# Call the main function.
if __name__ == "__main__":
    main()
