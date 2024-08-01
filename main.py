import buy
import sell


print("\n")

print("---------------------------------------------------------")

print("\t\tPrashant electronics")

print("\t\tThulobhyaryang,kathmandu")

print("---------------------------------------------------------")

System_loop = True


while System_loop:

    try:

        print("Press 1 to Purchase Laptop")

        print("Press 2 to Sell laptop ")

        print("Press 3 to exit")

        user_input = int(input("Enter: "))

        if user_input == 1:

            buy.buy_laptop()
            
            
        elif user_input == 2:

            sell.sell_laptop()
            

        elif user_input == 3:

            print("Thank you, We hope we could see you again")

            break

        else:
            print("Enter a valid option")

        choice = input("Do you want to buy or sell anything again? (Y/N): ")

        if choice.upper() == 'N':

            System_loop = False
    except:

        print("Error - Enter a valid input from 1 to 3")
