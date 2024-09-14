class Cow:
    def __init__(self, cow_id, farm_id):
        self.cow_id = cow_id  # เก็บรหัสวัว
        self.farm_id = farm_id  # เก็บรหัสฟาร์ม

    def validate_cow_id(self):
        # ตรวจสอบว่ารหัสวัวมีความยาว 8 ตัวอักษรและตัวแรกไม่ใช่ '0'
        return len(self.cow_id) == 8 and self.cow_id[0] != '0'

    def validate_farm_id(self):
        # ตรวจสอบว่ารหัสฟาร์มมีความยาว 1 ตัวอักษรและไม่ใช่ '0'
        return len(self.farm_id) == 1 and self.farm_id != '0'

class WhiteCow(Cow):
    def __init__(self, cow_id, farm_id, age_years, age_months):
        super().__init__(cow_id, farm_id)  # เรียกใช้ constructor ของ Cow เพื่อกำหนด cow_id และ farm_id
        self.age_years = age_years  # เก็บอายุปีของวัว
        self.age_months = age_months  # เก็บอายุเดือนของวัว

    def validate_age(self):
        # ตรวจสอบว่าอายุปีอยู่ระหว่าง 0 ถึง 10 และอายุเดือนอยู่ระหว่าง 0 ถึง 11
        return 0 <= self.age_years <= 10 and 0 <= self.age_months <= 11

class BrownCow(Cow):
    def __init__(self, cow_id, farm_id, mother_id):
        super().__init__(cow_id, farm_id)  # เรียกใช้ constructor ของ Cow เพื่อกำหนด cow_id และ farm_id
        self.mother_id = mother_id  # เก็บรหัสแม่ของวัว

    def validate_mother_id(self):
        # ตรวจสอบว่ารหัสแม่มีความยาว 8 ตัวอักษรและตัวแรกไม่ใช่ '0'
        return len(self.mother_id) == 8 and self.mother_id[0] != '0'

class PinkCow(Cow):
    def __init__(self, cow_id, farm_id, owner_name, owner_surname):
        super().__init__(cow_id, farm_id)  # เรียกใช้ constructor ของ Cow เพื่อกำหนด cow_id และ farm_id
        self.owner_name = owner_name  # เก็บชื่อเจ้าของวัว
        self.owner_surname = owner_surname  # เก็บนามสกุลเจ้าของวัว

    def validate_owner_name(self):
        # ตรวจสอบว่าชื่อเจ้าของมีความยาวไม่เกิน 8 ตัวอักษรและเป็นตัวพิมพ์เล็ก
        return len(self.owner_name) <= 8 and self.owner_name.islower()

    def validate_owner_surname(self):
        # ตรวจสอบว่านามสกุลเจ้าของมีความยาวไม่เกิน 8 ตัวอักษรและเป็นตัวพิมพ์เล็ก
        return len(self.owner_surname) <= 8 and self.owner_surname.islower()
