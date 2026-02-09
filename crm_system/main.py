import tkinter as tk
from tkinter import messagebox, ttk
from customer import Customer
from customer_manager import CustomerManager
from utils import validate_email, validate_date
from exceptions import CRMError


class CRMGui:
    def __init__(self, root):
        self.manager = CustomerManager()
        self.root = root
        self.root.title("NovaTech Solutions - CRM Professional System")
        self.root.geometry("900x700")
        self.root.configure(bg="#f0f2f5")

        self.setup_ui()

    def setup_ui(self):
        # Header
        header = tk.Frame(self.root, bg="#2c3e50", height=80)
        header.pack(fill="x")
        tk.Label(header, text="CRM SYSTEM - DASHBOARD", font=("Helvetica", 18, "bold"), fg="white", bg="#2c3e50").pack(
            pady=20)

        # --- SECTION 1: ADD CUSTOMER ---
        input_frame = tk.LabelFrame(self.root, text=" 👤 Add New Customer ", font=("Arial", 10, "bold"), padx=15,
                                    pady=10)
        input_frame.pack(fill="x", padx=20, pady=10)

        fields = [("ID:", "id"), ("Name:", "name"), ("Email:", "email"),
                  ("Phone:", "phone"), ("DOB (YYYY-MM-DD):", "dob"), ("Address:", "addr")]

        self.entries = {}
        for i, (label_text, key) in enumerate(fields):
            lbl = tk.Label(input_frame, text=label_text)
            lbl.grid(row=i // 3, column=(i % 3) * 2, sticky="e", pady=5)
            entry = tk.Entry(input_frame)
            entry.grid(row=i // 3, column=(i % 3) * 2 + 1, padx=10, pady=5)
            self.entries[key] = entry

        tk.Button(input_frame, text="Add Customer", command=self.add_customer, bg="#27ae60", fg="white",
                  font=("Arial", 9, "bold")).grid(row=2, column=5, sticky="e", padx=10)

        # --- SECTION 2: SEARCH & FILTER (MISSING PART ADDED HERE) ---
        filter_frame = tk.LabelFrame(self.root, text=" 🔍 Search & Filter ", font=("Arial", 10, "bold"), padx=15,
                                     pady=10)
        filter_frame.pack(fill="x", padx=20, pady=5)

        # Address Search
        tk.Label(filter_frame, text="Search Address:").grid(row=0, column=0, padx=5)
        self.search_addr = tk.Entry(filter_frame)
        self.search_addr.grid(row=0, column=1, padx=5)
        tk.Button(filter_frame, text="Search", command=self.filter_address).grid(row=0, column=2, padx=5)

        # Age Filter
        tk.Label(filter_frame, text="Min Age:").grid(row=0, column=3, padx=5)
        self.min_age = tk.Entry(filter_frame, width=5)
        self.min_age.grid(row=0, column=4, padx=5)
        tk.Label(filter_frame, text="Max Age:").grid(row=0, column=5, padx=5)
        self.max_age = tk.Entry(filter_frame, width=5)
        self.max_age.grid(row=0, column=6, padx=5)
        tk.Button(filter_frame, text="Filter Age", command=self.filter_age).grid(row=0, column=7, padx=5)

        tk.Button(filter_frame, text="Reset View", command=self.view_customers, bg="#95a5a6").grid(row=0, column=8,
                                                                                                   padx=20)

        # --- SECTION 3: TABLE ---
        table_frame = tk.Frame(self.root)
        table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.tree = ttk.Treeview(table_frame, columns=("ID", "Name", "Email", "Age", "Address"), show='headings')
        for col in ("ID", "Name", "Email", "Age", "Address"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        self.tree.pack(side="left", fill="both", expand=True)

        scroll = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        scroll.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scroll.set)

        # --- SECTION 4: EXPORT & DELETE ---
        footer = tk.Frame(self.root, pady=10)
        footer.pack()
        tk.Button(footer, text="Export CSV", command=lambda: self.export('csv'), bg="#f39c12", fg="white",
                  width=12).pack(side="left", padx=5)
        tk.Button(footer, text="Export JSON", command=lambda: self.export('json'), bg="#3498db", fg="white",
                  width=12).pack(side="left", padx=5)
        tk.Button(footer, text="Delete Selected ID", command=self.delete_customer, bg="#e74c3c", fg="white",
                  width=15).pack(side="left", padx=5)

    # --- LOGIC FUNCTIONS ---

    def add_customer(self):
        try:
            cid = int(self.entries['id'].get())
            name = self.entries['name'].get()
            email = self.entries['email'].get()
            dob = self.entries['dob'].get()
            addr = self.entries['addr'].get()

            if not validate_email(email): raise CRMError("Invalid Email Format")
            if not validate_date(dob): raise CRMError("Invalid Date (YYYY-MM-DD)")

            new_cust = Customer(cid, name, email, "000", dob, addr)
            self.manager.add_customer(new_cust)
            messagebox.showinfo("Success", "Customer Added Successfully!")
            self.view_customers()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_table(self, customer_list):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for c in customer_list:
            self.tree.insert("", "end",
                             values=(c.get_id(), c.get_name(), c.get_email(), c.calculate_age(), c.get_address()))

    def view_customers(self):
        self.update_table(self.manager.customers)

    def filter_address(self):
        keyword = self.search_addr.get()
        results = self.manager.filter_by_address(keyword)
        self.update_table(results)

    def filter_age(self):
        try:
            low = int(self.min_age.get())
            high = int(self.max_age.get())
            results = self.manager.filter_by_age_range(low, high)
            self.update_table(results)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter numeric values for age.")

    def delete_customer(self):
        try:
            # Entry field se ID le raha hai (ya selection se bhi ho sakta hai)
            cid = int(self.entries['id'].get())
            if self.manager.remove_customer(cid):
                messagebox.showinfo("Deleted", f"ID {cid} removed.")
                self.view_customers()
            else:
                messagebox.showwarning("Not Found", "ID not found.")
        except:
            messagebox.showerror("Error", "Enter ID in the ID input box to delete.")

    def export(self, fmt):
        try:
            fname = self.manager.export_data(fmt)
            messagebox.showinfo("Exported", f"Saved as {fname}")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = CRMGui(root)
    root.mainloop()