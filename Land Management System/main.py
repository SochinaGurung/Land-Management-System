from operation import rent_land,return_land
from read import read_land_data
import operation

def main():
    """Function to run the land management system.
        
        It displays menus users to rent land, return land and exit the system"""


    d = read_land_data()

    main_loop = True
    while main_loop:
        print("-"*120)
        print("\n")
        print("\t\t\t\t TECHNO PROPERTY NEPAL")
        print("\t\t\t Kathmandu, Nepal | Phone NO: 9862778822")
        print("\t\t\t\t Vat No: 200000000")
        print("\t\t\t\t\t Welcome")
        print("\n")
        print("-"*120)
        print("\t\t\t Please choose from the following options")
        print("\n")
        print("\t\t\t 1. || Press 1 for Renting")
        print("\t\t\t 2. || Press 2 for Returning")
        print("\t\t\t 3. || Press 3 for Exit")
        print("-"*120)
        valid_input=False
        while not valid_input:
            try:
                user_input = int(input("Enter your choice form the given options: "))
                print("-"*120)
                print("\n")
                print("\n")
                valid_input=True
                
        #The customer can rent the land if he chooses option no.1
                if user_input == 1:
                    print("\t\t Welcome to our land management System") 
                    operation.rent_land(d)

        #The customer can return the land they rented if he chooses option no.2
                elif user_input == 2:
                    operation.return_land(d)
                    
        #The customer can exit the land management system if he chooses option no.3
                elif user_input == 3:
                    print("-"*120)
                    print("\t\t\t Thank you for using our land management system")
                    print("-"*120)
                    main_loop = False
                else:
                    print("Invalid input")
                    
              #Exception hhandling  
            except ValueError:
                print("-"*120)
                print("\t\t **Invalid Input.**")
                print("-"*120)
if __name__ == "__main__":
    main()
