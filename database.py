class DataBase:
    def car_registers(self):
        if True:
            import firebase_admin
            firebase_admin._apps.clear()
            from firebase_admin import credentials, initialize_app, db
            if not firebase_admin._apps:
                cred = credentials.Certificate(
                    "credential/osg-fleet-management-firebase-adminsdk-tssjd-c2bc176130.json")
                initialize_app(cred, {
                    'databaseURL': 'https://osg-fleet-management-default-rtdb.firebaseio.com/'})

            ref = db.reference('Vehicles').child(id).child("vehicle_info")
            ref.set({
                "company_phone": "company",
                "Phone number": "phone",
                "location": "location",
                "quantity": "quantity",
            })


# DataBase.Order(DataBase()) todo
