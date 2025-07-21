def write_land_data(data):
    """ Writing the updated data in the land.txt file"""
    
    file= open("land.txt", "w")
    for key, value in data.items():
        file.write(key + "," + ",".join(value))
        file.write("\n")

def write_rent_bill(file_path, customerFname,customerLname, contact_number, today_date_and_time, bills, grand_total):
    """"Writing the renting of the bill on rent_land.txt file"""

    file=open("rent_land.txt", "w")
    file.write("\n")
    file.write("\t \t \t \t Techno Property Nepal ")
    file.write("\n")
    file.write("\t \t Kamalpokhari, Kathmandu | Phone No: 9811112255 ")
    file.write("\n")
    file.write("\t\t\t\t\t Vat No: 20000000")
    file.write("\n")
    file.write("\t\t\t\t\t Rent Bill")
    file.write("\n")
    file.write("-"*120)
    file.write("\n")
    file.write("Customers Detail :")     #Writing renting customer details
    file.write("\n")
    file.write("-"*120)
    file.write("\n")
    file.write("Name of the Customer: " + str(customerFname+" "+customerLname))
    file.write("\n")
    file.write("Contact number: " + str(contact_number))
    file.write("\n")
    file.write("Date and time of purchase: " + str(today_date_and_time))
    file.write("\n")
    file.write("-"*120)
    file.write("\n")
    file.write("Land Rent Details are:")
    file.write("\n")
    file.write("-"*120)
    file.write("\n")
    file.write("LandID \t City \t\tDirection \tPrice  \t\tRented Month \t\tTotal Price")
    file.write("\n")
    file.write("-"*120)
    file.write("\n")
    for each in bills:
        file.write("\n")
        file.write(str(each[0]) + "\t" + str(each[1]) + "\t" + str(each[2]) + "\t\t" + str(each[3]) + "\t\t" + str(each[4]) + "\t\t" + str(each[5])+"/n")
        file.write("\n")
    file.write("\n")
    file.write("="*120)
    file.write("\n")
    file.write("Grand Total: " + str(grand_total))
    file.write("\n")
    file.write("="*120)
    


def write_returning_bill(file_path, customerFname,customerLname, contact_number, today_date_and_time, bills, grand_total,months):
    """Writing the returning of bill on return_bill.txt file"""

    file=open("return_bill.txt", "w")
    file.write("\n")
    file.write("\t \t \t \t Techno Property Nepal ")
    file.write("\n")
    file.write("\t \t Kamalpokhari, Kathmandu | Phone No: 9811112255 ")
    file.write("\n")
    file.write("\t\t\t\t Vat No: 20000000")
    file.write("\n")
    file.write("\t\t\t\t Return Bill")
    file.write("\n")
    file.write("-"*120)
    file.write("\n")
    file.write("Customers Detail :")            #Writing returning customer details
    file.write("\n")
    file.write("-"*120)
    file.write("\n")
    file.write("Name of the Customer: " + str(customerFname+" "+customerLname))
    file.write("\n")
    file.write("Contact number: " + str(contact_number))
    file.write("\n")
    file.write("Date and time of purchase: " + str(today_date_and_time))
    file.write("\n")
    file.write("-"*120)
    file.write("\n")
    file.write("Land Return Details are:")
    file.write("\n")
    file.write("-"*120)
    file.write("\n")
    file.write("LandID \t City \t\tDirection \tPrice  \t\tRented Month \t\tTotal Price")
    file.write("\n")
    file.write("-"*120)
    file.write("\n")
    for each in bills:
        file.write("\n")
        file.write(str(each[0]) + "\t" + str(each[1]) + "\t" + str(each[2]) + "\t\t" + str(each[3]) + "\t\t" + str(each[4]) + "\t\t" + str(each[5]))
        file.write("\n")
    file.write("\n")
    file.write("="*120)
    #Fining a customer if he returned land after 24 months
    '''if months<24:
        file.write("Grand Total: " + str(grand_total))
    else:
        Fine=10/100*int(selected_item[3])
        grand_price=Fine+grand_total'''
    file.write("\n")
    file.write(" Total Price: " + str(grand_total))
    file.write("\n")
    '''file.write("Fine amount:"+str(Fine))
    file.write("\n")
    file.write("Grand price with fine:" +str(grand_price))'''
    file.write("="*120)
    file.write("\n")

        

        
