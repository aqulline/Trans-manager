class DataBase:

    def car_json(self, name, registration, manufactured_y, purchased_y, current_user,
                 vehicle_driver, engine_no, engine_capacity, fuel_capacity, fuel_type, chassis_no, body_type):
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
            "body_type": body_type
        }

        self.car_registers(data)

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

# DataBase.Order(DataBase()) todo
