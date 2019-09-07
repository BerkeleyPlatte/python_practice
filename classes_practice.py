import re
import datetime
from building import Building
from city import City


class Pizza:
    def __init__(self):
        self.size = ""
        self.crust_type = ""
        self.toppings = []

    def add_toppings(self, topping):
        self.toppings.append(topping)

    def pizza_sentence(self):
        sentence_constructor = ["I", "want", "a",
                                self.size, self.crust_type, "pizza", "with"]
        sentence_constructor.extend(self.toppings)
        sentence_constructor.reverse()
        sentence_constructor.insert(1, "and")
        sentence_constructor.reverse()
        sentence = (" ".join(sentence_constructor))
        sentence_1 = sentence[:-1]
        sentence_2 = sentence_1 + "."
        print(sentence_2)


veggie = Pizza()
veggie.size = "large"
veggie.crust_type = "hand-tossed"
veggie.toppings = ["spinach,", "peppers,", "cucumbers,", "olives,"]
veggie.add_toppings("onion,")
# veggie.pizza_sentence()


nss_building = Building("301 Plus Park Blvd", 5)
nss_building.designer = "Frank Lloyd Wright"
nss_building.purchase("Cohort 33")
nss_building.construct()
# nss_building.solution_sentence()

nss_building = Building("1 place drive", 653)
nss_building.designer = "bob"
nss_building.purchase("fred")
nss_building.construct()
# nss_building.solution_sentence()

nss_building = Building("2 place drive", 142)
nss_building.designer = "frank"
nss_building.purchase("jen")
nss_building.construct()
# nss_building.solution_sentence()

nss_building = Building("3 place drive", 87)
nss_building.designer = "gus"
nss_building.purchase("mel")
nss_building.construct()
# nss_building.solution_sentence()

nss_building = Building("4 place drive", 67)
nss_building.designer = "eve"
nss_building.purchase("jim")
nss_building.construct()
# nss_building.solution_sentence()


class Employee:
    def __init__(self, name):
        self.name = name
        self.job_title = ""
        self.start_date = ""


class Company:
    def __init__(self, name):
        self.name = name
        self.address = ""
        self.industry = ""
        self.employees = list()


tech_company = Company("Tech a Man to Fish")
tech_company.address = "1 Place Drive"
tech_company.industry = "tech"

food_company = Company("Food and Stuff")
food_company.address = "2 Place Drive"
food_company.industry = "food"

emp_1 = Employee("marge")
emp_1.job_title = "boss"
emp_1.start_date = datetime.date.today()

emp_2 = Employee("steve")
emp_2.job_title = "manager"
emp_2.start_date = datetime.date.today()

emp_3 = Employee("joe")
emp_3.job_title = "pa"
emp_3.start_date = datetime.date.today()

emp_4 = Employee("jack")
emp_4.job_title = "grunt"
emp_4.start_date = datetime.date.today()

emp_5 = Employee("ellie")
emp_5.job_title = "queen bee"
emp_5.start_date = datetime.date.today()

tech_company.employees.append(emp_1)
tech_company.employees.append(emp_2)
food_company.employees.append(emp_3)
food_company.employees.append(emp_4)
food_company.employees.append(emp_5)

# print(tech_company.employees, food_company.employees)

# for each in tech_company.employees:
#     print(f"{each.name} is employeed by {tech_company.name}")

# for each in food_company.employees:
#     print(f"{each.name} is employeed by {food_company.name}")

my_house = Building("1706 Mill St", 2)
my_house.construct()
my_house.purchase("me")
# my_house.solution_sentence()

new_city = City()
new_city.name = "Camden"
new_city.mayor = "Some One"
new_city.year = 2019
new_city.add_building(my_house)
for each in new_city.buildings:
    # print(each)
    print("")


class Student:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.age = 0
        self.cohort = 0
        self.__full_name = ""

    @property
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return 0

    @property
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return 0

    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 0

    @property
    def cohort(self):
        try:
            return self.__cohort
        except AttributeError:
            return 0

    @property
    def full_name(self):
        try:
            return self.first_name + " " + self.last_name
        except AttributeError:
            return 0

    @first_name.setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError('only characters Aa-Zz')

    @last_name.setter
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else:
            raise TypeError('only characters Aa-Zz')

    @age.setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError('only characters 0-9')

    @cohort.setter
    def cohort(self, new_cohort):
        if type(new_cohort) is int:
            self.__cohort = new_cohort
        else:
            raise TypeError('only characters 0-9')

    def __str__(self):
        return(
            f"{self.full_name} is {self.age} years old and is in cohort {self.cohort}.")


dude = Student()
dude.first_name = "Some"
dude.last_name = "Guy"
dude.age = 29
dude.cohort = 33
# print(dude)


class Patient:
    def __init__(self, ssn, dob, insurance_num, first_name, last_name, address):
        self.__ssn = ssn
        self.__dob = dob
        self.__insurance_num = insurance_num
        self.full_name = first_name + " " + last_name
        self.address = address

    @property
    def address(self):
        try:
            return self.__address
        except AttributeError:
            return 0

    @property
    def ssn(self):
        try:
            return self.__ssn
        except AttributeError:
            return 0

    @property
    def dob(self):
        try:
            return self.__dob
        except AttributeError:
            return 0

    @property
    def insurance_num(self):
        try:
            return self.__insurance_num
        except AttributeError:
            return 0

    @address.setter
    def address(self, new_address):
        if bool(re.match('\d+\D+', new_address)) is True:
            self.__address = new_address
        else:
            raise TypeError("don't be that guy")

    def __str__(self):
        return f"name: {self.full_name}, address: {self.address}, ssn: {self.ssn}, DoB: {self.dob}, insurance number: {self.insurance_num}"


whale = Patient(1, 2, 3, "Free", "Willy", "1 the ocean")
print(whale)
