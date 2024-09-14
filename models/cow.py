class Cow:
    def __init__(self, cow_id, farm_id):
        self.cow_id = cow_id
        self.farm_id = farm_id

    def validate_cow_id(self):
        return len(self.cow_id) == 8 and self.cow_id[0] != '0'

    def validate_farm_id(self):
        return len(self.farm_id) == 1 and self.farm_id != '0'

class WhiteCow(Cow):
    def __init__(self, cow_id, farm_id, age_years, age_months):
        super().__init__(cow_id, farm_id)
        self.age_years = age_years
        self.age_months = age_months

    def validate_age(self):
        return 0 <= self.age_years <= 10 and 0 <= self.age_months <= 11

class BrownCow(Cow):
    def __init__(self, cow_id, farm_id, mother_id):
        super().__init__(cow_id, farm_id)
        self.mother_id = mother_id

    def validate_mother_id(self):
        return len(self.mother_id) == 8 and self.mother_id[0] != '0'

class PinkCow(Cow):
    def __init__(self, cow_id, farm_id, owner_name, owner_surname):
        super().__init__(cow_id, farm_id)
        self.owner_name = owner_name
        self.owner_surname = owner_surname

    def validate_owner_name(self):
        return len(self.owner_name) <= 8 and self.owner_name.islower()

    def validate_owner_surname(self):
        return len(self.owner_surname) <= 8 and self.owner_surname.islower()
