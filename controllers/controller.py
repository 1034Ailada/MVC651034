from models.cow import WhiteCow, BrownCow, PinkCow
from views.view import CowRegistrationView

class CowController:
    def __init__(self, root):
        self.root = root  # เก็บข้อมูล root สำหรับการเชื่อมต่อกับ UI
        self.view = CowRegistrationView(self, root)  # สร้าง instance ของ CowRegistrationView สำหรับการจัดการ UI
        self.farms = {}  # ใช้เพื่อเก็บข้อมูลของฟาร์มและวัว

    def create_main_screen(self):
        self.view.create_main_screen()  # เรียกใช้เมธอดใน CowRegistrationView เพื่อสร้างหน้าจอหลักใหม่

    def register_white_cow(self, cow_id, farm_id, age_years, age_months):
        cow = WhiteCow(cow_id, farm_id, age_years, age_months)  # สร้าง WhiteCow object ใหม่
        if not self.validate_cow(cow):
            return  # ถ้าข้อมูลวัวไม่ถูกต้อง ให้หยุดการทำงาน
        self.add_cow_to_farm(farm_id, cow)  # เพิ่มวัวลงในฟาร์ม

    def register_brown_cow(self, cow_id, farm_id, mother_id):
        cow = BrownCow(cow_id, farm_id, mother_id)  # สร้าง BrownCow object ใหม่
        if not self.validate_cow(cow):
            return  # ถ้าข้อมูลวัวไม่ถูกต้อง ให้หยุดการทำงาน
        if not cow.validate_mother_id():
            self.view.display_error("Invalid mother ID")  # แสดงข้อผิดพลาดถ้า mother_id ไม่ถูกต้อง
            return
        self.add_cow_to_farm(farm_id, cow)  # เพิ่มวัวลงในฟาร์ม

    def register_pink_cow(self, cow_id, farm_id, owner_name, owner_surname):
        cow = PinkCow(cow_id, farm_id, owner_name, owner_surname)  # สร้าง PinkCow object ใหม่
        if not self.validate_cow(cow):
            return  # ถ้าข้อมูลวัวไม่ถูกต้อง ให้หยุดการทำงาน
        if not cow.validate_owner_name() or not cow.validate_owner_surname():
            self.view.display_error("Invalid owner information")  # แสดงข้อผิดพลาดถ้าข้อมูลเจ้าของไม่ถูกต้อง
            return
        self.add_cow_to_farm(farm_id, cow)  # เพิ่มวัวลงในฟาร์ม

    def validate_cow(self, cow):
        if not cow.validate_cow_id():
            self.view.display_error("Invalid cow ID")  # แสดงข้อผิดพลาดถ้า cow_id ไม่ถูกต้อง
            return False
        if not cow.validate_farm_id():
            self.view.display_error("Invalid farm ID")  # แสดงข้อผิดพลาดถ้า farm_id ไม่ถูกต้อง
            return False
        if isinstance(cow, WhiteCow) and not cow.validate_age():
            self.view.display_error("Invalid age")  # แสดงข้อผิดพลาดถ้าอายุไม่ถูกต้องสำหรับ WhiteCow
            return False
        return True  # ข้อมูลวัวถูกต้อง

    def add_cow_to_farm(self, farm_id, cow):
        if farm_id not in self.farms:
            # ถ้าฟาร์มยังไม่มีในระบบ ให้สร้าง entry ใหม่
            self.farms[farm_id] = {'cows': [], 'color': type(cow).__name__}
        else:
            # ถ้าฟาร์มมีอยู่แล้ว ตรวจสอบว่าเป็นประเภทเดียวกัน
            current_color = self.farms[farm_id]['color']
            if current_color != type(cow).__name__:
                self.view.display_error(f"Farm {farm_id} already has a different type of cow")  # แสดงข้อผิดพลาดถ้าฟาร์มมีวัวประเภทอื่น
                return

        self.farms[farm_id]['cows'].append(cow)  # เพิ่มวัวลงในรายการวัวของฟาร์ม
        self.view.display_success(self.farms)  # แสดงข้อความสำเร็จและข้อมูลฟาร์ม
