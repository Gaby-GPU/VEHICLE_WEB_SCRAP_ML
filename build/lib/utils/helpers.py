def parse_html_to_data(soup):

    """
    Parses HTML content from a BeautifulSoup object and extracts relevant data 
    about items listed on a webpage. This function is tailored to work with 
    specific HTML structures commonly found on e-commerce websites.

    Args:
        soup (BeautifulSoup): A BeautifulSoup object containing the parsed HTML of the webpage.

    Returns:
        list: A list of dictionaries, where each dictionary contains the following keys:
            - 'title': The title of the item.
            - 'price': The price of the item without the thousands separator.
            - 'currency': The currency of the item (e.g., 'ARS' for Argentine Peso, 'USD' for US Dollar).
            - 'year': The year of manufacture of the item (if applicable).
            - 'KM': The number of kilometers (if applicable).
            - 'location': The location of the item.
            - 'Url': The URL to the item's detailed page.
    """

    items = soup.find_all("li", {'class': 'ui-search-layout__item'})
    data_list = []

    for item in items:
        data = {}

        # Title
        try:
            title_tag = item.find(class_='ui-search-item__title')
            if not title_tag:
                raise ValueError("Title tag not found")
        except ValueError:
            title_tag = item.find(class_='poly-component__title')

        if not title_tag:
            data['title'] = 'Title not found'
        else:
            data['title'] = title_tag.text

        # Price
        price_tag = item.find(class_='andes-money-amount__fraction')
        if not price_tag:
            data['price'] = 'Price not found'
        else:
            data['price'] = price_tag.text.replace(".", "")

        # Currency Symbol
        symbol_tag = item.find(class_='andes-money-amount__currency-symbol')
        if not symbol_tag:
            data['currency'] = 'Currency not found'
        else:
            if symbol_tag.text == '$':
                data['currency'] = 'ARS'
            else:
                data['currency'] = 'USD'

        # KM and Year
        year = 'N/A'
        kilometers = 'N/A'
        
        attributes_list = item.find(class_='poly-attributes-list')
        if attributes_list:
            attributes = attributes_list.find_all('li', class_='poly-attributes-list__item')
            if len(attributes) >= 2:
                kilometers = attributes[0].text.strip()
                year = attributes[1].text.strip()

        if year == 'N/A':
            continue
        
        data['year'] = year
        data['KM'] = kilometers

        # Location

        location = item.find(class_='poly-component__location')
        if not location:
            continue
        data['location'] = location.text


        # URL
        url_tag = item.find(class_='ui-search-link')
        if url_tag and url_tag.has_attr('href'):
            data['Url'] = url_tag['href']
        else:
            data['Url'] = 'URL not found'



        data_list.append(data)
    
    return data_list

def convert_to_number(price_str):
    """
    Converts a price string with symbols and dots to a numeric value.
    
    Args:
        price_str (str): Price in string format with symbol and dots.

    Returns:
        int: Price converted to an integer.
    """
    price_str = price_str.replace('$', '').replace('.', '')  # Removes dollar symbol and dots
    return int(price_str)

def sort_by_price_asc(products):
    """
    Sorts a list of products by price from lowest to highest.

    Args:
        products (list): List of dictionaries with products, where each product has a 'Price' key.

    Returns:
        list: List of products sorted by price in ascending order.
    """
    return sorted(products, key=lambda x: convert_to_number(x['price']))


def sort_by_price_desc(products):
    """
    Sorts a list of products by price from highest to lowest.

    Args:
        products (list): List of dictionaries with products, where each product has a 'Price' key.

    Returns:
        list: List of products sorted by price in descending order.
    """
    return sorted(products, key=lambda x: convert_to_number(x['price']), reverse=True)

def convert_km_to_number(km_str):
    """
    Converts a price string with symbols and dots to a numeric value.
    
    Args:
        price_str (str): Price in string format with symbol and dots.

    Returns:
        int: Price converted to an integer.
    """
    km_str = km_str.replace('Km', '').replace('.', '')  # Removes dollar symbol and dots
    return int(km_str)

def sort_by_km_asc(products):
    """
    Sorts a list of products by km from lowest to highest.

    Args:
        products (list): List of dictionaries with products, where each product has a 'Price' key.

    Returns:
        list: List of products sorted by km in ascending order.
    """
    return sorted(products, key=lambda x: convert_km_to_number(x['KM']))

def sort_by_km_desc(products):
    """
    Sorts a list of products by km from lowest to highest.

    Args:
        products (list): List of dictionaries with products, where each product has a 'Price' key.

    Returns:
        list: List of products sorted by km in ascending order.
    """
    return sorted(products, key=lambda x: convert_km_to_number(x['KM']), reverse=True)



def filter_by_name(products):
    """
    Filters items by the desired item name.

    Args:
        products (list): List of dictionaries with products, where each product has a 'title' key.

    Returns:
        list: List of products that contain the filtered items by name.
    """
    
    desired_item = input('Enter the name of the item you are looking for: ').lower()

    desired_item_list = []

    for product in products:
        if 'title' in product and isinstance(product['title'], str):
            product_name = product['title'].lower()
            if desired_item in product_name:
                desired_item_list.append(product)
        else:
            print(f"Product without a valid title found: {product}")

    print (desired_item_list)    

    option = input("Do you want to filter products by price or kilometers? [P/K/N] \t").upper()
    
    try:
        if option == "P":
            asc_desc = input("Filter by ascending or descending price [A/D] \t").upper()
            if asc_desc == "A":
                desired_item_list = sort_by_price_asc(desired_item_list)
            elif asc_desc == "D":
                desired_item_list = sort_by_price_desc(desired_item_list)
            else:
                print("Invalid input for sorting order.")
        elif option == "K":
            asc_desc = input("Filter by ascending or descending kilometers [A/D] \t").upper()
            if asc_desc == "A":
                desired_item_list = sort_by_km_asc(desired_item_list)
            elif asc_desc == "D":
                desired_item_list = sort_by_km_desc(desired_item_list)
            else:
                print("Invalid input for sorting order.")
        elif option == "N":
            pass  
        else:
            print("Invalid option selected.")
    
    except (ValueError, KeyError) as e:
        print(f"An error occurred: {e}")
    
    return desired_item_list

def return_to_menu():
    input("\nPress any key to return to the menu...")