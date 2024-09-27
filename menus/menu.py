import utils.helpers as ut
import data.scraping as da
import pandas as pd
from output import export as ex

def mainMenu():

    """
    Displays the main menu and handles user input to navigate through different options.
    
    The user can choose to export data to Excel or CSV, filter the data by name, or sort 
    the data by price (ascending or descending) or by kilometers. The loop continues until 
    the user chooses to exit the program.
    
    Inputs:
        User is prompted to enter a number corresponding to the desired option.
    
    Behavior:
        - If the input is invalid (not between 1 and 7), an error message is displayed.
        - If the input is 7, the program exits.
        - Otherwise, the selected option is processed in the `menuOptions` function.
    """

    continue_program = True

    while continue_program:
        correct_option = False

        while not correct_option:
            
            option = int(input("\n=====Welcome===== \n Choose one of the following options \n 1- Exportar a formato xlsx o csv \n 2- Export data to CSV \n 3- Filter by name \n 4- Sort by ascending price \n 5- Sort by descending price \n 6- Sort by kilometers \n 7- Exit the program \n "))

            if option < 1 or option > 7:
                print("Incorrect option, please choose a number between 1 and 7")
            elif option == 7:
                continue_program = False
                print("Connection closed successfully.")
                break
            else:
                correct_option = True
                menuOptions(option)


def export_data(data):

    my_data = data
    
    option = int(input("Elije una opción: Excel [1], Csv [2]:  "))

    if option < 1 or option > 2:
        print("Incorrect option, please choose a number between 1 and 2")
    if option == '1':
        df = pd.DataFrame(my_data)
        ex.export_to_excel(df, 'Cars.xlsx')
        ut.return_to_menu()
    elif option == '2':
        df = pd.DataFrame(my_data)
        ex.export_to_csv(df, 'Cars.csv')
        ut.return_to_menu()
       

def filter_by(data):
    
    my_data = data
    
    option = int(input("Elije una opción: nombre [1], precio_asc [2], precio_dsc [3], kilometros_asc [4]:  "))

    if option < 1 or option > 4:
        print("Incorrect option, please choose a number between 1 and 4")    
    if option == 1:
        new_data = ut.filter_by_name(my_data)
        df = pd.DataFrame(new_data)
        print(df)
        ut.return_to_menu()
    elif option == 2:
        new_data = ut.sort_by_price_asc(my_data)
        df = pd.DataFrame(new_data)
        print(df)
        ut.return_to_menu()
        # Sort by ascending price
    elif option == 3:
        new_data = ut.sort_by_price_desc(my_data)
        df = pd.DataFrame(new_data)
        print(df)
        ut.return_to_menu()
        # Sort by descending price
    elif option == 4:
        new_data = ut.sort_by_km_asc(my_data)
        df = pd.DataFrame(new_data)
        print(df)
        ut.return_to_menu()

def menuOptions(option):

    """
    Handles the selected option from the main menu.

    Args:
        option (int): The option selected by the user in the main menu.
    
    Behavior:
        - Option 1: Scrapes the data, converts it to a DataFrame, and exports it to an Excel file.
        - Option 2: Scrapes the data, converts it to a DataFrame, and exports it to a CSV file.
        - Option 3: Scrapes the data, filters it by a name specified by the user, converts it to a DataFrame, and displays it.
        - Option 4: Scrapes the data, sorts it by ascending price, converts it to a DataFrame, and displays it.
        - Option 5: Scrapes the data, sorts it by descending price, converts it to a DataFrame, and displays it.
        - Option 6: Scrapes the data, sorts it by kilometers in ascending order, converts it to a DataFrame, and displays it.
    
    Post-Processing:
        After processing, the user is returned to the main menu.
    """

    my_data = da.scrape_all_pages()

    if option == 1:
        export_data(my_data)
    elif option == 2:
        filter_by(my_data)
