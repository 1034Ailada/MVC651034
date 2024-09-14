import tkinter as tk
from tkinter import messagebox

class CowRegistrationView:
    def __init__(self, controller, root):
        self.controller = controller  # เก็บ reference ไปยัง controller เพื่อเรียกใช้ฟังก์ชันที่ควบคุมการลงทะเบียน
        self.root = root  # เก็บ reference ไปยัง root window ของแอปพลิเคชัน
        self.window = root  # ใช้ root window เป็นหน้าต่างหลัก
        self.create_main_screen()  # เรียกใช้ฟังก์ชันเพื่อสร้างหน้าจอหลัก

    def create_main_screen(self):
        # ลบ widget ที่มีอยู่แล้วในหน้าต่างหลัก
        for widget in self.window.winfo_children():
            widget.destroy()

        # สร้าง label และ entry สำหรับเลือกสีวัว
        self.label = tk.Label(self.window, text="Select Cow Color:")
        self.label.pack(pady=10)

        self.color_var = tk.StringVar()  # ใช้เพื่อเก็บข้อมูลสีที่ผู้ใช้ป้อน
        self.color_entry = tk.Entry(self.window, textvariable=self.color_var)
        self.color_entry.pack(pady=5)

        # สร้างปุ่มสำหรับส่งข้อมูลสี
        self.submit_color_btn = tk.Button(self.window, text="Submit", command=self.submit_color)
        self.submit_color_btn.pack(pady=10)

    def submit_color(self):
        color = self.color_var.get().lower()  # รับข้อมูลสีจาก entry และเปลี่ยนเป็นตัวพิมพ์เล็ก
        if color not in ['white', 'brown', 'pink']:
            messagebox.showerror("Error", "Invalid color. Please choose white, brown, or pink.")  # แสดงข้อผิดพลาดถ้าสีไม่ถูกต้อง
        else:
            self.open_registration_form(color)  # เปิดฟอร์มการลงทะเบียนสำหรับสีที่เลือก

    def open_registration_form(self, color):
        # ลบ widget ที่มีอยู่แล้วในหน้าต่างหลัก
        for widget in self.window.winfo_children():
            widget.destroy()

        # เรียกใช้ฟังก์ชันที่เหมาะสมตามสีวัวที่เลือก
        if color == 'white':
            self.white_cow_form()
        elif color == 'brown':
            self.brown_cow_form()
        elif color == 'pink':
            self.pink_cow_form()

    def white_cow_form(self):
        self.window.title("White Cow Registration")  # ตั้งชื่อหน้าต่างใหม่
        self.create_form_fields({
            "Cow ID": tk.StringVar(),  # ฟิลด์สำหรับรหัสวัว
            "Farm ID": tk.StringVar(),  # ฟิลด์สำหรับรหัสฟาร์ม
            "Age (Years)": tk.IntVar(),  # ฟิลด์สำหรับอายุปี
            "Age (Months)": tk.IntVar()  # ฟิลด์สำหรับอายุเดือน
        }, self.submit_white_cow)  # เรียกใช้ฟังก์ชัน submit_white_cow เมื่อลงทะเบียน

    def submit_white_cow(self):
        data = self.collect_form_data()  # รับข้อมูลจากฟอร์ม
        self.controller.register_white_cow(
            data['Cow ID'],
            data['Farm ID'],
            int(data['Age (Years)']),
            int(data['Age (Months)'])
        )  # เรียกใช้ฟังก์ชัน register_white_cow ของ controller

    def brown_cow_form(self):
        self.window.title("Brown Cow Registration")  # ตั้งชื่อหน้าต่างใหม่
        self.create_form_fields({
            "Cow ID": tk.StringVar(),  # ฟิลด์สำหรับรหัสวัว
            "Farm ID": tk.StringVar(),  # ฟิลด์สำหรับรหัสฟาร์ม
            "Mother Cow ID": tk.StringVar()  # ฟิลด์สำหรับรหัสแม่วัว
        }, self.submit_brown_cow)  # เรียกใช้ฟังก์ชัน submit_brown_cow เมื่อลงทะเบียน

    def submit_brown_cow(self):
        data = self.collect_form_data()  # รับข้อมูลจากฟอร์ม
        self.controller.register_brown_cow(
            data['Cow ID'],
            data['Farm ID'],
            data['Mother Cow ID']
        )  # เรียกใช้ฟังก์ชัน register_brown_cow ของ controller

    def pink_cow_form(self):
        self.window.title("Pink Cow Registration")  # ตั้งชื่อหน้าต่างใหม่
        self.create_form_fields({
            "Cow ID": tk.StringVar(),  # ฟิลด์สำหรับรหัสวัว
            "Farm ID": tk.StringVar(),  # ฟิลด์สำหรับรหัสฟาร์ม
            "Owner's First Name": tk.StringVar(),  # ฟิลด์สำหรับชื่อเจ้าของ
            "Owner's Last Name": tk.StringVar()  # ฟิลด์สำหรับนามสกุลเจ้าของ
        }, self.submit_pink_cow)  # เรียกใช้ฟังก์ชัน submit_pink_cow เมื่อลงทะเบียน

    def submit_pink_cow(self):
        data = self.collect_form_data()  # รับข้อมูลจากฟอร์ม
        self.controller.register_pink_cow(
            data['Cow ID'],
            data['Farm ID'],
            data['Owner\'s First Name'],
            data['Owner\'s Last Name']
        )  # เรียกใช้ฟังก์ชัน register_pink_cow ของ controller

    def create_form_fields(self, fields, submit_command):
        self.form_fields = {}  # ใช้เก็บฟิลด์ของฟอร์ม
        for label_text, var in fields.items():
            tk.Label(self.window, text=label_text).pack(pady=5)  # สร้าง label สำหรับแต่ละฟิลด์
            entry = tk.Entry(self.window, textvariable=var)  # สร้าง entry สำหรับแต่ละฟิลด์
            entry.pack(pady=5)
            self.form_fields[label_text] = var  # เก็บข้อมูลฟิลด์

        # สร้างปุ่มสำหรับส่งข้อมูลฟอร์ม
        tk.Button(self.window, text="Submit", command=submit_command).pack(pady=10)

    def collect_form_data(self):
        # เก็บข้อมูลทั้งหมดจากฟิลด์ในฟอร์ม
        return {label: var.get() for label, var in self.form_fields.items()}

    def display_success(self, farm_data):
        self.window.destroy()  # ปิดหน้าต่างปัจจุบัน
        success_window = tk.Tk()  # สร้างหน้าต่างใหม่สำหรับแสดงข้อมูล
        success_window.title("Farm Information")

        # แสดงข้อมูลฟาร์ม
        if not farm_data:
            tk.Label(success_window, text="No cows registered yet.").pack(pady=10)  # ถ้าไม่มีวัวให้แสดงข้อความ
        else:
            for farm_id, data in farm_data.items():
                color = data['color'].lower()  # รับสีจากชื่อคลาส
                count = len(data['cows'])  # นับจำนวนวัวในฟาร์ม
                tk.Label(success_window, text=f"Farm {farm_id}: {count} {color} cows").pack(pady=5)

        # สร้างปุ่มเพื่อกลับไปยังหน้าจอหลัก
        tk.Button(success_window, text="Back to Main Screen", command=lambda: self.reset_to_main_screen(success_window)).pack(pady=10)

    def display_error(self, message):
        messagebox.showerror("Error", message)  # แสดงกล่องข้อความข้อผิดพลาด

    def reset_to_main_screen(self, window):
        window.destroy()  # ปิดหน้าต่างปัจจุบัน
        self.__init__(self.controller, self.root)  # รีเซ็ตหน้าจอหลักโดยการสร้าง instance ใหม่
