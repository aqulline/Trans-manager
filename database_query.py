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

# x = DataQuery.vehicle_fetch(DataQuery())

# for i, y in x.items():
#    print(i)
#    for k, l in y.items():
#        print(l)
