from datetime import datetime
from read import read_land_data
from write import write_land_data, write_rent_bill,write_returning_bill
import read

def rent_land(d):
    read.land_details() #calling function from read and diaplays land details
    l = list(d.keys())  
    bills=[]
    grand_total=0
    more_rent=True
    while more_rent:
        valid=True
        while valid:
            try:
                land_id = input("Enter your desired land id that you like to rent: ")
                if land_id not in l:
                    print("\n")
                    print("Invalid LandId!!")
                    print("-"*120)
                    

                elif d[land_id][-1].lower() == "not available":   #Checking the availability of land
                    print("\n")
                    print("The land id you entered is not available at the moment.\n Please choose another land to rent.")
                    print("-"*120)
                    
                else:
                    print("\n")
                    print("Valid Land ID")
                    print("-"*120)
                    valid=False
        

            except ValueError:              #Handling value error
                print("***Invalid Input***")
            

        month_rent=True
        while month_rent==True:
            try:
                user_month=int(input("Please enter your desired month to rent the land: "))     #Asking customer for their desired land
                if user_month<=0:
                    print("\t\t\t\t Invalid Input!!")
                                                    
                else:
                    print("\n")
                    print("Land can be rented for "+ str(user_month) + " months")
                    print("-"*120)
                    month_rent=False

            except ValueError:
                print("-"*120)
                print("\t\t\tInvalid Input!!")


        selected_item = d[land_id]
        items = [land_id, selected_item[0], selected_item[1], selected_item[3], user_month, int(selected_item[3]) * user_month]
        bills.append(items)  #appending the valuesS
        selected_item[4] = "Not Available"      #Converting Available land into unavailable
        grand_total += int(selected_item[3]) * user_month   #Calculating the grand total of after

                    
        more_rent=True
        while more_rent==True:
            #Checking if the user wants to rent more land
            user_input=input(" Would you like to rent more land?\n \n \t\tEnter yes or no:")
            print("-"*120)           
            if user_input=="yes":
                
                month_rent=True
                break
    
            elif user_input=="no":
                more_rent=False
            else:
                print("please enter yes or no")
                
        #Asking renter for their first and last name         
    validName=True
    while validName==True:
        customerFname=input(" Pleaese enter your first name:")
        if customerFname.isalpha():
            validName=False
            break
        else:
            print("\t\t\t Invalid Input")
    validName=True
    while validName==True:
        customerLname=input("Please enter your last name:")
        if customerLname.isalpha():
            validName=False
            break
        else:
            print("\t\t\t Invalid Input!!")

         #Asking renter for their contact number       
    validContact=True
    while validContact==True:
        try:
            contact_number=int(input(" Please enter your contact number:"))
            print("-"*120)
            validContact=False
            break
        except ValueError:
                print("***Invalid Input***")

                                        

        # Updating Dictionary and writing to the files
    write_land_data(d)

        # Print bills for the renter when they rent land
    grand_total = 0
    for i in bills:
        grand_total += int(i[5])

    today_date_and_time = datetime.now()

    print("\n")
    print("\t \t \t \t Techno Property Nepal ")
    print("\t \t Kamalpokhari, Kathmandu | Phone No: 9811112255 ")
    print("\t\t\t\t Vat No: 20000000")
    print("\t\t\t\t\t INVOICE")
    print("\n")
    print("-"*120)
    print("Customers Detail :")
    print("-"*120)
    print("Name of the Customer: " + str(customerFname+" "+customerLname))
    print("Contact number: " + str(contact_number))
    print("Date and time of purchase: " + str(today_date_and_time))
    print("-"*120)
    print("\n")
    print("Land Rent Details are:")
    print("-"*120)
    print("LandID \t City \t\tDirection \tPrice  \t\tRented Month \t\tTotal Price")
    print("-"*120)
    for each in bills:
        print(str(each[0]) + "\t" + str(each[1]) + "\t" + str(each[2]) + "\t\t" + str(each[3]) + "\t\t\t" + str(each[4]) + "\t\t" + str(each[5]))
    print("="*120)
    print("Grand Total: " + str(grand_total))
    print("="*120)
    print("\n")

    write_rent_bill("bill.txt", customerFname,customerLname, contact_number, today_date_and_time, bills, grand_total)

    print("\t\t**Thank you for using our land management system**")  
        

