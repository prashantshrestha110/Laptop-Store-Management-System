file = open("laptop.txt", "r")

mydict = {}

lap_id = 1





for line in file:

    line = line.replace("\n", "")

    mydict[lap_id] = line.split(",")

    lap_id += 1





def buy_laptop():

    print("Enter your details name and number for bill: ")

    print("---------------------------------------------------------------------")



    print("Customer details:")
     
    print("\n")

    name = input("Customer name:")

    phone = input("Phone number of customer: ")    

    while len(phone) != 10:

        try:

            phone = input("Phone number of customer : ")

        except ValueError:

            print("Invalid input")



    print("----------------------------------------------------------------------")

    print("S.N\tName\t\tBrand\tPrice\tQuantity\tCPU\tGraphics")

    a = 1

    file = open('laptop.txt', 'r')

    for line in file:

        print(a, "\t"+line.replace(",", "\t"))

        a += 1

    file.close()

    print("-------------------------------------------------------------------------")



    valid_id = int(input("Enter laptop ID: "))

    while valid_id <= 0 or valid_id > len(mydict):

        print("Error please enter again")

        valid_id = int(input("Enter laptop ID: "))



    user_quantity = int(input("Enter quantity of laptop:"))



    get_quantity = mydict[valid_id][3]

    while user_quantity <= 0 or user_quantity > int(get_quantity):

        print("Quantity invalid ")

        user_quantity = int(input("Enter quantity of laptop:"))



    mydict[valid_id][3] = int(mydict[valid_id][3]) - int(user_quantity)

    file = open('laptop.txt', 'w')



    for values in mydict.values():

        file.write(str(values[0])+","+str(values[1])+","+str(values[2]) +

                   ","+str(values[3])+","+str(values[4])+","+str(values[5]))

        file.write("\n")

    file.close()



    product_name = str(mydict[valid_id][0])

    user_quantity = str(user_quantity)

    per_price = str(mydict[valid_id][2])

    price = str(mydict[valid_id][2].replace("$", ""))

    amount = str(int(price)*int(user_quantity))

    tot = str(float(int(amount)+(0.13)*(int(amount))))



    shipping_cost = input(

        "Do you want the laptop to be shipped? (y/n)").lower()

    if shipping_cost == "y":

        tot = str(float(tot)+100)



    dir = [product_name, user_quantity, per_price, amount, tot]



    with open('buy.txt', 'w') as buy:



        buy.write(

            "\n\n\n----------------------------------------------------------------------------------\n")

        buy.write("\t\t\t\tBILL\n")

        buy.write(

            "----------------------------------------------------------------------------------\n")

        buy.write("\t\t\t\t\Prashant electronics\n")

        buy.write("\t\t\tThulobhyaryang,kathmandu\n")

        buy.write(

            "----------------------------------------------------------------------------------\n\n")



        buy.write("\nCustomer name: "+name+"\n")

        buy.write("Phone number of customer: "+phone+"\n")

        buy.write("\n")

        buy.write(

            "----------------------------------------------------------------------------------\n")

        buy.write("\t\t\t   Your order:\n")

        buy.write(

            "----------------------------------------------------------------------------------\n")

        buy.write(

             "\n\nProduct name\t\tquantity\tUnit Price\tnet amount\tTotal\n")

        for i in dir:

            buy.write(i+"\t\t")



    f = open('buy.txt', 'r')

    inside = f.read()

    print(inside)

    f.close()
