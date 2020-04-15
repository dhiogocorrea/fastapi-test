import pyodbc
from decouple import config


class MyDatabase():
    def __init__(self):
        server = config('SQL_SERVER_HOST', cast=str)
        database = config('SQL_SERVER_DATABASE', cast=str)
        username = config('SQL_SERVER_USERNAME', cast=str)
        password = config('SQL_SERVER_PASSWORD', cast=str)

        driver_name = ''
        driver_names = [x for x in pyodbc.drivers() if x.endswith(' for SQL Server')]
        print('Available drivers: ', driver_names)
        if driver_names:
            driver_name = driver_names[0]

        if driver_name:
            conn_str = 'DRIVER={' + driver_name + '};SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password + ';Trusted_Connection=yes;'
            self.cnxn = pyodbc.connect(conn_str)
        else:
            print('(No suitable driver found. Cannot connect.)')


    def save(self, data):
        pass

    def get(self, nf_id):
        return {}

    def delete(self, nf_id):
        pass
