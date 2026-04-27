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


# main program (instantiation & testing)

def main():
    # employee objects(part 1)
    print("*** Employee Data ***")
    print(f"{'Name':<15} {'ID Number':<10} {'Department':<15} {'Position'}")
    print("*" * 60)
    
    # load specific data from the table
    # emp1 loaded from full constructor
    emp1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")

    # emp2 loaded from name/id constructor then setters
    emp2 = Employee.from_name_id("Mark Jones", 39119)
    emp2.set_department("IT")
    emp2.set_position("Programmer")
    
    # emp3 loaded from default constructor then setters
    emp3 = Employee.default_employee()
    emp3.set_name("Joy Rogers")
    emp3.set_id_number(81774)
    emp3.set_department("Manufacturing")
    emp3.set_position("Engineer")

    for e in [emp1, emp2, emp3]:
        print(f"{e.get_name():<15} {e.get_id_number():<10} {e.get_department():<15} {e.get_position()}")

    print("\n" + "="*60 + "\n")

    # patient and procedure objects(part 2)
    patient = Patient("John", "Quincy", "Doe", "123 Maple St", "Springfield", "IL", "62704", "555-0199", "Jane Doe", "555-0100")

    proc1 = Procedure("Physical Exam", "2026-04-26", "Dr. Irvine", 250.00)
    proc2 = Procedure("X-ray", "2026-04-26", "Dr. Jamison", 500.00)
    proc3 = Procedure("Blood test", "2026-04-26", "Dr. Smith", 200.00)

    print("*** Patient Record ***")
    print(f"Patient Name: {patient.get_full_name()}")
    print(f"Address:      {patient.get_address()}")
    print(f"Phone:        {patient.get_phone()}")
    print(f"Emergency Contact Info: {patient.get_emergency_contact()}")

    total_charges = 0
    procedures = [proc1, proc2, proc3]
    
    for i, p in enumerate(procedures, 1):
        print(f"\nProcedure #{i}:")
        print(f"  Procedure name: {p.get_name()}")
        print(f"  Date:           {p.get_date()}")
        print(f"  Practitioner:   {p.get_practitioner()}")
        print(f"  Charge:         ${p.get_charge():.2f}")
        total_charges += p.get_charge()

    print(f"\nTotal Charges: ${total_charges:.2f}")


if __name__ == "__main__":
    main()