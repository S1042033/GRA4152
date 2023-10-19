
## A module defining two classes, a class for a single country and a class to handle multiple countries
#
# 

## A Country class with a name, population and area
#
class Country:

    ## Constructs a Country 
    #  @param name the name of the country
    #  @param population the population of the country
    #  @param area the area of the country
    #
    def __init__(self, name, population, area):
        self._name = name
        self._population = population
        self._area = area

    ## Gets the name of the country
    #  @return name of the country
    #
    @property
    def name(self):
        return self._name

    ## Gets the area of the country
    #  @return area of the country
    #
    @property
    def area(self):
        return self._area
    
    ## Gets the population of the country
    #  @return the population of the country
    #
    @property
    def population(self):
        return self._population
    
    ## Gets the population density of the country
    #  @return the population density of the country
    #
    @property
    def popDensity(self):
        return self._population / self._area


## A CountryCollection class that maintains a list and a dictionary of countries.
#  It allows adding countries to both the list and the dictionary and provides methods
#  to retrieve the country with the largest area, population, or population density from both.
#
class CountryCollection:

    ## Constructs a CountryCollection 
    #  Initializes an empty list and an empty dictionary for storing countries.
    #
    def __init__(self):
        self._country_list = []
        self._country_dict = {}

    ## Adds a new Country object to the country list
    #  @param name the name of the country
    #  @param population the population of the country
    #  @param area the area of the country
    #
    def addCountryToList(self, name, population, area):
        new_country = Country(name, population, area)  
        self._country_list.append(new_country)

    ## Adds a new country to the country dictionary
    #  @param name the name of the country
    #  @param population the population of the country
    #  @param area the area of the country
    #
    def addCountryToDict(self, name, population, area):
        new_country = {
            "population": population,
            "area": area
        }
        self._country_dict[name] = new_country

    ## Retrieves the country with the largest area from the country list
    #  @return the Country name with the largest area or None if the list is empty
    #
    def list_largest_area(self):
        if not self._country_list:
            print("The country list is empty.")
            return

        # By specifying a lambda function in the key of the max function, we can
        # maximize over the area of all countries but return the respective country object
        largest_country = max(self._country_list, key=lambda i: i.area)
                
        return largest_country.name

    ## Retrieves the country with the largest population from the country list
    #  @return the Country name with the largest population or None if the list is empty
    #
    def list_largest_population(self):
        if not self._country_list:
            print("The country list is empty.")
            return
        
        # By specifying a lambda function in the key of the max function, we can
        # maximize over the population of all countries but return the respective country object
        largest_country = max(self._country_list, key=lambda i: i.population)
                
        return largest_country.name
    
    ## Retrieves the country with the largest population density from the country list
    #  @return the Country name with the largest population density or None if the list is empty
    #
    def list_largest_pop_density(self):
        if not self._country_list:
            print("The country list is empty.")
            return
        
        # By specifying a lambda function in the key of the max function, we can
        # maximize over the population density of all countries but return the respective country object
        largest_country = max(self._country_list, key=lambda i: i.popDensity)
                
        return largest_country.name
    
    ## Retrieves the country with the largest area from the country dictionary
    #  @return the name for the country with the largest area or None if the dictionary is empty
    #
    def dict_largest_area(self):
        if not self._country_dict:
            print("The country list is empty.")
            return

        # By passing a lambda function to the key parameter of the max function, we can maximize 
        # over the areas but return the tuple from .items() corresponding to the country with the largest area
        largest_country = max(self._country_dict.items(), key=lambda i: i[1]["area"])
                
        return largest_country[0] # Return just the country name

    ## Retrieves the country with the largest population from the country dictionary
    #  @return the name for the country with the largest population or None if the dictionary is empty
    #
    def dict_largest_population(self):
        if not self._country_dict:
            print("The country list is empty.")
            return
        
        # By passing a lambda function to the key parameter of the max function, we can maximize 
        # over the populations but return the tuple from .items() corresponding to the country with the largest area
        largest_country = max(self._country_dict.items(), key=lambda i: i[1]["population"])
                
        return largest_country[0] # Return just the country name
        
    ## Retrieves the country with the largest population density from the country dictionary
    #  @return the name for the country with the largest population density or None if the dictionary is empty
    #
    def dict_largest_pop_density(self):
        if not self._country_dict:
            print("The country list is empty.")
            return
        
        # By passing a lambda function to the key parameter of the max function, we can maximize 
        # over the population densities but return the tuple from .items() corresponding to the country with the largest area
        largest_country = max(self._country_dict.items(), key=lambda i: i[1]["population"]/i[1]["area"])
                
        return largest_country[0] # Return just the country name


## A simple test of the Country class
#
if __name__ == "__main__":
    norway = Country("Norway", 5408000, 385207)
    print("The name of the country is: ", norway.name)
    print("Expected: Norway")
    print("The population of the country is: ", norway.population)
    print("Expected: 5408000")
    print("The area of the country is: ", norway.area)
    print("Expected: 385207")
    print("The population density of the country is: ", norway.popDensity)
    print(f"Expected: {5408000/385207}")