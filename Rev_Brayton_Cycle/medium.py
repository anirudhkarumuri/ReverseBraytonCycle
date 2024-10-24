import os
from sqlite3 import DatabaseError

import numpy as np
from Db_connect import *

class Medium:

    """
    Class to declare fluid values
    """

    def __init__(self, pressure: float, temperature: float):
        """
        Constructor for gas properties
        :param pressure: Initial pressure of fluid at Position 1 ( before compressor )
        :param temperature: Initial temperature of fluid at Position 1
        """
        self.gamma = None
        self.pressure = pressure
        self.temperature = temperature

    def specific_heat_ratio(self):
        """
        Returns the specific heat ratio of the fluid at Position 1
        :return: cp, and gamma values
        """

        df = self.__get_gamma_value_from_db()
        temperature_values = df["Temperature"]
        cp_values = df["Cp"]
        gamma_values = df["gamma"]
        temp = self.temperature
        cp = np.interp(temp, temperature_values, cp_values)
        gamma = np.interp(temp,temperature_values, gamma_values)
        # gamma is specific heat ratio
        self.gamma = gamma
        return cp, gamma

    @staticmethod
    def __get_gamma_value_from_db():
        try:
            db_file_path = 'thermodynamic_properties.db'
            db_conn_instance = DatabaseConnection(db_file_path)
            table_name = 'properties'
            with db_conn_instance as conn:
                query = f"SELECT * from {table_name}"
                df = pd.read_sql(query, conn)
                return df
        except ConnectionError as e:
            print("Connection Error to Database", e)
        except DatabaseError as e:
            print("Database Error:", e)


# # example
# sx = Medium(pressure=220,temperature=305)
# cp, gamma =sx.specific_heat_ratio()
# print(cp, gamma)