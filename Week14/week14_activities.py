# problem 1
class Employee:
    # default arguments to handle constructor requirements
    def __init__(self, name="", idNumber=0, department="", position=""):
        self.__name = name
        self.__idNumber = idNumber
        self.__department = department
        self.__position = position

    # alternative constructor (name + id only)
    @classmethod
    def from_name_id(cls, name, idNumber):
        return cls(name, idNumber)

    # default constructor
    @classmethod
    def default_employee(cls):
        return cls()

    # setters
    def set_name(self, name): self.__name = name
    def set_id_number(self, id_num): self.__idNumber = id_num
    def set_department(self, dept): self.__department = dept
    def set_position(self, pos): self.__position = pos

    # getters
    def get_name(self): return self.__name
    def get_id_number(self): return self.__idNumber
    def get_department(self): return self.__department
    def get_position(self): return self.__position

# inheritance
class ProductionWorker(Employee):
    # constructor extending Employee with shift and pay rate
    def __init__(self, name, idNumber, department, position, shift=1, pay_rate=0.0):
        # call the superclass constructor
        super().__init__(name, idNumber, department, position)
        # shift: 1 for day, 2 for night
        self.__shift = shift
        self.__pay_rate = pay_rate

    # setters
    def set_shift(self, shift): self.__shift = shift
    def set_pay_rate(self, rate): self.__pay_rate = rate

    # getters
    def get_shift(self): return self.__shift
    def get_pay_rate(self): return self.__pay_rate

    # new method
    def get_shift_name(self):
        if self.__shift == 1:
            return "Day"
        elif self.__shift == 2:
            return "Night"
        else:
            return "Invalid Shift"

    # overriding a method from the base class
    # overriding get_position to include the shift information
    def get_position(self):
        base_pos = super().get_position()
        return f"{base_pos} ({self.get_shift_name()} Shift)"

# problem 2
class Patient:
    # constructor accepts an argument for each member variable
    def __init__(self, first, middle, last, addr, city, state, zip_code, phone, em_name, em_phone):
        self.__first = first
        self.__middle = middle
        self.__last = last
        self.__address = addr
        self.__city = city
        self.__state = state
        self.__zip = zip_code
        self.__phone = phone
        self.__em_name = em_name
        self.__em_phone = em_phone

    # setters
    def set_first(self, first): self.__first = first
    def set_middle(self, middle): self.__middle = middle
    def set_last(self, last): self.__last = last
    def set_address(self, addr): self.__address = addr
    def set_city(self, city): self.__city = city
    def set_state(self, state): self.__state = state
    def set_zip(self, zip_code): self.__zip = zip_code
    def set_phone(self, phone): self.__phone = phone
    def set_emergency_name(self, name): self.__em_name = name
    def set_emergency_phone(self, phone): self.__em_phone = phone

    # getters
    def get_full_name(self): return f"{self.__first} {self.__middle} {self.__last}"
    def get_address(self): return f"{self.__address}, {self.__city}, {self.__state} {self.__zip}"
    def get_phone(self): return self.__phone
    def get_emergency_contact(self): return f"{self.__em_name} ({self.__em_phone})"


class Procedure:
    # constructor accepts an argument for each member variable
    def __init__(self, name, date, practitioner, charge):
        self.__name = name
        self.__date = date
        self.__practitioner = practitioner
        self.__charge = charge

    # setters
    def set_name(self, name): self.__name = name
    def set_date(self, date): self.__date = date
    def set_practitioner(self, practitioner): self.__practitioner = practitioner
    def set_charge(self, charge): self.__charge = charge

    # getters
    def get_name(self): return self.__name
    def get_date(self): return self.__date
    def get_practitioner(self): return self.__practitioner
    def get_charge(self): return self.__charge

def main():
    # demonstration of inherited class
    print("*** Production Worker Data ***")
    print(f"{'Name':<15} {'ID Number':<10} {'Department':<15} {'Position':<25} {'Rate'}")
    print("*" * 85)
    
    # instantiating the inherited class and adding data
    worker1 = ProductionWorker("Alice Smith", 55432, "Assembly", "Technician", 1, 22.50)
    worker2 = ProductionWorker("Bob Brown", 66123, "Shipping", "Operator", 2, 25.00)

    for w in [worker1, worker2]:
        # displaying data using class methods
        # overide method can be seen by looking at differences in tables, new method is used in override method
        print(f"{w.get_name():<15} {w.get_id_number():<10} {w.get_department():<15} {w.get_position():<25} ${w.get_pay_rate():.2f}")

    print("\n" + "="*85 + "\n")

    # original employee objects to show nothing broke
    print("*** Original Employee Data ***")
    print(f"{'Name':<15} {'ID Number':<10} {'Department':<15} {'Position'}")
    print("*" * 60)
    
    emp1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    emp2 = Employee.from_name_id("Mark Jones", 39119)
    emp2.set_department("IT")
    emp2.set_position("Programmer")
    
    emp3 = Employee.default_employee()
    emp3.set_name("Joy Rogers")
    emp3.set_id_number(81774)
    emp3.set_department("Manufacturing")
    emp3.set_position("Engineer")

    for e in [emp1, emp2, emp3]:
        print(f"{e.get_name():<15} {e.get_id_number():<10} {e.get_department():<15} {e.get_position()}")

if __name__ == "__main__":
    main()