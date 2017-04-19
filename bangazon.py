import random

class Department(object):
    """Parent class for all departments"""

    def __init__(self):
        self.employees = set()
    
    def add_employee(self, employee):
        self.employees.add(employee)

    def remove_employee(self, employee):
        try:
            self.employees.remove(employee)
        except KeyError:
            return "That person is not an employee"

    def get_employees(self):
        return self.employees 

    @property
    def name(self):
        try:
            return self.__name
        except AttributeError:
            return ""

    @name.setter
    def name(self, val):
        if not isinstance(val, str):
            raise TypeError('Please provide a string value for the department name')

        if val is not "" and len(val) > 1:
            self.__name = val
        else:
            raise ValueError("Please provide a department name")

    @property
    def supervisor(self):

        try:
            return self.__supervisor
        except AttributeError:
            return ""

    @supervisor.setter
    def supervisor(self, val):
        if not isinstance(val, str):
            raise TypeError('Please provide a string value for the supervisor name')

        if val is not "" and len(val) > 2:
            self.__supervisor = val
        else:
            raise ValueError("Please provide a supervisor name")

    @property
    def employee_count(self):
        try:
            return self.__employee_count
        except AttributeError:
            return "" 

    @employee_count.setter
    def employee_count(self, count):
        self.__employee_count = count
       

    def get_budget(self, budget=3000):
        
        try:
            return self.budget
        except AttributeError:
            self.budget = budget
            return self.budget



class HumanResources(Department):
    """Class for representing Human Resources department

    Methods: __init__, add_policy, get_policy, etc.
    """

    def __init__(self, name, supervisor, employee_count):
        super().__init__()
        self.policies = set()
        self.name = name
        self.supervisor = supervisor
        self.employee_count = employee_count


    def add_policy(self, policy_name, policy_text):
        """Adds a policy, as a tuple, to the set of policies

        Arguments:
        policy_name (string)
        policy_text (string)
        """
        self.policies.add((policy_name, policy_text))

    def get_policy(self):
        """Returns the set of policy
        """
        return self.policies
 
    def get_budget(self, budget):
        """Gets the budget from the department
        """

        self.budget = super().get_budget() + 1500
        return self.budget

class InformationTechonolgy(Department):
    """Class for representing IT department

    Methods:__init__, add_program, set_it_supervisor, set_it_employee
    """
    def __init__(self, name, supervisor, employee_count):
        super().__init__()
        self.programs = set()
        self.name = name
        self.supervisor = supervisor
        self.employee_count = employee_count

    def add_program(self, program_name, program_text):
        """Adds a program

        Arguments:
        policy_name (string)
        policy_text (string)
        """
        self.programs.add((program_name, program_text))

    def get_program(self):
        """Returns the name of the program 
        """
        return self.programs

    def get_budget(self, budget):
        """Gets the budget from the department
        """

        self.budget = super().get_budget() + 2000
        return self.budget


class Marketing(Department):
    """Class for representing Marketing department

    Methods: __init__, 
    """
    def __init__(self, name, supervisor, employee_count):
        super().__init__()
        self.campaigns = set()
        self.name = name
        self.supervisor = supervisor
        self.employee_count = employee_count


    def add_campaign(self, campaign_name, campaign_target):
        """Adds a marketing campaign and the campaign's target audience 
        """

        self.campaigns.add((campaign_name, campaign_target))

    def get_campaign(self):
        """Returns the campaigns that the Marketing department is working on
        """

        return self.campaigns

    def get_budget(self, budget):
        """Gets the budget from the department
        """

        self.budget = super().get_budget() + 5400
        return self.budget

class Sales(Department):
    """Class for representing the Sales department

    Methods: __init__, set_sales_supervisor, get_sales_supervisor
    """
    def __init__(self, name, supervisor, employee_count):
        super().__init__()
        self.orders = set()
        self.name = name
        self.supervisor = supervisor
        self.employee_count = employee_count

    def add_order(self, order_name, order_type):
        """Adds an order to a list that sales reps can access
        """

        self.orders.add((order_name, order_type))

    def get_orders(self):
        """Returns the order 
        """

        return self.orders 

    def get_budget(self, budget):
        """Gets the budget from the department
        """

        self.budget = super().get_budget() + 3500
        return self.budget


class Employee:
    """Building an employee

    Methods: eat()
    """
    def __init__(self, first_name, last_name):
        self.first_name = first_name 
        self.last_name = last_name
        self.full_name = first_name + " " + last_name


    def eat(self, food=None, companions=None):
        restaurants = ["Denny's", "Waffle House", "Baja Burrito", "Vui's Vietnamese", "Wendy's"]
        restaurant_of_choice = random.choice(restaurants)
        if food is not None and companions is None:
            print("{} ate {} at the office for lunch...sad".format(self.full_name, food))
        if companions is not None:
            people_list = list()
            for companion in companions:
                people_list.append(companion.first_name)
            lunch_buddies = ', '.join(people_list)
            if food is not None:
                print("{} joined {} for {} at {} for lunch.".format(self.full_name, lunch_buddies, food, restaurant_of_choice))
            else:
                print("{} left with {} to go to lunch.".format(self.full_name, lunch_buddies))
        return restaurant_of_choice

