from datetime import date, datetime

class Customer:
    def __init__(self, cid, name, email, phone, dob, address):
        # Encapsulation: Private Attributes (__variable)
        self.__customer_id = cid
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__dob = dob
        self.__address = address

    # Getters
    def get_id(self): return self.__customer_id
    def get_name(self): return self.__name
    def get_email(self): return self.__email
    def get_phone(self): return self.__phone
    def get_dob(self): return self.__dob
    def get_address(self): return self.__address

    # Setters (For HD Marks)
    def set_name(self, name): self.__name = name
    def set_email(self, email): self.__email = email

    def calculate_age(self):
        """Calculates age based on Date of Birth."""
        birth_date = datetime.strptime(self.__dob, '%Y-%m-%d').date()
        today = date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    def __repr__(self):
        return f"[ID: {self.__customer_id}] Name: {self.__name} | Age: {self.calculate_age()} | Email: {self.__email}"