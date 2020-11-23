#file to create Flight class

class FlightRoute:
    # constructor
    def __init__(self, orig, dest, dept_date, ret_date):
        self.origin = orig
        self.destination = dest
        self.departure_date = dept_date
        self.return_date = ret_date

    # default constructor
    def __init__(self):
        self.origin = ""
        self.destination = ""
        self.departure_date = ""
        self.return_date = ""

# getters
    def getOrigin(self):
        return self.origin

    def getDestination(self):
        return self.destination

    def getDepartureDate(self):
        return self.departure_date

    def getReturnDate(self):
        return self.return_date

# setters
    def setOrigin(self, orig):
        self.origin = orig

    def setDestination(self, dest):
        self.destination = dest

    def setDepartureDate(self, dept_date):
        self.departure_date = dept_date

    def setReturnDate(self, ret_date):
        self.return_date = ret_date

# user inputs
    def setFlightInfo(self):
        # get airport designations
        self.origin = input("Enter 3 letter origin airport: ")
        while(len(origin) != 3):
            origin=input("Only 3 letter airport codes supported, try again: ")
        destination = input("Enter 3 letter destination airport: ")
        while(len(destination) != 3):
            destination=input("Only 3 letter airport codes supported, try again: ")

# str overload
    def __str__(self):
        return "Flight from {} to {} on {} to {}".format(self.origin, self.destination, self.departure_date, self.return_date)
