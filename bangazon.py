class Department(object):
    """Parent class for all departments"""

    def __init__(self):
        self.employees = set()
    
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



#instances and stuff for the HR department
hr_department = HumanResources('Human Resources', 'Meg', 9)
# hr_department.add_policy('E.L.E.', 'Everybody Love Everybody')
# print(hr_department.name)
# print('Department Supervisor: ', hr_department.supervisor)
# print("The number of HR employees: ",hr_department.employee_count)
# print('------------------------\n')
# print("Company Policy: ",hr_department.get_policy())

#instances and stuff for the IT department
it = InformationTechonolgy('Information Technologies', 'Meg', 10)
# print(it.name)
# print('Department Supervisor: ', it.supervisor)
# it.add_program('Really Important Influential Shit', 'It does really cool shit and shit')
# print('--------------------------\n')
# print("The number of peeps employeed in IT: ",it.employee_count)
# print('--------------------------\n')
# print("IT Department Programs: ", it.get_program())
# print('--------------------------\n')

#instance and things for the Marketing department
market = Marketing('Marketing', 'Emily', 5)
# print(market.name)
# print('--------------------------\n')
# print('Department Supervisor: ', market.supervisor)
# market.add_campaign('Selling this Product', 'All the people')
# print('--------------------------\n')
# print("The marketing department's campaigns: ", market.get_campaign())
# print('--------------------------\n')

#instance and things for the Sales department
sales = Sales('Sales', 'James', 8)
# print(sales.name)
# print('--------------------------\n')
# print('Department Supervisor: ', sales.supervisor)
# print('--------------------------\n')
# sales.add_order('SPA', 'Single Page Application')
# print("The sales department's orders: ", sales.get_orders())