class Animal:
    """
    The base class for all animals, providing basic attributes and methods common to all animals.

    ...

    Attributes
    ----------
    _name : str
        The name of the animal, not intended to be accessed directly or modified by subclasses.
    _age : int or float
        The age of the animal, not intended to be accessed directly or modified by subclasses.

    Methods
    -------
    greets()
        Abstract method to be implemented by subclasses for animal-specific greetings.
    describe()
        Provides a basic description of the animal including its name and age.
    """

    def __init__(self, name, age):
        """
        Parameters
        ----------
        name : str
            The name of the animal.
        age : int or float
            The age of the animal.
        """
        self._name = name
        self._age = age

    def greets(self):
        """
        Abstract method to be implemented by animal subclasses.

        Raises
        ------
        NotImplementedError
            If the subclass does not implement this method.
        """
        raise NotImplementedError("Please implement this method in a subclass.")
    
    def describe(self):
        """
        Provides a basic description of the animal including its name and age.

        Returns
        -------
        description : str
            A description of the animal.
        """
        return f"This is {self._name}, and it is {self._age} years old."


class Cat(Animal):
    """
    A Cat class that inherits from Animal and represents a cat.
    """

    def __init__(self, name, age):
        """
        Construct a Cat instance using the Animal base class constructor.

        Parameters
        ----------
        name : str
            The name of the cat.
        age : int or float
            The age of the cat.
        """
        super().__init__(name, age)
    
    def greets(self):
        """
        Prints the sound a cat makes.
        """
        print("meow")
    
    def describe(self):
        """
        Provides a description of the cat, extending the base class description.

        Returns
        -------
        description : str
            A description of the cat.
        """
        return super().describe() + "It is a cat."


class Dog(Animal):
    """
    A Dog class that inherits from Animal and represents a dog.
    """

    def __init__(self, name, age):
        """
        Construct a Dog instance using the Animal base class constructor.

        Parameters
        ----------
        name : str
            The name of the dog.
        age : int or float
            The age of the dog.
        """
        super().__init__(name, age)
    
    def greets(self):
        """
        Prints the sound a dog makes.
        """
        print("woof")
    
    def describe(self):
        """
        Provides a description of the dog, extending the base class description.

        Returns
        -------
        description : str
            A description of the dog.
        """
        return super().describe() + "It is a dog."


class BigDog(Dog):
    """
    A BigDog class that inherits from Dog and represents a big dog.
    """

    def __init__(self, name, age):
        """
        Construct a BigDog instance using the Dog class constructor.

        Parameters
        ----------
        name : str
            The name of the big dog.
        age : int or float
            The age of the big dog.
        """
        super().__init__(name, age)
    
    def greets(self):
        """
        Prints the sound a big dog makes, extending the Dog class's method.
        """
        super().greets()
        print("woooof")
    
    def describe(self):
        """
        Provides a description of the big dog, modifying the Dog class's description.

        Returns
        -------
        description : str
            A description of the big dog.
        """
        return super().describe()[:-2] + " and it is big."



# Creating instances of Cat, Dog, and BigDog
cat = Cat("Tom", 4)
dog = Dog("Buddy", 6)
big_dog = BigDog("Lucy", 10)

# Output descriptions and greetings for each animal
print(cat.describe())
cat.greets()

print(dog.describe())
dog.greets()

print(big_dog.describe())
big_dog.greets()
