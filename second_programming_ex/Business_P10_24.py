import datetime as dt

class Appointment:
    """
    A class used to represent a generic Appointment.
    
    Attributes
    ----------
    _description : str
        A description for the appointment.
    _timestamp : datetime
        The date and time when the appointment was created, ignoring microseconds.
    _type : str
        The type of the appointment, defaulting to "Generic".
    _strspecified_time : str or None
        A string representing the specified time for the appointment, defaulting to None.

    Methods
    -------
    occursOn(year, month, day)
        Abstract method to check if the appointment occurs on a given date.
    getDescription()
        Return the description of the appointment.
    getTimeStamp()
        Return the creation timestamp of the appointment.
    save(file_name)
        Save the appointment to a file.
    load(text_line)
        Load the appointment details from a text line.
    """

    def __init__(self, description):
        """
        Parameters
        ----------
        description : str
            The description of the appointment.
        """
        self._description = description
        self._timestamp = dt.datetime.now().replace(microsecond=0)
        self._type = "Generic"
        self._strspecified_time = None
    
    def occursOn(self, day, month, year):
        """
        Check if the appointment occurs on the specified year, month, and day.

        Parameters
        ----------
        day : int
            The day to check.
        month : int
            The month to check.
        year : int
            The year to check.

        Raises
        ------
        NotImplementedError
            If the method is not implemented in a subclass.
        """
        raise NotImplementedError("Please implement this in a subclass.")
    
    def getDescription(self):
        """
        Return the description of the appointment.

        """
        return self._description
    
    def getTimeStamp(self):
        """
        Return the creation timestamp of the appointment.

        """
        return self._timestamp
    
    def save(self, file_name):
        """
        Save the appointment to a file in a specified format.

        This method appends the appointment information to the given file. If a specified time
        is set for the appointment, it is included in the saved data; otherwise, only the 
        timestamp and description are saved.

        Parameters
        ----------
        file_name : str
            The name of the file where the appointment will be saved.

        Notes
        -----
        The appointment is saved in the following format:
        If specified_time is set:
            [timestamp] | [type] appointment: '[description]' at [specified_time]
        If specified_time is not set:
            [timestamp] | [type] appointment: '[description]'
        Each appointment entry is written on a new line.
        """
        with open(file_name, "a+") as file:
            if self._strspecified_time:
                file.write(f"{self._timestamp} | {self._type} appointment: '{self.getDescription()}' at " + self._strspecified_time + "\n")
            else:
                file.write(f"{self._timestamp} | {self._type} appointment: '{self.getDescription()}'\n")
        
    def load(self, text_line):
        """
        This method sets the object's timestamp attribute to the timestamp found in the text_line.

        Parameters
        ----------
        text_line : str
            A line of text containing the appointment details with an ISO format timestamp at the start.

        """
        timestamp = dt.datetime.fromisoformat(text_line[:text_line.find(" | ")])
        self._timestamp = timestamp


class OneTime(Appointment):
    """
    A class used to represent a one-time appointment, inheriting from Appointment.

    Attributes
    ----------
    _day : int
        The day of the month on which the one-time appointment occurs.
    _month : int
        The month of the year on which the one-time appointment occurs.
    _year : int
        The year on which the one-time appointment occurs.
    _type : str
        The type of appointment, which is "One time".
    _strspecified_time : str or None
        A string representing the specified time for the appointment, which for a OneTime appointment is "year-month-day".

    Methods
    -------
    __repr__()
        An override of the built-in function for returning a string representation of an object.
    occursOn(day, month, year)
        Check if the one-time appointment occurs on the specified date.
    """

    def __init__(self, description, day, month, year):
        """
        Parameters
        ----------
        description : str
            The description of the one-time appointment.
        day : int
            The day of the month for the appointment.
        month : int
            The month of the year for the appointment.
        year : int
            The year for the appointment.
        """
        super().__init__(description)
        self._day = day
        self._month = month
        self._year = year
        self._type = "One time"
        self._strspecified_time = f"{self._year}-{self._month}-{self._day}"
    
    def __repr__(self):
        """
        Compute the "official" string representation of the OneTime appointment object.

        Returns
        -------
        repr : str
            The string representation of the one-time appointment with the date and description.
        """
        strmonth = dt.date(1900, self._month, 1).strftime('%B')  # To get the string representation of the month
        return f"One time appointment {self._day} {strmonth} {self._year} '{super().getDescription()}'"
    
    def occursOn(self, day, month, year):
        """
        Check if the one-time appointment occurs on the specified date.

        Parameters
        ----------
        day : int
            The day of the month to check.
        month : int
            The month of the year to check.
        year : int
            The year to check.

        Returns
        -------
        occurs : bool
            True if the appointment occurs on the given date, False otherwise.
        """
        return self._year == year and self._month == month and self._day == day
        

