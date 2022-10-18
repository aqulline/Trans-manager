from kivy.properties import NumericProperty, StringProperty
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (1920, 1016)
Window.minimum_width, Window.minimum_height = Window.size


class MainApp(MDApp):
    # App
    size_x, size_y = NumericProperty(0), NumericProperty(0)

    # FLEET
    car_name = StringProperty("")
    car_id = StringProperty("")
    car_year_purchased = StringProperty("")
    car_owner = StringProperty("")
    car_driver = StringProperty("")
    car_status = StringProperty("")

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

    def build(self):
        self.size_x, self.size_y = Window.size
        self.theme_cls.theme_style = "Light"
        self.size_x, self.size_y = Window.size
        self.title = "Transport Officer"


MainApp().run()
