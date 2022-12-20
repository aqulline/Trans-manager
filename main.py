from kivy.properties import NumericProperty, StringProperty, ListProperty
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.toast import toast
from kivymd.uix.card import MDCard

from database import DataBase as DB
from database_query import DataQuery as DQ

Window.size = (1920, 1016)
Window.minimum_width, Window.minimum_height = Window.size


class CarCard(MDCard):
    car_name = StringProperty("")
    status = StringProperty("")
    status_icon = StringProperty("")
    icon_color = ListProperty()

    # checkbox-blank-circle, alert

    def status_selector(self, status):
        if status:
            self.icon_color = 83 / 225, 186 / 225, 115 / 225, 1
            return "checkbox-blank-circle"
        else:
            self.icon_color = 1, 0, 0, .7
            return "alert"


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
    fuel_type1 = StringProperty("")
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

    # !important
    status_counter = False
    total_cars = StringProperty("0")
    cars_on_road = StringProperty("0")
    cars_idle = StringProperty("0")

    counter = NumericProperty(0)

    # screen info vars
    car_name_info = StringProperty("")
    cars_name_inf = StringProperty("")

    # fuel calculation
    car_id_temp = StringProperty("")
    last_km = StringProperty("")
    reading_km = StringProperty("")
    fuel_prices = StringProperty("")
    consumption_per = StringProperty("")
    fuel_issued = StringProperty("")
    amount_f = StringProperty("0")  # calc = fuel_issued * fuel_prices
    travel_km = StringProperty("0")  # calc = reading_km - last_km
    used_fuel = StringProperty("0")  # calc = travel_km / consumption_per

    def on_start(self):
        self.add_item()

    # DATA INPUTS FUNCTIONS
    def v_status(self, instance):
        if not instance.active:
            self.status = "On road"
            self.car_status = self.status
            instance.active = True
        elif instance.active:
            self.status = "Idle"
            self.car_status = self.status
            instance.active = False

    def car_validate(self):
        self.car_register(self.car_name, self.car_id, self.car_manufactured, self.car_purchased, self.car_owner,
                          self.car_driver, self.engine_no, self.engine_capacity, self.fuel_capacity, self.fuel_type,
                          self.chassis_no, self.car_body)

    def car_register(self, name, registration, manufactured_y, purchased_y, current_user,
                     vehicle_driver, engine_no, engine_capacity, fuel_capacity, fuel_type, chassis_no, body_type):

        print(name, registration, manufactured_y, purchased_y, current_user,
              vehicle_driver, engine_no, engine_capacity, fuel_capacity, fuel_type, chassis_no, body_type,
              self.car_status)

        if name != "" and registration != "" and manufactured_y != "" and purchased_y != "" and current_user != "" and \
                vehicle_driver != "" and engine_no != "" and engine_capacity != "" and fuel_capacity != "" \
                and fuel_type != "" and chassis_no != "" and body_type != "":

            DB.car_json(DB(), name, registration, manufactured_y, purchased_y, current_user,
                        vehicle_driver, engine_no, engine_capacity, fuel_capacity, fuel_type, chassis_no, body_type,
                        self.car_status)

        else:
            toast("Please fill all inputs")

            # DATA DISPLAY CAR FUNCTIONS

    def car_fuel_validate(self):
        self.amount_f = str(int(self.fuel_issued) - int(self.fuel_prices))
        self.travel_km = str(int(self.reading_km) - int(self.last_km))
        self.used_fuel = str(int(self.travel_km) - int(self.consumption_per))

        self.car_fuel_register(self.car_id_temp, self.last_km, self.reading_km, self.fuel_prices, self.consumption_per,
                               self.fuel_issued, self.amount_f, self.travel_km, self.used_fuel)

        print(self.car_id_temp, self.last_km, self.reading_km, self.fuel_prices, self.consumption_per,
              self.fuel_issued, self.amount_f, self.travel_km, self.used_fuel)

    def car_fuel_register(self, carId, last_km, reading_km, fuel_price, consumption_per, fuel_issued, amount_f,
                          travel_km, used_fuel):
        if carId != "" and last_km != "" and reading_km != "" and fuel_price != "" and consumption_per != "" and fuel_issued != "" \
                and amount_f != "" and travel_km != "" and used_fuel != "":

            DB.fuel_json(DB(), carId, last_km, reading_km, fuel_price, consumption_per, fuel_issued, amount_f,
                         travel_km, used_fuel)
        else:
            toast("Fix tha shit")

    def realtime_calc_cost(self, inst):
        if inst != "":
            self.amount_f = str(int(self.fuel_prices) * int(inst))
        elif inst == "":
            self.amount_f = "0"

    def realtime_calc_travel(self, inst):
        if inst != "":
            self.amount_f = str(int(self.fuel_prices) * int(inst))
        elif inst == "":
            self.amount_f = "0"

    def realtime_calc_used(self, inst):
        if inst != "":
            self.amount_f = str(int(self.fuel_prices) * int(inst))
        elif inst == "":
            self.amount_f = "0"

    def add_item(self):
        main = DQ.vehicle_fetch(DQ())
        # self.total_cars = str(DQ.number_of_vehicles(DQ()))
        # self.cars_on_road = str(DQ.on_road(DQ()))
        if main:
            for i, y in main.items():
                if self.counter <= 9:
                    self.root.ids.cars.data.append(
                        {
                            "viewclass": "CarCard",
                            "car_name": i,
                            "id": i,
                            "status": "Grounded",
                            "status_icon": "alert"
                        }
                    )
                self.counter = self.counter + 1
        else:
            img = self.root.ids.nodata
            img.source = "components/icons/file-plus.jpg"

    def info_screen(self, instance):
        sm = self.root
        sm.current = "screen_info"
        self.car_name_info = instance.id

    def build(self):
        self.size_x, self.size_y = Window.size
        self.theme_cls.theme_style = "Light"
        self.size_x, self.size_y = Window.size
        self.title = "Transport Officer"


MainApp().run()
