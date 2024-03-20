class Song:
    count = 0
    genres = []

    def __init__(self, name, artist, genre) -> None:
        self.name = name
        self.artist = artist
        self.genre = genre
        # self.genres.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str:
            self._name = name

    @property
    def artist(self):
        return self._artist
    
    @artist.setter
    def artist(self, artist):
        if artist:
            self._artist = artist

    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self, genre):
        if genre:
            self._genre = genre


    def add_song_to_count(cls):
        for s in Song.name:
            return cls.count +1

    def add_to_genres(cls):
        for g in Song.genre:
            cls.genres.append(g)
        return set(cls.genres)
    
    def add_to_artists():
        pass

connor1 = Song('Snow', 'Red Hot', 'Rap')
connor2 = Song('Sniff', 'Blues', 'Rap')
connor3 = Song('Stand', 'Jeffy', 'Country')



class Employee: 

    #raise_amount = class variable
    raise_amount = 1.04

    #num_of_eps class variable keeps track of each employee created (see under init)
    num_of_emps = 0


    def __init__(self, first, last, pay) -> None:
        # attributes
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + '@gmail.com'
        self.full_name = first + ' ' + last

    #Reason why we didn't use self is because self would keep emp count unique to the instance whereas using the class Employee will track emp count for each instance in total
        Employee.num_of_emps += 1

# method 
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
# method containing a class variable
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# class method (decorator) that alters the class in some way
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

#this class method (@ is decorator) takes in a string like "connor-burns-70000", removes the '-', and assigns the attributes
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

#Static methods are used when you don't need to access the instance or the class anywhere within the function
#so if not using self or cls use static
    @staticmethod
    def is_workday(day):
        # weekday() assigns days of week to number with 0 == monday and 6 == sunday
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


#this is a dunder method (special method) typically used for debugging. if you print(emp_1) it will no longer print the literal object but rather the newly formatted information
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    
    def __str__(self) -> str:
        return "{} - {}".format(self.fullname(), self.email)

# this will alter the raise_amount class variable which changes the raise amount for all instances as well
Employee.set_raise_amount(1.05)

# uses from_string class method to convert string to 
emp_str_3 = 'joe-shmoe-60000'
new_emp_3 = Employee.from_string(emp_str_3)
print(new_emp_3.email)

# Think of self = emp_1 
# So emp_1.first == self.first
# emp_1 & emp_2 are Instances of the Employee class:
        
emp_1 = Employee('Patrick', 'Star', 20000)
emp_2 = Employee('Sponge', 'Bob', 50000)


# Instance variables contains data that is unique to each instance
emp_1.first = 'Connor'
emp_1.last = 'Burns'
emp_1.email = 'cburns@gmail.com'

# Each of these instances have attributes that are unique to them
# Attributes = data relating to the instance
# first is an attribute of class Employee
# connor is an attribute of instance emp_2

print(emp_1)
print(emp_1.__str__())

print(emp_1.first)
print(emp_2.full_name)
print(emp_2.raise_amount)

emp_2.raise_amount = 1.06
emp_2.apply_raise()
print(emp_2.raise_amount)
print(emp_2.pay)

#__dict__ prints out the attribute details
print(emp_2.__dict__)


# Subclass that inherits from Employee class
class Developer(Employee):
#changing the range_amount in subclass doesnt have effect on Employee instances, it will only effect subclass
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang) -> None:
        #super() inherits the attributes from Employee
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees = None) -> None:
        super().__init__(first, last, pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Travis', 'Barker', 50000, 'Python')
dev_2 = Developer('Dan', 'Hight', 60000, 'Java')

print(dev_1.email)
print(dev_1.prog_lang)

print(dev_2.pay)
dev_2.apply_raise()
print(dev_2.pay)

#help() will show you resolution order and what methods or attributes the subclass inherits from main class
# print(help(Developer))

mngr_1 = Manager('Sue', 'Smith', 90000, [dev_2])
mngr_1.add_employee(dev_1)
mngr_1.print_emps()

# isInstance will tell us if an instance is inherited from a class
print(isinstance(mngr_1, Employee))
#issubClass will tell us if a class is a subclass of another
print(issubclass(Manager, Employee)) #True
print(issubclass(Manager, Developer)) #False






# Dunder = double underscores 
# for ex: dunder init == __init__

#special methods:

#__repr__(self):
# this method represents 