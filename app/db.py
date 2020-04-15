import pyodbc
from decouple import config
import uuid

class MyDatabase():
    def __init__(self):
        server = config('SQL_SERVER_HOST', cast=str)
        database = config('SQL_SERVER_DATABASE', cast=str)
        username = config('SQL_SERVER_USERNAME', cast=str)
        password = config('SQL_SERVER_PASSWORD', cast=str)

        self.mockdb = {}
        # self.connect(server, database, username, password)

    
    def connect(self, server, database, username, password):
        driver_name = ''
        driver_names = [x for x in pyodbc.drivers() if x.endswith(' for SQL Server')]
        print('Available drivers: ', driver_names)
        if driver_names:
            driver_name = driver_names[0]

        if driver_name:
            conn_str = 'DRIVER={' + driver_name + '};SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password + ';Trusted_Connection=yes;'
            try:
                self.cnxn = pyodbc.connect(conn_str)
            except:
                print('Could not connect using ODBC.')
        else:
            print('(No suitable driver found. Cannot connect.)')


    def save(self, data):
        nf_id = str(uuid.uuid4())
        self.mockdb[nf_id] = data
        
        return nf_id


    def update(self, nf_id, data):
        self.mockdb[nf_id] = data
        return self.mockdb[nf_id]


    def get(self, nf_id):
        if nf_id in self.mockdb:
            return self.mockdb[nf_id]
        return {}


    def delete(self, nf_id):
        if nf_id in self.mockdb:
            del self.mockdb[nf_id]
