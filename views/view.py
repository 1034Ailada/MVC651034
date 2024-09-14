import tkinter as tk
from tkinter import messagebox

class CowRegistrationView:
    def __init__(self, controller, root):
        self.controller = controller
        self.root = root
        self.window = root
        self.create_main_screen()

    def create_main_screen(self):
        # Clear existing widgets
        for widget in self.window.winfo_children():
            widget.destroy()

        self.label = tk.Label(self.window, text="Select Cow Color:")
        self.label.pack(pady=10)

        self.color_var = tk.StringVar()
        self.color_entry = tk.Entry(self.window, textvariable=self.color_var)
        self.color_entry.pack(pady=5)

        self.submit_color_btn = tk.Button(self.window, text="Submit", command=self.submit_color)
        self.submit_color_btn.pack(pady=10)

    def submit_color(self):
        color = self.color_var.get().lower()
        if color not in ['white', 'brown', 'pink']:
            messagebox.showerror("Error", "Invalid color. Please choose white, brown, or pink.")
        else:
            self.open_registration_form(color)

    def open_registration_form(self, color):
        # Clear existing widgets
        for widget in self.window.winfo_children():
            widget.destroy()

        if color == 'white':
            self.white_cow_form()
        elif color == 'brown':
            self.brown_cow_form()
        elif color == 'pink':
            self.pink_cow_form()

    def white_cow_form(self):
        self.window.title("White Cow Registration")
        self.create_form_fields({
            "Cow ID": tk.StringVar(),
            "Farm ID": tk.StringVar(),
            "Age (Years)": tk.IntVar(),
            "Age (Months)": tk.IntVar()
        }, self.submit_white_cow)

    def submit_white_cow(self):
        data = self.collect_form_data()
        self.controller.register_white_cow(
            data['Cow ID'],
            data['Farm ID'],
            int(data['Age (Years)']),
            int(data['Age (Months)'])
        )

    def brown_cow_form(self):
        self.window.title("Brown Cow Registration")
        self.create_form_fields({
            "Cow ID": tk.StringVar(),
            "Farm ID": tk.StringVar(),
            "Mother Cow ID": tk.StringVar()
        }, self.submit_brown_cow)

    def submit_brown_cow(self):
        data = self.collect_form_data()
        self.controller.register_brown_cow(
            data['Cow ID'],
            data['Farm ID'],
            data['Mother Cow ID']
        )

    def pink_cow_form(self):
        self.window.title("Pink Cow Registration")
        self.create_form_fields({
            "Cow ID": tk.StringVar(),
            "Farm ID": tk.StringVar(),
            "Owner's First Name": tk.StringVar(),
            "Owner's Last Name": tk.StringVar()
        }, self.submit_pink_cow)

    def submit_pink_cow(self):
        data = self.collect_form_data()
        self.controller.register_pink_cow(
            data['Cow ID'],
            data['Farm ID'],
            data['Owner\'s First Name'],
            data['Owner\'s Last Name']
        )

    def create_form_fields(self, fields, submit_command):
        self.form_fields = {}
        for label_text, var in fields.items():
            tk.Label(self.window, text=label_text).pack(pady=5)
            entry = tk.Entry(self.window, textvariable=var)
            entry.pack(pady=5)
            self.form_fields[label_text] = var
        
        tk.Button(self.window, text="Submit", command=submit_command).pack(pady=10)

    def collect_form_data(self):
        return {label: var.get() for label, var in self.form_fields.items()}

    def display_success(self, farm_data):
        self.window.destroy()  # Close the current window
        success_window = tk.Tk()
        success_window.title("Farm Information")

        # Display farm information
        if not farm_data:
            tk.Label(success_window, text="No cows registered yet.").pack(pady=10)
        else:
            for farm_id, data in farm_data.items():
                color = data['color'].lower()  # Get color from class name
                count = len(data['cows'])
                tk.Label(success_window, text=f"Farm {farm_id}: {count} {color} cows").pack(pady=5)

        tk.Button(success_window, text="Back to Main Screen", command=lambda: self.reset_to_main_screen(success_window)).pack(pady=10)

    def display_error(self, message):
        messagebox.showerror("Error", message)

    def reset_to_main_screen(self, window):
        window.destroy()
        self.__init__(self.controller, self.root)  # Reinitialize the main screen
