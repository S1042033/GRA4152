from Business_P10_24 import OneTime, Daily, Monthly
import datetime as dt


# Create an empty list to store appointment objects
appointment_list = []

# Start an infinite loop to continually prompt the user for input
while True:
    # Prompt the user to select an action and convert their input into an integer
    choice = int(input("Please select one of the following: \n" +
                       "1. Add appointment \n" +
                       "2. Check appointments on a date \n" +
                       "3. Save the appointments to a file \n" +
                       "4. Load appointments from a file \n" + 
                       "5. Print all appointments \n" +
                       "6. Quit \n" ))
    
    # Break the loop to quit the program if the user selects option 6
    if choice == 6:
        break

    # If the user selects option 1, they want to add a new appointment
    elif choice == 1:
        # Prompt the user to specify the type of appointment to create
        app_type = int(input("Please select the type of appointment: \n" +
                                "1. One time appointment \n" +
                                "2. Daily appointment \n" +
                                "3. Monthly appointment \n"))
        # Get a description for the new appointment
        desc = input("Enter a description for the appointment: ")

        # Create a one-time appointment if that option was selected
        if app_type == 1:
            # Prompt the user for the date details and make sure the date is a valid date
            while True:
                try:
                    day   = int(input("Enter a day as integer: "))
                    month = int(input("Enter a month as integer: "))
                    year  = int(input("Enter a year as integer: "))
                    # This will raise a ValueError if the date is not valid
                    valid_date = dt.datetime(year, month, day)
                    break
                except ValueError as e:
                    print("That's not a valid date. Please try again.")
                    print(f"Error: {e}")
            
            new_app = OneTime(desc, day, month, year) # Instantiate a OneTime appointment object
            appointment_list.append(new_app)          # Add the new appointment to the appointment list
        # Create a daily appointment if that option was selected
        elif app_type == 2:
            new_app = Daily(desc)            # Instantiate a Daily appointment object
            appointment_list.append(new_app) # Add the new appointment to the appointment list
        # Create a monthly appointment if that option was selected
        elif app_type == 3:

            while True:
                day = int(input("Enter a day as integer: "))
                # A simple test for wether the day is valid in any month
                if 1 <= day <= 31:
                    break
                else:
                    print("That's not a valid day. It must be between 1 and 31.")

            new_app = Monthly(desc, day)     # Instantiate a Monthly appointment object
            appointment_list.append(new_app) # Add the new appointment to the appointment list
        else:
            # Inform the user their input was invalid if it wasn't options 1, 2, or 3
            print("Not valid. Please specify 1, 2, or 3.")

    # If the user selects option 2, they want to check appointments on a specific date
    elif choice == 2:
        # Prompt the user for the date details and make sure the date is a valid date
        while True:
            try:
                day   = int(input("Enter a day as integer: "))
                month = int(input("Enter a month as integer: "))
                year  = int(input("Enter a year as integer: "))
                # This will raise a ValueError if the date is not valid
                valid_date = dt.datetime(year, month, day)
                break
            except ValueError as e:
                print("That's not a valid date. Please try again.")
                print(f"Error: {e}")
    
        # Flag to check if any appointments are found
        i = False
        print("---------------------------------------------------")
        print("Appointments on this date:")
        # Iterate over the list of appointments
        for a in appointment_list:
            # Check if the appointment occurs on the given date
            if a.occursOn(day, month, year):
                print(a) # Print the appointment if it does
                i = True # Set the flag to True since we found at least one appointment
        # If no appointments were found, inform the user
        if not i: print("No appointments on this date.")
        print("---------------------------------------------------")

    # If the user selects option 3, they want to save the appointments to a file
    elif choice == 3:
        # Check if there are any appointments to save
        if not appointment_list:
            print("No appointments added or loaded.")
        else:
            # Prompt the user for a filename to save the appointments
            filename = input("Enter a filename (with file format): ")
            # Iterate over the list of appointments and save each to the file
            for a in appointment_list:
                a.save(filename)
    
    # If the user selects option 4, they want to load appointments from a file
    elif choice == 4:
        # Prompt the user for a filename from which to load appointments
        filename = input("Enter a filename (with file format): ")
        try:
            # Open the specified file for reading
            with open(filename, "r") as file:
                # Read each line from the file
                for line in file.readlines():
                    # Determine the type of appointment from the line
                    app_type = next((x for x in ["One", "Daily", "Monthly"] if x in line), False)
                    # Extract the description from the line
                    desc_indx = [i for i in range(len(line)) if line.startswith("'", i)]
                    desc = line[(desc_indx[0]+1):desc_indx[1]]
                    # Create a new appointment object based on the type
                    if app_type == "One":
                        # Parse the date for the OneTime appointment
                        app_date = dt.datetime.strptime(line[(line.find(" at ")+4):len(line)].strip(), "%Y-%m-%d")
                        new_app  = OneTime(desc, app_date.day, app_date.month, app_date.year)
                    elif app_type == "Daily":
                        new_app = Daily(desc)
                    elif app_type == "Monthly":
                        # Parse the day for the monthly appointment
                        app_day = int(line[(line.find(" at ")+4):(line.find(" of ")+1)].strip())
                        new_app = Monthly(desc, app_day)
                    
                    # Change datetime of the object to what is stored in file
                    new_app.load(line) 
                    # Add the new appointment to the list
                    appointment_list.append(new_app)
        except FileNotFoundError:
            # Inform the user if the specified file could not be found
            print("File not found.")
    
    # If the user selects option 5, they want to print all the appointments
    elif choice == 5:
        # Check if there are any appointments to print
        if not appointment_list:
            print("No appointments added or loaded.")
        else:
            print("---------------------------------------------------")
            print("Appointments added or loaded:")
            # Iterate over the list of appointments and print each
            for a in appointment_list:
                print(a)
            print("---------------------------------------------------")

    
