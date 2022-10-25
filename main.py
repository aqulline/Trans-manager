import re

from kivy.properties import NumericProperty, StringProperty
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.toast import toast
from kivymd.uix.textfield import MDTextField

from database import DataBase as DB

Window.size = (1920, 1016)
Window.minimum_width, Window.minimum_height = Window.size


class NumberOnlyField(MDTextField):
    pat = re.compile('[^0-9]')

    def insert_text(self, substring, from_undo=False):

        pat = self.pat

        if "." in self.text:
            s = re.sub(pat, "", substring)

        else:
            s = ".".join([re.sub(pat, "", s) for s in substring.split(".", 1)])

        return super(NumberOnlyField, self).insert_text(s, from_undo=from_undo)


class MainApp(MDApp):
    # App
    size_x, size_y = NumericProperty(0), NumericProperty(0)

    # Dummy

    vars = []

    # FLEET
    car_name = StringProperty("")
    car_id = StringProperty("")
    car_purchased = StringProperty("")
    car_manufactured = StringProperty("")
    car_owner = StringProperty("")
    car_driver = StringProperty("")
    car_type = StringProperty("")
    car_status = StringProperty("")
    status = StringProperty("Idle")
    engine_no = StringProperty("")
    engine_capacity = StringProperty("")
    fuel_capacity = StringProperty("")
    fuel_type = StringProperty("")
    chassis_no = StringProperty("")
    car_body = StringProperty("")

    # MAINTENANCE
    date_reported = StringProperty("")
    reported_issue = StringProperty("")
    maintenance_status = StringProperty("")
    maintenance_cost = StringProperty("")
    total_maintenance = StringProperty("")

    # FUEL-UTILIZATION
    starting_km = StringProperty("")
    ending_km = StringProperty("")
    km_travel = StringProperty("")
    consumption_km = StringProperty("")
    fuel_given = StringProperty("")
    total_given = StringProperty("")
    fuel_used = StringProperty("")
    total_used = StringProperty("")
    fuel_price = StringProperty("")
    fuel_amount = StringProperty("")
    total_amount = StringProperty("")
    fuel_type = StringProperty("")
    petrol_price = StringProperty("")
    diesel_price = StringProperty("")
    total_petrol = StringProperty("")
    total_diesel = StringProperty("")

    # SAFARI
    location_origin = StringProperty("")
    location_destination = StringProperty("")
    date_origin = StringProperty("")
    date_destination = StringProperty("")

    # TRASH
    status_counter = False

    def v_status(self, instance):
        if not instance.active:
            self.status = "On road"
            instance.active = True
        elif instance.active:
            self.status = "Idle"
            instance.active = False

    def car_validate(self):
        self.car_register(self.car_name, self.car_id, self.car_manufactured, self.car_purchased, self.car_owner,
                          self.car_driver, self.engine_no, self.engine_capacity, self.fuel_capacity, self.fuel_type,
                          self.chassis_no, self.car_body)

    def car_register(self, name, registration, manufactured_y, purchased_y, current_user,
                     vehicle_driver, engine_no, engine_capacity, fuel_capacity, fuel_type, chassis_no, body_type):

        print(name, registration, manufactured_y, purchased_y, current_user,
              vehicle_driver, engine_no, engine_capacity, fuel_capacity, fuel_type, chassis_no, body_type)

        if name != "" and registration != "" and manufactured_y != "" and purchased_y != "" and current_user != "" and \
                vehicle_driver != "" and engine_no != "" and engine_capacity != "" and fuel_capacity != "" \
                and fuel_type != "" and chassis_no != "" and body_type != "":

            DB.car_json(DB(), name, registration, manufactured_y, purchased_y, current_user,
                        vehicle_driver, engine_no, engine_capacity, fuel_capacity, fuel_type, chassis_no, body_type)


        else:
            toast("Please fill all inputs")

    def build(self):
        self.size_x, self.size_y = Window.size
        self.theme_cls.theme_style = "Light"
        self.size_x, self.size_y = Window.size
        self.title = "Transport Officer"


MainApp().run()
