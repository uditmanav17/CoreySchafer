import logging

# Setting up custom Logger
logger = logging.getLogger(__name__)  # create logger
logger.setLevel(logging.INFO)  # set logging level

# create logging formatter
formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
file_handler = logging.FileHandler("employee1.log")  # create fileHandler
file_handler.setFormatter(formatter)  # set formatter to file handler, NOT Logger

logger.addHandler(file_handler)  # add file handler to logger


class Employee1:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info("Created Employee: {} - {}".format(self.fullname, self.email))

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)


emp_1 = Employee1("John", "Smith")
emp_2 = Employee1("Corey", "Schafer")
emp_3 = Employee1("Jane", "Doe")
