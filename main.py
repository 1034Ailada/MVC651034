import tkinter as tk  # นำเข้าไลบรารี tkinter สำหรับการสร้าง UI
from controllers.controller import CowController  # นำเข้าคลาส CowController จากโมดูล controller

def main():
    root = tk.Tk()  # สร้าง root window ซึ่งเป็นหน้าต่างหลักของแอปพลิเคชัน
    root.geometry("300x150")  # ตั้งค่าขนาดหน้าต่างหลักเป็น 300x150 พิกเซล
    root.title("Cow Registration System")  # ตั้งชื่อหน้าต่างหลักเป็น "Cow Registration System"
    controller = CowController(root)  # สร้าง instance ของ CowController และส่ง root window ให้กับมัน
    root.mainloop()  # เริ่ม loop หลักของ tkinter ซึ่งจะทำให้หน้าต่างหลักทำงานและตอบสนองต่อเหตุการณ์ต่างๆ

if __name__ == "__main__":
    main()  # เรียกใช้ฟังก์ชัน main ถ้าไฟล์นี้ถูกเรียกใช้งานโดยตรง