class FullTime:
    """Describes the attributes of full time employee
    """
    def __init__(self):
        self.hours_per_week = 40

class PartTime:
    """Describes the attributes of a part time employee
    """
    def __init__(self):
        self.hours_per_week = 24

class AccessCard:
    """Allows for an access card to be added to departments
    """
    def __init__(self):
        self.access_card = False

class HRPersonnel(Employee, FullTime, AccessCard):
    """builds the class for the HR employees
    """
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        FullTime.__init__(self)
        AccessCard.__init__(self)

        self.access_card = True

class ITPersonnel(Employee, FullTime, AccessCard):
    """Builds the class for the IT employees
    """
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        FullTime.__init__(self)
        AccessCard.__init__(self)

        self.access_card = True

class MarketingPersonnel(Employee, FullTime, AccessCard):
    """Builds the class for the Marketing employee
    """
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        FullTime.__init__(self)
        AccessCard.__init__(self)

class SalesPersonnel(Employee, PartTime, AccessCard):
    """Builds the class for the Sales employees 
    """
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        PartTime.__init__(self)
        AccessCard.__init__(self)




######################################################################################
###############################Printing Out Info######################################
######################################################################################
hr_department = HumanResources('Human Resources', 'Meg', 9)
it = InformationTechonolgy('Information Technologies', 'Meg', 10)
market = Marketing('Marketing', 'Emily', 5)
sales = Sales('Sales', 'James', 8)

#department names
print('------------EXERCISE 1----------')
print(hr_department.name)
print(it.name)
print(market.name)
print(sales.name)

#department budgets
print('------------EXERCISE 2----------')
print("HR BUDGET: ", hr_department.get_budget(500))
print('IT BUDGET: ', it.get_budget(700))
print("MARKETING BUDGET: ", market.get_budget(800))
print("SALES BUDGET: ", sales.get_budget(950))

#instances of the Employee class
print('-----------EXERCISE 3-----------')
e = Employee('Harper', 'Frankstone')
b = Employee('Bob', 'Sagat')
c = Employee('Claire', 'Holt')
d = Employee('David', 'Thomas')
# print(e.full_name)
e.eat('salads', [b, c, d])



#instances and stuff for the HR department
# hr_department.add_policy('E.L.E.', 'Everybody Love Everybody')
# print('Department Supervisor: ', hr_department.supervisor)
# print("The number of HR employees: ",hr_department.employee_count)
# print('------------------------\n')
# print("Company Policy: ",hr_department.get_policy())

#instances and stuff for the IT department
# print('Department Supervisor: ', it.supervisor)
# it.add_program('Really Important Influential Shit', 'It does really cool shit and shit')
# print('--------------------------\n')
# print("The number of peeps employeed in IT: ",it.employee_count)
# print('--------------------------\n')
# print("IT Department Programs: ", it.get_program())
# print('--------------------------\n')

#instance and things for the Marketing department
# print('--------------------------\n')
# print('Department Supervisor: ', market.supervisor)
# market.add_campaign('Selling this Product', 'All the people')
# print('--------------------------\n')
# print("The marketing department's campaigns: ", market.get_campaign())
# print('--------------------------\n')

#instance and things for the Sales department
# print('--------------------------\n')
# print('Department Supervisor: ', sales.supervisor)
# print('--------------------------\n')
# sales.add_order('SPA', 'Single Page Application')
# print("The sales department's orders: ", sales.get_orders())



print('---------------EXERCISE 4-------------')
#Employees with different attributes that are inherited from different classes 
Adam = HRPersonnel('Adam', 'Meyers')
Harper = HRPersonnel('Harper', 'Frankstone')
# print(Adam.full_name)
Sarah = ITPersonnel('Sarah', 'Palin')
Blaise = ITPersonnel('Blaise', 'Roberts')
# print(Sarah.full_name)
Timothy = MarketingPersonnel('Timothy', 'Leary')
Meg = MarketingPersonnel('Meg', 'Ducharme')
# print(Timothy.full_name)
Chantel = SalesPersonnel('Chantel', 'Johnson')
# print(Chantel.full_name)


hr_department.add_employee(Adam)
hr_department.add_employee(Harper)
it.add_employee(Sarah)
it.add_employee(Blaise)
market.add_employee(Timothy)
market.add_employee(Meg)
sales.add_employee(Chantel)

print('-------------EXERCISE 5---------------')
print('Department: ', hr_department.name)
employee_set_hr = hr_department.get_employees()
for each in employee_set_hr:
    print("    ", each.full_name)

print('Department: ', it.name)
employee_set_it = it.get_employees()
for each in employee_set_it:
    print("    ",each.full_name)

print('Department: ', market.name)
employee_set_marketing = market.get_employees()
for each in employee_set_marketing:
    print("    ",each.full_name)

print('Department: ', sales.name)
employee_set_sales = sales.get_employees()
for each in employee_set_sales:
    print("    ",each.full_name)

