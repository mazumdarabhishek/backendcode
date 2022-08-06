import json

import mysql.connector
from datetime import datetime

class restaurantDbQuery:



    def New_Entry(self,
                  restaurantname=None,fssailicno=None,gstin=None,
                  cgst=None,sgst=None,restaurantphone=None,restaurantemail=None,
                  restaurantaddress=None,restaurantmembershipstatus=None,registrationdate=None):
        try:
            data = (restaurantname,fssailicno,gstin,cgst,sgst,restaurantphone,restaurantemail,restaurantaddress,restaurantmembershipstatus,registrationdate)
            # Establishing connection
            connection = mysql.connector.connect(host='localhost',
                                                 port=3306,
                                                 database='foodapp',
                                                 user='root',
                                                 password='')

            if connection.connection_id:
                print(f"Connection established with ID::{connection.connection_id}")
            else:
                print("Connection not established")

            # creating cursor
            cur = connection.cursor()
            # Getting current datetime
            #now = datetime.now()
            #now = now.strftime("%Y-%m-%d %H:%M:%S")

            # INSERT QUERY
            INSERT_QUERY = ("INSERT INTO foodapp.restaurant_registration"
                            "(restaurantname,fssailicno,gstin,cgst,sgst,restaurantphone,restaurantemail,restaurantaddress,restaurantmembershipstatus,registrationdate)"
                            "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

            cur.execute(INSERT_QUERY, data)
            connection.commit()
            cur.close()
            connection.close()
            return "Data Inserted"

        except Exception as e:
            return e



    def update_entry(self,id_,payload_dict:dict):

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 port=3306,
                                                 database='foodapp',
                                                 user='root',
                                                 password='')

            if connection.connection_id:
                print(f"Connection established with ID:: {connection.connection_id}")
            else:
                print("Connection not established")

            # creating cursor
            cur = connection.cursor()
            FETCH_QUERY = "SELECT * FROM foodapp.restaurant_registration WHERE id = %s"
            cur.execute(FETCH_QUERY,(id_,))
            #print("query executed")
            data = cur.fetchone()
            print(data)
            if data is not None:
                for column in payload_dict.keys():
                    UPDATE_QUERY = "UPDATE foodapp.restaurant_registration SET %s = %s WHERE id = %s " % (column, payload_dict[column], id_)
                    cur.execute(UPDATE_QUERY)
                connection.commit()
                connection.close()
                return "Success"
            else:
                return "id Does not Exists"
        except Exception as e:
            return str(e)

    def remove_entry(self,id_):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 port=3306,
                                                 database='foodapp',
                                                 user='root',
                                                 password='')

            if connection.connection_id:
                print(f"Connection established with ID::{connection.connection_id}")
            else:
                print("Connection not established")


            # creating cursor
            cur = connection.cursor()
            cur.execute("SELECT * FROM foodapp.restaurant_registration WHERE id = %s"%id_)
            if cur.fetchone() is not None:

                DELETE_QUERY = "DELETE FROM foodapp.restaurant_registration WHERE id = %s"%id_
                cur.execute(DELETE_QUERY)
                connection.commit()
                connection.close()
                return "success"
            else:
                connection.close()
                return "id_ does not exists"

        except Exception as e:
            return e


    def fetch_data(self,id_):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 port=3306,
                                                 database='foodapp',
                                                 user='root',
                                                 password='')

            if connection.connection_id:
                print(f"Connection established with ID::{connection.connection_id}")
            else:
                print("Connection not established")

            # creating cursor
            cur = connection.cursor()

            FETCH_QUERY = "SELECT * FROM foodapp.restaurant_registration WHERE id = %s" % id_
            try:
                cur.execute(FETCH_QUERY)

                DATA = cur.fetchone()
                connection.close()
                Data_Dict = {}
                Data_Dict['id'] = DATA[0]
                Data_Dict['restaurantname'] = DATA[1]
                Data_Dict['fssailicno'] = DATA[2]
                Data_Dict['gstin'] = DATA[3]
                Data_Dict['cgst'] = DATA[4]
                Data_Dict['sgst'] = DATA[5]
                Data_Dict['restaurantphone'] = DATA[6]
                Data_Dict['restaurantemail'] = DATA[7]
                Data_Dict['restaurantaddress'] = DATA[8]
                Data_Dict['restaurantmembershipstatus'] = DATA[9]
                Data_Dict['registrationdate'] = DATA[10]
                print("query executed")
                return Data_Dict
            except:
                return "id Does not Exists!"
        except Exception as e:

            return str(e)

    def fetch_all(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 port=3306,
                                                 database='foodapp',
                                                 user='root',
                                                 password='')

            if connection.connection_id:
                print(f"Connection established with ID::{connection.connection_id}")
            else:
                print("Connection not established")

            # creating cursor
            cur = connection.cursor()

            FETCHALL_QUERY = "SELECT * FROM foodapp.restaurant_registration "
            cur.execute(FETCHALL_QUERY)
            DATA = cur.fetchall()
            payload = []
            for t in DATA:
                temp = dict()
                temp['id'] = t[0]
                temp['restaurantname'] = t[1]
                temp['fssailicno'] = t[2]
                temp['gstin'] = t[3]
                temp['cgst'] = t[4]
                temp['sgst'] = t[5]
                temp['restaurantphone'] = t[6]
                temp['restaurantemail'] = t[7]
                temp['restaurantaddress'] = t[8]
                temp['restaurantmembershipstatus'] = t[9]
                temp['registrationdate'] = t[10]
                payload.append(temp)

            connection.close()
            return payload
        except Exception as e:
            return e