def return_land(d):
    """
        It handles the customers desire to return the land they rented
        This function allows user to return one or multiple lands genertes
        return bill and updates the unavailable land to available

    """
    
    read.land_details()     #Calling function land details from read.py to display land details
    l=list(d.keys())
    bills=[]
    grand_total=0
    more_return=True
    while more_return==True:
        returning=True
        while returning==True:
            try:
                land_id=input("Please enter the id of the land that you want ro return:").strip()           # Asking returner to enter the land id
                if land_id not in l:
                    print("\n")
                    print("Invalid LandId!!")
                    print("-"*120)
                
                elif d[land_id][-1].lower() == "available":  #Cecking availability of the land and available land cant be returned
                    print("\n")
                    print("The land id you entered is already available. ")
                    print("-"*120)
                
                else:
                    print("\n")
                    print("Valid Land ID")
                    print("-"*120)
                    returning=False

            except ValueError:
                print("***Invalid Input***")

        month_return=True
        while month_return==True:
            try:
                months=int(input("Enter the number of months that you rented the land:"))           #Asking returner to enter the monthe they rented land
                if months<=0:
                    print("***Invalid Input***")
                elif months>24:
                    print("\n")
                    print("Since you are returning the land after more than the promised time, you will be fined 10% more.")            #Fining the customer
                    print("\n")
                    month_return=True
                else:
                    print("\n")
                    print("You rented the land for "+ str(months) + " months.")
                    print("-"*120)
                    month_return=False
                    
            except ValueError:
                print("-"*120)
                print("\t\t\t Invalid True")

    
        selected_item = d[land_id]
        items = [land_id, selected_item[0], selected_item[1], selected_item[3], months, int(selected_item[3]) * months]
        bills.append(items)                 #Appending items into the bill
        selected_item[4] = " Available"                 #Changing availability to available after return
        grand_total += int(selected_item[3]) * months          #Calculatinng the amount for land return
                
        #Asking customer if they have more land to return
        more_return=True
        while more_return==True:
            user_input=input(" Would you like to return more land?\n \n \t\tEnter yes or no:")                 
            print("-"*120)
            if user_input=="yes":
                month_return=True
                break
            elif user_input == "no":
                more_return=False

        # Asking customer for their details
    validName=True
    while validName==True:
        customerFname=input(" Pleaese enter your first name:")
        if customerFname.isalpha():
            validName=False
            break
        else:
            print("\t\t\t Invalid Input")
    ValidName=True
    while ValidName==True:
        customerLname=input("Please enter your last name:")
        if customerLname.isalpha():
            validName=True
            break
        else:
            print("\t\t\t Invalid Input!!")
             
                                
    #Asking customer for their contact information
    validContact=True
    while validContact==True:
        try:
            contact_number=int(input(" Please enter your contact number:"))
            print("-"*120)
            validContact=False
            break
                                                       
        except ValueError:
            print("***Invalid Input***")

    #Updating dictionary and writing to the files
    write_land_data(d)
                                        
    # Printing bill for the returne
    grand_total = 0
    for i in bills:
        grand_total += int(i[5])

    today_date_and_time = datetime.now()

    print("\n")
    print("\t \t \t \t Techno Property Nepal ")
    print("\t \t Kamalpokhari, Kathmandu | Phone No: 9811112255 ")
    print("\t\t\t\t Vat No: 20000000")
    print("\t\t\t\t\tINVOICE")
    print("\n")
    print("-"*120)
    print("Customers Detail :")
    print("-"*120)
    print("Name of the Customer: " + str(customerLname)+" "+customerLname)
    print("Contact number: " + str(contact_number))
    print("Date and time of purchase: " + str(today_date_and_time))
    print("-"*120)
    print("\n")
    print("Land Return Details are:")
    print("-"*120)
    print("LandID \t City \t\tDirection \tPrice  \t\tRented Month \t\tTotal Price")
    print("-"*120)
    for each in bills:
        print(str(each[0]) + "\t" + str(each[1]) + "\t\t" + str(each[2]) + "\t\t" + str(each[3]) + "\t\t\t" + str(each[4]) + "\t\t" + str(each[5]))
        print("="*120)
    '''if months<=24:
        print("Grand Total: " + str(grand_total))
    else:
        Fine=10/100*int(selected_item[3])
        grand_price=Fine+grand_total'''
    print("\n")
    print(" Total Price: " + str(grand_total))
    '''print("\n")
    print("Fine amount:"+str(Fine))
    print("\n")
    print("Grand price with fine:" +str(grand_price))'''
    print("="*120)
    print("\n")

    write_returning_bill("bill.txt", customerFname,customerLname, contact_number, today_date_and_time, bills, grand_total,months)
                                                             
                                                
    print("\t\t**Thank you for using our land management system**")
            
            

