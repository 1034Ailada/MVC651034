from models.cow import WhiteCow, BrownCow, PinkCow
from views.view import CowRegistrationView

class CowController:
    def __init__(self, root):
        self.root = root
        self.view = CowRegistrationView(self, root)
        self.farms = {}  

    def create_main_screen(self):
        self.view.create_main_screen()  # Call the method to recreate the main screen

    def register_white_cow(self, cow_id, farm_id, age_years, age_months):
        cow = WhiteCow(cow_id, farm_id, age_years, age_months)
        if not self.validate_cow(cow):
            return
        self.add_cow_to_farm(farm_id, cow)

    def register_brown_cow(self, cow_id, farm_id, mother_id):
        cow = BrownCow(cow_id, farm_id, mother_id)
        if not self.validate_cow(cow):
            return
        if not cow.validate_mother_id():
            self.view.display_error("Invalid mother ID")
            return
        self.add_cow_to_farm(farm_id, cow)

    def register_pink_cow(self, cow_id, farm_id, owner_name, owner_surname):
        cow = PinkCow(cow_id, farm_id, owner_name, owner_surname)
        if not self.validate_cow(cow):
            return
        if not cow.validate_owner_name() or not cow.validate_owner_surname():
            self.view.display_error("Invalid owner information")
            return
        self.add_cow_to_farm(farm_id, cow)

    def validate_cow(self, cow):
        if not cow.validate_cow_id():
            self.view.display_error("Invalid cow ID")
            return False
        if not cow.validate_farm_id():
            self.view.display_error("Invalid farm ID")
            return False
        if isinstance(cow, WhiteCow) and not cow.validate_age():
            self.view.display_error("Invalid age")
            return False
        return True

    def add_cow_to_farm(self, farm_id, cow):
        if farm_id not in self.farms:
            self.farms[farm_id] = {'cows': [], 'color': type(cow).__name__}
        else:
            current_color = self.farms[farm_id]['color']
            if current_color != type(cow).__name__:
                self.view.display_error(f"Farm {farm_id} already has a different type of cow")
                return

        self.farms[farm_id]['cows'].append(cow)
        self.view.display_success(self.farms)  # Show success and farm information