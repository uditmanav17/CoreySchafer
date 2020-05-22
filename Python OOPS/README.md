<a href="https://colab.research.google.com/github/uditmanav17/CoreySchafer/blob/master/Python OOPS/Python_OOP_Tutorial.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>


```python
from pprint import pprint as pp
```

# Classes and Instances
[//]: # "Disclaimer - This is inspired from [this](https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)."


```python
class Employee:
    pass

emp1 = Employee() # instance 1
emp2 = Employee() # instance 2

print(emp1, emp2, sep='\n') # notice the address of instances

```

    <__main__.Employee object at 0x7efc030d4898>
    <__main__.Employee object at 0x7efc030d4cc0>
    

# Adding attributes variables to instances
Instance variables contains data that is unique to each instances.


```python
emp1.first = 'Udit'
emp1.last = 'Manav'
emp1.mail = "udit.manav@gmail.com"
emp1.pay = 50000

emp2.first = 'Test'
emp2.last = 'User'
emp2.mail = "Test.user@gmail.com"
emp2.pay = 50000

```


```python
print(emp1.__dict__)
print(emp1.mail)
```

    {'first': 'Udit', 'last': 'Manav', 'mail': 'udit.manav@gmail.com', 'pay': 50000}
    udit.manav@gmail.com
    

#  Class Methods \__init__ 
This method behaves as constructor. 


```python
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.mail = f"{first}.{last}@comapny.com"
        self.pay = pay

emp1 = Employee('Udit', 'Manav', 50000)

print(emp1.__dict__)
```

    {'first': 'Udit', 'last': 'Manav', 'mail': 'Udit.Manav@comapny.com', 'pay': 50000}
    

# Adding methods to classes


```python
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.mail = f"{first}.{last}@comapny.com"
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}" 

emp1 = Employee('Udit', 'Manav', 50000)

print(emp1.fullname())
print(Employee.fullname(emp1))
```

    Udit Manav
    Udit Manav
    

# class variables
Variables that are shared among all instances of a class. While instance variables are unique to each class and may have different values for each instance, class variables will be shared among all instances.


```python
class Employee:

    num_emp = 0
    raise_amt = 1.04 # class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.mail = f"{first}.{last}@comapny.com"
        self.pay = pay

        Employee.num_emp += 1 
        # used Employee.num_emp because total num employees should be same
        # for every instance 

    def fullname(self):
        return f"{self.first} {self.last}" 

    def apply_raise(self):
        self.pay = self.pay * self.raise_amt  
        # self.raise_amt can also be replaced with Employee.raise_amt
        # but using self.raise_amt provides us the capability to set different
        # raise_amt for every employee

print(Employee.num_emp)
emp1 = Employee('Udit', 'Manav', 50000)
emp2 = Employee('Test', 'Users', 60000)
print(Employee.num_emp)

print(f"emp1.raise_amt = {emp1.raise_amt}")
print(f"emp2.raise_amt = {emp2.raise_amt}")
print(f"Employee.raise_amt = {Employee.raise_amt}")
# now we check namespace of emp1 and Employee
print("emp1 neamspace:-")
pp(emp1.__dict__) # no raise_amt
print("Employee neamspace:-")
pp(Employee.__dict__)
```

    emp1.raise_amt = 1.04
    emp2.raise_amt = 1.04
    Employee.raise_amt = 1.04
    emp1 neamspace:-
    {'first': 'Udit',
     'last': 'Manav',
     'mail': 'Udit.Manav@comapny.com',
     'pay': 50000}
    Employee neamspace:-
    mappingproxy({'__dict__': <attribute '__dict__' of 'Employee' objects>,
                  '__doc__': None,
                  '__init__': <function Employee.__init__ at 0x7efc031f5158>,
                  '__module__': '__main__',
                  '__weakref__': <attribute '__weakref__' of 'Employee' objects>,
                  'apply_raise': <function Employee.apply_raise at 0x7efc031f5ae8>,
                  'fullname': <function Employee.fullname at 0x7efc031f52f0>,
                  'raise_amt': 1.04})
    

In the above example we can see that emp1's namespace does not contain 'raise_amt' variable. So, it looks for raise_amt in Employee's namespace. 

Now, let's try to modify emp1's raise amount, we'll notice that now raise amount is present in emp1's namespace since it is totally different.


```python
emp1.raise_amt = 1.05
print(f"emp1.raise_amt = {emp1.raise_amt}")
print(f"emp2.raise_amt = {emp2.raise_amt}")
print(f"Employee.raise_amt = {Employee.raise_amt}")
print("updated var using class")
Employee.raise_amt = 1.07
print(f"emp1.raise_amt = {emp1.raise_amt}")
print(f"emp2.raise_amt = {emp2.raise_amt}")
print(f"Employee.raise_amt = {Employee.raise_amt}")
```

    emp1.raise_amt = 1.05
    emp2.raise_amt = 1.06
    Employee.raise_amt = 1.06
    updated var using class
    emp1.raise_amt = 1.05
    emp2.raise_amt = 1.07
    Employee.raise_amt = 1.07
    


```python
print("emp1 neamspace:-")
pp(emp1.__dict__) # no raise_amt
print("Employee neamspace:-")
pp(Employee.__dict__)
```

    emp1 neamspace:-
    {'first': 'Udit',
     'last': 'Manav',
     'mail': 'Udit.Manav@comapny.com',
     'pay': 50000,
     'raise_amt': 1.05}
    Employee neamspace:-
    mappingproxy({'__dict__': <attribute '__dict__' of 'Employee' objects>,
                  '__doc__': None,
                  '__init__': <function Employee.__init__ at 0x7efc031f5158>,
                  '__module__': '__main__',
                  '__weakref__': <attribute '__weakref__' of 'Employee' objects>,
                  'apply_raise': <function Employee.apply_raise at 0x7efc031f5ae8>,
                  'fullname': <function Employee.fullname at 0x7efc031f52f0>,
                  'raise_amt': 1.07})
    

# Part 3- regular vs classmethods vs staticmethods
___Regular___ methods in a class automatically takes instance as the first argument (self). <br>
To change this so that our method takes class as first argument we use ***class*** methods. <br>(Hint: using @classmethod).


```python
class Employee:

    num_emp = 0
    raise_amt = 1.04 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.mail = f"{first}.{last}@comapny.com"
        self.pay = pay

        Employee.num_emp += 1 
        
    def fullname(self):
        return f"{self.first} {self.last}" 

    def apply_raise(self):
        self.pay = self.pay * self.raise_amt  
       
    @classmethod       
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


emp1 = Employee('Udit', 'Manav', 50000)
emp2 = Employee('Test', 'Users', 60000)

print(f"emp1.raise_amt = {emp1.raise_amt}")
print(f"emp2.raise_amt = {emp2.raise_amt}")
print(f"Employee.raise_amt = {Employee.raise_amt}")
Employee.set_raise_amt(1.02) 
# we can also run set_raise_amt class method from instance but that looks odd
print(f"emp1.raise_amt = {emp1.raise_amt}")
print(f"emp2.raise_amt = {emp2.raise_amt}")
print(f"Employee.raise_amt = {Employee.raise_amt}")

```

    0
    emp1.raise_amt = 1.04
    emp2.raise_amt = 1.04
    Employee.raise_amt = 1.04
    emp1.raise_amt = 1.02
    emp2.raise_amt = 1.02
    Employee.raise_amt = 1.02
    

## class methods as alternative constructors
used to provide multiple ways of creating an object. Consider a use case where user wants to create an instance using strings in provided in format "first-last-pay". is htere any way to just pass a string and create an employee object whiout parsing explictly everytime. Now, first let's see what it would look like if we have to parse string everytime.


```python
emp_str1 = 'udit-manav-50000'
emp_1 = Employee(*emp_str1.split('-'))
pp(emp_1.__dict__)
```

    {'first': 'udit',
     'last': 'manav',
     'mail': 'udit.manav@comapny.com',
     'pay': '50000'}
    

To avoid this parsing everytime let's create an alternative constructor using classmethod which can create employee object directly by passing the string.


```python
class Employee:

    num_emp = 0
    raise_amt = 1.04 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.mail = f"{first}.{last}@comapny.com"
        self.pay = pay

        Employee.num_emp += 1 
        
    def fullname(self):
        return f"{self.first} {self.last}" 

    def apply_raise(self):
        self.pay = self.pay * self.raise_amt  
       
    @classmethod       
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

emp_str1 = 'udit-manav-50000'
emp_1 = Employee.from_string(emp_str1)
pp(emp_1.__dict__)
```

    {'first': 'udit',
     'last': 'manav',
     'mail': 'udit.manav@comapny.com',
     'pay': '50000'}
    

Static methods don't have access to the attributes of an instance of a class (like a regular method does), and they don't have access to the attributes of the class itself (like a class method does).

However, they can be useful to group some utility function together with a class - e.g. a simple conversion from one type to another - that doesn't need access to any information apart from the parameters provided (and perhaps some attributes global to the module.)

They could be put outside the class, but grouping them inside the class may make sense where they are only applicable there.

Consider a function for Employee class that would take in a date and returns whether it was a working day or not. It does have some logical connection but doesn't need access to any attribute of the class.


```python
class Employee:

    num_emp = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.mail = f"{first}.{last}@comapny.com"
        self.pay = pay

        Employee.num_emp += 1 
            
    @staticmethod
    def is_workday(day):
        if any([day.weekday() == 5, day.weekday() == 6]): # weekday at saturday/sunday
            return False
        return True

import datetime
my_date = datetime.date.today()
print(Employee.is_workday(my_date))

```

    True
    

# Part 4: Inheritance
Inheritance allows child class to inherit methods and attributes from parent class.  


```python
class Employee:

    raise_amt = 1.04 # class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.mail = f"{first}.{last}@comapny.com"
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}" 

    def apply_raise(self):
        self.pay = self.pay * self.raise_amt  
```

Now, let's create different types of Employees, Developers and Managers.


```python
class Developer(Employee):
    pass

dev1 = Developer('A', 'Z', 100)
dev1 = Developer('B', 'X', 200)

pp(dev1.__dict__)
```

    {'first': 'B', 'last': 'X', 'mail': 'B.X@comapny.com', 'pay': 200}
    

Check out the method resolution order.


```python
print(help(Developer))
```

    Help on class Developer in module __main__:
    
    class Developer(Employee)
     |  Method resolution order:
     |      Developer
     |      Employee
     |      builtins.object
     |  
     |  Methods inherited from Employee:
     |  
     |  __init__(self, first, last, pay)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  apply_raise(self)
     |  
     |  fullname(self)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Employee:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from Employee:
     |  
     |  raise_amt = 1.04
    
    None
    

Now, lets say that, we need some extra attributes (major prog\_language) in developer class, apart from those that were provided in Employee. For this, we need to define \_\_init__ method for of its own.


```python
class Developer(Employee):
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

dev1 = Developer('Udit', 'Manav', 50000, 'Python')
dev2 = Developer('Sparsh', 'Gupta', 60000, 'BrainFuck')
pp(dev1.__dict__)
```

    {'first': 'Udit',
     'last': 'Manav',
     'mail': 'Udit.Manav@comapny.com',
     'pay': 50000,
     'prog_lang': 'Python'}
    


```python
class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        self.employees = [] if not employees else employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            print(f"{self.fullname()} is now supervising {emp.fullname()}")
        else:
            print(f"{self.fullname()} is already supervising {emp.fullname()}")

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            print(f"{self.fullname()} is now NOT supervising {emp.fullname()}")
        else:
            print(f"{self.fullname()} is already NOT supervising {emp.fullname()}")

    def print_emps(self):
        print(f'List of employees {self.fullname()} supervising:-')
        for emp in self.employees:
            print('-->', emp.fullname())

mgr1 = Manager('Shubham', 'Jain', 90000, [dev2])
print(mgr1.mail)
mgr1.print_emps()
mgr1.remove_employee(dev1)
mgr1.add_employee(dev2)
mgr1.add_employee(dev1)
mgr1.print_emps()

```

    Shubham.Jain@comapny.com
    List of employees Shubham Jain supervising:-
    --> Sparsh Gupta
    Shubham Jain is already NOT supervising Udit Manav
    Shubham Jain is already supervising Sparsh Gupta
    Shubham Jain is now supervising Udit Manav
    List of employees Shubham Jain supervising:-
    --> Sparsh Gupta
    --> Udit Manav
    

## isinstance() and issubclass()


```python
print(isinstance(mgr1, Manager))
print(isinstance(mgr1, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Developer, Manager))
```

    True
    True
    True
    True
    False
    

# Part 5: Magic/Dunder Methods
these Methods allows us to emulate some built in behaviour within python nad its also how we implement operator overloading. Now, lets try to print emp1.



```python
 print(emp1)
```

    <__main__.Employee object at 0x7efc0316bdd8>
    

Okay, so that gives us no useful information about what emp1 is, wouldn't it be great if we could get some useful information by printing out Employee object. We can accomplish this using \_\_repr__ & \_\_str__ methods. 

\_\_repr__ is fallback for \_\_str__ method i.e. if \_\_str__ is not implemented then wgile printing it would fallback to \_\_repr__ implementation. Let's have a look.


```python
class Employee:

    raise_amt = 1.04 # class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.mail = f"{first}.{last}@comapny.com"
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}" 

    def apply_raise(self):
        self.pay = self.pay * self.raise_amt 

    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"

    def __str__(self):
        return f"{self.fullname()} - {self.mail}"

dev1 = Employee('Udit', 'Manav', 50000)

print(str(dev1))
print(dev1.__str__())
print(dev1)
print(repr(dev1))
print(dev1.__repr__())
dev1
    
```

    Udit Manav - Udit.Manav@comapny.com
    Udit Manav - Udit.Manav@comapny.com
    Udit Manav - Udit.Manav@comapny.com
    Employee(Udit, Manav, 50000)
    Employee(Udit, Manav, 50000)
    




    Employee(Udit, Manav, 50000)



For more information on dunder methods refer [this](https://docs.python.org/3/reference/datamodel.html#special-method-names).

# Part 6: Property Decorator, Getters and setters


```python
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.mail = f"{first}.{last}@comapny.com"

    def fullname(self):
        return f"{self.first} {self.last}" 

emp1 = Employee('John', 'Smith')

print(emp1.first)
print(emp1.mail)
print(emp1.fullname())
```

    john
    john.Smith@comapny.com
    john Smith
    

Now, lets change the first name of emp1.


```python
emp1.first = 'Jim'
print(emp1.first)
print(emp1.mail)
print(emp1.fullname())
```

    Jim
    john.Smith@comapny.com
    Jim Smith
    


```python
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def fullname(self):
        return f"{self.first} {self.last}" 
    
    @property
    def mail(self):
        return f"{self.first}.{self.last}@comapny.com"

emp1 = Employee('John', 'Smith')

print(emp1.first)
print(emp1.mail)
print(emp1.fullname())
emp1.first = 'Jim'
print(emp1.first)
print(emp1.mail)
print(emp1.fullname())
```

    John
    John.Smith@comapny.com
    John Smith
    Jim
    Jim.Smith@comapny.com
    Jim Smith
    


```python
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def mail(self):
        return f"{self.first}.{self.last}@comapny.com"
    
    @property
    def fullname(self):
        return f"{self.first} {self.last}" 
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('deleting name!')
        self.first = None
        self.last = None
        

emp1 = Employee('John', 'Smith')

emp1.fullname = 'Udit Manav'
print(emp1.first)
print(emp1.mail)
print(emp1.fullname)

del emp1.fullname
print(emp1.first)
print(emp1.mail)
print(emp1.fullname)
```

    Udit
    Udit.Manav@comapny.com
    Udit Manav
    deleting name!
    None
    None.None@comapny.com
    None None
    

# Getter/Setter 
In Python, getters and setters are not the same as those in other object-oriented programming languages. Basically, the main purpose of using getters and setters in object-oriented programs is to ensure data encapsulation. Private variables in python are not actually hidden fields like in other object oriented languages. Getters and Setters in python are often used when:

* We use getters & setters to add validation logic around getting and setting a value.
* To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified by external user.

For more [info](https://www.geeksforgeeks.org/getter-and-setter-in-python/).

## Using normal function to achieve getters and setters behaviour
To achieve getters & setters property, if we define normal get() and set() methods it will not reflect any special implementation. For Example


```python
class Geek: 
    def __init__(self, age = 0): 
         self._age = age 
      
    # getter method 
    def get_age(self): 
        return self._age 
      
    # setter method 
    def set_age(self, x): 
        self._age = x 
  
raj = Geek() 
  
# setting the age using setter 
raj.set_age(21) 
  
# retrieving age using getter 
print(raj.get_age()) 
  
print(raj._age) 
```

    21
    21
    

## Using property() function to achieve getters and setters behaviour

In Python property()is a built-in function that creates and returns a property object. A property object has three methods, getter(), setter(), and delete(). property() function in Python has four arguments property(fget, fset, fdel, doc), fget is a function for retrieving an attribute value. fset is a function for setting an attribute value. fdel is a function for deleting an attribute value. doc creates a docstring for attribute. A property object has three methods, getter(), setter(), and delete() to specify fget, fset and fdel individually. For Example


```python
class Geeks: 
     def __init__(self): 
          self._age = 0
       
     # function to get value of _age 
     def get_age(self): 
         print("getter method called") 
         return self._age 
       
     # function to set value of _age 
     def set_age(self, a): 
         print("setter method called") 
         self._age = a 
  
     # function to delete _age attribute 
     def del_age(self): 
         del self._age 
     
     age = property(get_age, set_age, del_age)  
  
mark = Geeks() 
  
mark.age = 10
print('-----------------')
print(mark.age) 

```

    setter method called
    -----------------
    getter method called
    10
    

## Using @property decorators to achieve getters and setters behaviour

In previous method we used property() function in order to achieve getters and setters behaviour. However as mentioned earlier in this post getters and setters are also used for validating the getting and setting of attributes value. There is one more way to implement property function i.e. by using decorator. Python @property is one of the built-in decorators. The main purpose of any decorator is to change your class methods or attributes in such a way so that the user of your class no need to make any change in their code. For Example


```python
class Geeks: 
     def __init__(self): 
          self._age = 0
       
     # using property decorator 
     # a getter function 
     @property
     def age(self): 
         print("getter method called") 
         return self._age 
       
     # a setter function 
     @age.setter 
     def age(self, a): 
         if(a < 18): 
            raise ValueError("Sorry you age is below eligibility criteria") 
         print("setter method called") 
         self._age = a 
  
mark = Geeks() 
  
mark.age = 19
print('-----------------')
print(mark.age) 
```

    setter method called
    -----------------
    getter method called
    19
    
