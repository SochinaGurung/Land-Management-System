def read_land_data():
    """ Read the datas of land from the file and inserts it in the dictionary
        It reads land.txt reads each lines extracts data and store it in the
        dictionary in key value form where labd id is key and land attributes are
        values"""
        
    d = {}
    with open("land.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.replace("\n", "")  #Removing newline character
            l = line.split(",")  #Split the line by commas
            k = l[0]            #The first element in dictionary is land id
            value = l[1:]       #Attributes
            d[k] = value        #Adding key value in dictionary
    file.close
    return d


def land_details():
    """Prints the details of the lands
        Reads the land.txt file and prints the land details in table form
        """
    
    print("-"*110)
    print("\n")
    print("\t\t\t\t TECHNO PROPERTY NEPAL")
    print("\t\t\t Kathmandu, Nepal | Phone NO: 9862778822")
    print("\t\t\t\t Vat No: 200000000")
    print("\t\t\t\t\t Welcome")
    print("\n")
    print("\t\t ***Following are the land details***")
    print("-"*110)
    print("Kitta\t\tCity\t\tDirection\t\t Aana\t\tPrice\t\tAvailability")
    print("-"*110)
    file= open("Land.txt","r")

    for line in file:
        print(line.replace(",","\t\t"))     #Replace commas with tabbed spaces
    file.close()
    print("-"*110)
