import datetime


class DataBase:
    mnth_name = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                 "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    day = ["Mon", "Tue", "Wed", "Thu",
           "Fri", "Sat", "Sun"]

    # data_inputs
    year_id = ""
    week_no = ""
    data_id = ""
    date = ""

    def car_json(self, name, registration, manufactured_y, purchased_y, current_user,
                 vehicle_driver, engine_no, engine_capacity, fuel_capacity, fuel_type, chassis_no, body_type, status):
        data = {
            "car_name": name,
            "car_id": registration,
            "year_manufactured": manufactured_y,
            "year_purchased": purchased_y,
            "car_owner": current_user,
            "car_driver": vehicle_driver,
            "engine_number": engine_no,
            "engine_capacity": engine_capacity,
            "fuel_capacity": fuel_capacity,
            "fuel_type": fuel_type,
            "chassis_no": chassis_no,
            "body_type": body_type,
            "car_status": status
        }

        self.car_registers(data)

    def fuel_json(self, carId, last_km, reading_km, fuel_price, consumption, fuel_issued, amount, travel_km, fuel_used):
        data = {
            "last_km": last_km,
            "reading_km": reading_km,
            "fuel_price": fuel_price,
            "consumption": consumption,
            "fuel_issued": fuel_issued,
            "amount": amount,
            "travel_km": travel_km,
            "fuel_used": fuel_used
        }

        self.car_fuel(carId, data)

    # data model = vehicles.carID.fuel_info.20229.w1,w2,w3,w4
    def car_fuel(self, car_id, data):
        self.index_fill()
        if True:
            import firebase_admin
            firebase_admin._apps.clear()
            from firebase_admin import credentials, initialize_app, db
            if not firebase_admin._apps:
                cred = credentials.Certificate(
                    "credential/osg-fleet-management-firebase-adminsdk-tssjd-c2bc176130.json")
                initialize_app(cred, {
                    'databaseURL': 'https://osg-fleet-management-default-rtdb.firebaseio.com/'})

            ref = db.reference('Vehicles').child(car_id).child("fuel_info").child(self.year_id).child(
                self.week_no)
            ref.set(data)

    # data model = vehicle.carId.vehicleInfo
    def car_registers(self, data):
        if True:
            import firebase_admin
            firebase_admin._apps.clear()
            from firebase_admin import credentials, initialize_app, db
            if not firebase_admin._apps:
                cred = credentials.Certificate(
                    "credential/osg-fleet-management-firebase-adminsdk-tssjd-c2bc176130.json")
                initialize_app(cred, {
                    'databaseURL': 'https://osg-fleet-management-default-rtdb.firebaseio.com/'})

            ref = db.reference('Vehicles').child(data["car_id"]).child("vehicle_info")
            ref.set(data)

    def index_fill(self):
        date = self.get_date()
        year, month, day = date.strip().split("-")
        self.date = date
        self.year_id = year + month
        self.week_no = self.week_number(int(day))

    def date_format(self):
        date = self.get_date()
        year, month, self.day = date.strip().split("-")
        if int(month) >= 10:
            month_update = int(month) - 1
        else:
            month_update = int(month.replace("0", "")) - 1
        month_name = self.mnth_name[month_update]
        self.week_no = self.week_number(int(self.day))
        date_frmt = f"{month_name} {str(self.day)}"
        month_frmt = f"{month_name} {str(year)}"
        full_frmt = f"{self.day}/{month}/{year}"
        week_name = ""
        self.year_id = year + month

        if self.week_no == "w1":
            week_name = "Week One"
        if self.week_no == "w2":
            week_name = "Week Two"
        if self.week_no == "w3":
            week_name = "Week Three"
        if self.week_no == "w4":
            week_name = "Week Four"

        return [date_frmt, full_frmt, month_name, week_name, self.year_id, self.week_no, month_frmt, month, year]

    def week_number(self, date):
        if 1 <= date <= 7:
            return "w1"
        elif 8 <= date <= 14:
            return "w2"
        elif 15 <= date <= 21:
            return "w3"
        elif date >= 22:
            return "w4"

    def get_date(self):
        return str(datetime.datetime.now()).split(" ")[0]


#data = {
#    "car_id": "STK 4052",
#    "price": "25000",
#    "driver": "50000"
#}

#DataBase.car_fuel(DataBase(), "STK 4052", data)
#DataBase.date_format(DataBase())