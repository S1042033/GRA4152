import argparse, textwrap
from P9_23_module import CountryCollection


## Documenting and testing the CountryCollection class using the argparse library
#  It allows users to add multiple countries to a list or a dictionary, and retrieve the country with the 
#  largest area, population, or population density.
#
parser = argparse.ArgumentParser(prog='CountryCollection',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
                                A class to handle multiple countries with methods to find
                                the country with the largest area, the largest population,
                                or the largest population density.
                                ------------------------------------------------------------
                                
                                The class contains both list methods and dictionary methods
                                to handle multiple countries. To use the list methods, add
                                countries using the --add_list argument for every country
                                and specify name, population, and area of the country, 
                                e.g., "--add_list USA 331002651 9833517 --add_list Canada 
                                37590000 9984670 --list_largest_area" to get the largest
                                area using the list method.
                                Similarly for the dictionary methods use --add_dict, e.g., 
                                "--add_dict USA 331002651 9833517 --add_dict Canada 
                                37590000 9984670 --dict_largest_density".
                                
                                '''),
    epilog=textwrap.dedent('''\
                                ------------------------------------------------------------
                                
                                ''')
                )

## Adds new countries to the country list
#  Each country is represented by three arguments: name, population, and area.
#  This argument needs to be repeated for each country you want to add to the list.
#
parser.add_argument("--add_list", nargs=3, action='append', metavar=('name', 'population', 'area'), 
                    help="Add a country to the list with its name, population, and area. Repeat for each country.")

## Adds new countries to the country dictionary
#  Each country is represented by three arguments: name, population, and area.
#  This argument needs to be repeated for each country you want to add to the dictionary.
#
parser.add_argument("--add_dict", nargs=3, action='append', metavar=('name', 'population', 'area'), 
                    help="Add a country to the dictionary with its name, population, and area. Repeat for each country.")

## Add the list arguments
parser.add_argument("--list_largest_area", action="store_true", 
                    help="Display the country with the largest area from the country list.")
parser.add_argument("--list_largest_population", action="store_true", 
                    help="Display the country with the largest population from the country list.")
parser.add_argument("--list_largest_density", action="store_true", 
                    help="Display the country with the largest population density from the country list.")

## Add the dictionary arguments
parser.add_argument("--dict_largest_area", action="store_true", 
                    help="Display the country with the largest area from the country dictionary.")
parser.add_argument("--dict_largest_population", action="store_true", 
                    help="Display the country with the largest population from the country dictionary.")
parser.add_argument("--dict_largest_density", action="store_true", 
                    help="Display the country with the largest population density from the country dictionary.")

args = parser.parse_args()

country_collection = CountryCollection()

## As multiple countries can be added by repeating the add arguments, we need to
#  loop over all countries and add them one by one
if args.add_list:
    for country in args.add_list:
        name, population, area = country
        country_collection.addCountryToList(name, int(population), float(area))

if args.add_dict:
    for country in args.add_dict:
        name, population, area = country
        country_collection.addCountryToDict(name, int(population), float(area))

# List methods
if args.list_largest_area:
    print("The country with the largest area, using the list method, is:", 
          country_collection.list_largest_area())
if args.list_largest_population:
    print("The country with the largest population, using the list method, is:", 
          country_collection.list_largest_population())
if args.list_largest_density:
    print("The country with the largest population density, using the list method, is:", 
          country_collection.list_largest_pop_density())

# Dictionary methods
if args.dict_largest_area:
    print("The country with the largest area, using the dictionary method, is:",
          country_collection.dict_largest_area())
if args.dict_largest_population:
    print("The country with the largest population, using the dictionary method, is:",
          country_collection.dict_largest_population())
if args.dict_largest_density:
    print("The country with the largest population density, using the dictionary method, is:",
          country_collection.dict_largest_pop_density())
