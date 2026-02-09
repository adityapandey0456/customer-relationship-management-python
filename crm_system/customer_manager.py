import csv
import json
from customer import Customer
from exceptions import DuplicateCustomerError, ExportError


class CustomerManager:
    def __init__(self):
        self.customers = []  # List of Customer objects

    def add_customer(self, customer):
        # HD Requirement: Duplicate Prevention
        if any(c.get_id() == customer.get_id() for c in self.customers):
            raise DuplicateCustomerError(f"Error: Customer ID {customer.get_id()} already exists.")
        self.customers.append(customer)

    def remove_customer(self, cid):
        initial_len = len(self.customers)
        self.customers = [c for c in self.customers if c.get_id() != cid]
        return len(self.customers) < initial_len

    def filter_by_age_range(self, min_age, max_age):
        return [c for c in self.customers if min_age <= c.calculate_age() <= max_age]

    def filter_by_address(self, city_keyword):
        return [c for c in self.customers if city_keyword.lower() in c.get_address().lower()]

    def export_data(self, format_type='csv'):
        if not self.customers:
            raise ExportError("No customer data available to export.")

        filename = f"crm_export.{format_type}"
        try:
            data = []
            for c in self.customers:
                data.append({
                    "ID": c.get_id(), "Name": c.get_name(), "Email": c.get_email(),
                    "Phone": c.get_phone(), "DOB": c.get_dob(), "Address": c.get_address()
                })

            if format_type == 'json':
                with open(filename, 'w') as f:
                    json.dump(data, f, indent=4)
            else:
                with open(filename, 'w', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=data[0].keys())
                    writer.writeheader()
                    writer.writerows(data)
            return filename
        except Exception as e:
            raise ExportError(f"Failed to export: {str(e)}")