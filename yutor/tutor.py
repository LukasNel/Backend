class Tutor:
    def __init__(self, firstName: str, lastName: str, email: str, password: str, hourlyRate: float, rating: float, numRatings: int, availability: list, subjects: list):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.hourlyRate = hourlyRate
        self.rating = rating
        self.numRatings = numRatings
        self.availability = availability
        self.subjects = subjects


    def setFirstName(self, firstName):
        self.firstName = firstName 

    def setLastName(self, lastName):
        self.lastName = lastName
    
    def setEmail(self, email):
        self.email = email

    def setPassword(self, password):
        self.password = password
    
    def setHourlyRate(self, hourlyRate):
        self.hourlyRate = hourlyRate
    
    def setRating(self, rating):
        self.rating = rating
    
    def setNumRatings(self, numRatings):
        self.numRatings = numRatings
    
    def setAvailability(self, availability):
        self.availabality = availability
    
    def setSubjects(self, subjects):
        self.subjects = subjects
    
    def addSubject(self, subject):
        if subject in self.subjects:
            ()
        self.subjects.append(subject)


    def delSubject(self, subject )