class Daily(Appointment):
    """
    A class used to represent an appointment that occurs daily, inheriting from Appointment.

    Attributes
    ----------
    _type : str
        The type of appointment, which is "Daily".

    Methods
    -------
    __repr__()
        An override of the built-in function for returning a string representation of an object.
    occursOn(day, month, year)
        Check if the daily appointment occurs on the specified date (always true for daily appointments).
    """

    def __init__(self, description):
        """
        Initialize a Daily appointment with a description.

        Parameters
        ----------
        description : str
            The description of the daily appointment.
        """
        super().__init__(description)
        self._type = "Daily"
        
    
    def __repr__(self):
        """
        Compute the "official" string representation of the Daily appointment object.

        Returns
        -------
        repr : str
            The string representation of the daily appointment with the start date and description.
        """
        day      = super().getTimeStamp().day
        strmonth = super().getTimeStamp().strftime('%B')  # To get the string representation of the month
        year     = super().getTimeStamp().year
        return f"Daily appointment starting {day} {strmonth} {year} '{super().getDescription()}'"
        
    def occursOn(self, day, month, year):
        """
        Check if the daily appointment occurs on the specified date.

        This method always returns True for Daily appointments, as they occur every day.

        Parameters
        ----------
        day : int
            The day of the month to check (ignored for Daily appointments).
        month : int
            The month of the year to check (ignored for Daily appointments).
        year : int
            The year to check (ignored for Daily appointments).

        Returns
        -------
        occurs : bool
            Always True for daily appointments.
        """
        return True


class Monthly(Appointment):
    """
    A class used to represent an appointment that occurs monthly, inheriting from Appointment.
    ...

    Attributes
    ----------
    _day : int
        The day of the month on which the monthly appointment occurs.
    _type : str
        The type of appointment, which is "Monthly".
    _strspecified_time : str or None
        A string representing the specified time for the appointment, which for a Monthly appointment is "[self._day] of every month".

    Methods
    -------
    __repr__()
        An override of the built-in function for returning a string representation of an object.
    occursOn(day, month, year)
        Check if the monthly appointment occurs on the specified date.
    """

    def __init__(self, description, day):
        """
        Initialize a Monthly appointment with a description and day.

        Parameters
        ----------
        description : str
            The description of the monthly appointment.
        day : int
            The day of the month for the appointment.
        """
        super().__init__(description)
        self._day = day
        self._type = "Monthly"
        self._strspecified_time = f"{self._day} of every month"
    
    def __repr__(self):
        """
        Compute the "official" string representation of the Monthly appointment object.

        Returns
        -------
        repr : str
            The string representation of the monthly appointment with the start date and description.
        """
        cur_day   = super().getTimeStamp().day
        cur_month = super().getTimeStamp().month
        year      = super().getTimeStamp().year

        # If appointment day is less than the current day, the appointment will start next month
        if self._day <= cur_day:
            # Calculate the next month for the appointment to start
            next_month = cur_month % 12 + 1
            year      += cur_month // 12
            strmonth   = dt.datetime(year, next_month, 1).strftime('%B')
        else:
            strmonth = super().getTimeStamp().strftime('%B')
            
        return f"Monthly appointment starting {self._day} {strmonth} {year} '{super().getDescription()}'"
    
    def occursOn(self, day, month, year):
        """
        Check if the monthly appointment occurs on the specified date.

        Parameters
        ----------
        day : int
            The day of the month to check.
        month : int
            The month of the year to check (ignored for Monthly appointments).
        year : int
            The year to check (ignored for Monthly appointments).

        Returns
        -------
        occurs : bool
            True if the appointment occurs on the given day of any month, False otherwise.
        """
        return self._day == day
        
