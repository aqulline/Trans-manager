class DataQuery:
    def vehicle_fetch(self):

        import firebase_admin
        firebase_admin._apps.clear()
        from firebase_admin import credentials, initialize_app, db
        if not firebase_admin._apps:
            try:
                cred = credentials.Certificate \
                    ("credential/osg-fleet-management-firebase-adminsdk-tssjd-c2bc176130.json")
                initialize_app(cred, {'databaseURL': 'https://osg-fleet-management-default-rtdb.firebaseio.com/'})
                store = db.reference("Vehicles")
                print("nice")
                stores = store.get()

                return stores

            except:
                return False

    def number_of_vehicles(self):

        return len(self.vehicle_fetch())

    def on_road(self):
        counter = 0
        data = self.vehicle_fetch()
        for i, y in data.items():
            print(i)
            for k, l in y.items():
                stat = l["car_status"]
                if stat == "On road":
                    counter += 1

        return counter

    def fuel_data(self, car_id, year_id, week_no):
        import firebase_admin
        firebase_admin._apps.clear()
        from firebase_admin import credentials, initialize_app, db
        if not firebase_admin._apps:
            try:
                cred = credentials.Certificate \
                    ("credential/osg-fleet-management-firebase-adminsdk-tssjd-c2bc176130.json")
                initialize_app(cred, {'databaseURL': 'https://osg-fleet-management-default-rtdb.firebaseio.com/'})
                data_fuel = db.reference("Vehicles").child(car_id).child("fuel_info").child(year_id).child(week_no)
                print("nice")
                fuel = data_fuel.get()

                return fuel

            except:
                return False


# x = DataQuery.vehicle_fetch(DataQuery())

# z = DataQuery.number_of_vehicles(DataQuery())


# DataQuery.on_road(DataQuery())

x = DataQuery.fuel_data(DataQuery(), "STK 4052", "202212", "w3")
print(x)

for i, y in x.items():
    print(i,y)
