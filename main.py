from kivy.properties import NumericProperty, StringProperty, ListProperty
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.toast import toast
from kivymd.uix.card import MDCard

from database import DataBase as DB
from database_query import DataQuery as DQ

import threading

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
    date = StringProperty("")
    months = StringProperty("")
    full_fmt = StringProperty("")
    month_name = StringProperty("")
    week_name = StringProperty("")

    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

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
    starting_km = StringProperty("0")
    ending_km = StringProperty("0")
    km_travel = StringProperty("0")
    consumption_km = StringProperty("0")
    fuel_given = StringProperty("0")
    total_given = StringProperty("0")
    fuel_used = StringProperty("0")
    total_used = StringProperty("0")
    fuel_price = StringProperty("0")
    fuel_amount = StringProperty("0")
    total_amount = StringProperty("0")
    fuel_type = StringProperty("")
    petrol_price = StringProperty("0")
    diesel_price = StringProperty("0")
    total_petrol = StringProperty("0")
    total_diesel = StringProperty("0")
    current_month = StringProperty("")

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
    car_id_temp = StringProperty("0")
    last_km = StringProperty("0")
    reading_km = StringProperty("0")
    fuel_prices = StringProperty("0")
    consumption_per = StringProperty("0")
    fuel_issued = StringProperty("0")
    amount_f = StringProperty("0")  # calc = fuel_issued * fuel_prices
    travel_km = StringProperty("0")  # calc = reading_km - last_km
    used_fuel = StringProperty("0")  # calc = travel_km / consumption_per

    def on_start(self):
        self.load_item()

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
        self.fuel_used = self.used_fuel

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

    def load_fuel(self):
        thread = threading.Thread(target=self.fuel_fill)
        thread.start()

    def mon_clr(self, num):
        for i in range(1, 13):
            if str(i) == num:
                mnth = self.root.ids

                mnth["mon" + str(i)].md_bg_color = 150 / 255, 111 / 255, 51 / 255, 1

                self.months = f"{self.month_names[i - 1]} {DB.date_format(DB())[8]}"
            else:
                mnth = self.root.ids

                mnth["mon" + str(i)].md_bg_color = 1, 1, 1, 1

        week_no = "1"

        self.current_month = num

        self.week_clr(week_no)

    def week_clr(self, num):
        for i in range(1, 5):
            if str(i) == num:
                mnth = self.root.ids

                mnth["week" + str(i)].md_bg_color = 150 / 255, 111 / 255, 51 / 255, 1
            else:
                mnth = self.root.ids

                mnth["week" + str(i)].md_bg_color = 1, 1, 1, 1

        car_id = self.car_id_temp

        year_id = DB.date_format(DB())[8] + self.current_month

        week_no = f"w{num}"

        if week_no == "w1":
            self.week_name = "Week One"
        if week_no == "w2":
            self.week_name = "Week Two"
        if week_no == "w3":
            self.week_name = "Week Three"
        if week_no == "w4":
            self.week_name = "Week Four"

        print(car_id, year_id, week_no)
        self.fuel_info(car_id, year_id, week_no)

    def load_item(self):
        thread = threading.Thread(target=self.add_item)
        thread.start()

    def add_item(self, **kwargs):
        main = DQ.vehicle_fetch(DQ())
        dates = DB.date_format(DB())
        self.date = dates[0]
        self.full_fmt = dates[1]
        self.month_name = dates[2]
        self.week_name = dates[3]
        self.months = dates[6]
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

    def fuel_fill(self, **kwargs):

        month = DB.date_format(DB())[7]

        if month[0] == "0":
            month = month.replace("0", "")

        self.mon_clr(month)
        toast("Refreshed!")

    def fuel_info(self, car_id, year_id, week_no):
        data = DQ.fuel_data(DQ(), car_id, year_id, week_no)
        print(data)
        if data:
            if data == "None":
                self.fuel_issued = "0"
                self.fuel_used = "0"
                self.reading_km = "0"
                self.last_km = "0"
                self.travel_km = "0"
                self.consumption_per = "0"
                self.fuel_prices = "0"
                self.amount_f = "0"
                toast("No data found!")
            else:
                self.fuel_issued = data['fuel_issued']
                self.fuel_used = data['fuel_used']
                self.reading_km = data['reading_km']
                self.last_km = data['last_km']
                self.travel_km = data['travel_km']
                self.consumption_per = data['consumption']
                self.fuel_prices = data['fuel_price']
                self.amount_f = data['amount']
                toast("Present!")
        else:
            print("no.....")
            self.fuel_issued = "0"
            self.fuel_used = "0"
            self.reading_km = "0"
            self.last_km = "0"
            self.travel_km = "0"
            self.consumption_per = "0"
            self.fuel_prices = "0"
            self.amount_f = "0"
            toast("No data found!")

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
