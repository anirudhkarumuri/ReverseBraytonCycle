import os
import numpy as np
from Db_connect import *

class Medium:

    """
    Class to declare fluid values
    """

    def __init__(self, initial_pressure: float, initial_temperature: float):
        """
        Constructor for gas properties
        :param initial_pressure: Initial pressure of fluid at Position 1 ( before compressor )
        :param initial_temperature: Initial temperature of fluid at Position 1
        """
        self.gamma = None
        self.initial_pressure = initial_pressure
        self.initial_temperature = initial_temperature

    def specific_heat_ratio(self):
        """
        Returns the specific heat ratio of the fluid at Position 1
        :return:
        """

        df = self.__get_gamma_value_from_db()
        temperature_values = df["Temperature"]
        cp_values = df["Cp"]
        gamma_values = df["gamma"]
        temp = self.initial_temperature
        cp = np.interp(temp, temperature_values, cp_values)
        self.gamma = np.interp(temp,temperature_values, gamma_values)
        # gamma is specific heat ratio
        gamma = 'implement search algo'
        return cp, self.gamma

    @staticmethod
    def __get_gamma_value_from_db():
        try:
            print('thermodynamic_properties.db')
            db_file_path = 'thermodynamic_properties.db'
            db_conn_instance = DatabaseConnection(db_file_path)
            table_name = 'properties'
            with db_conn_instance as conn:
                query = f"SELECT * from {table_name}"
                df = pd.read_sql(query, conn)
                return df
        except ConnectionError as e:
            print("Connection Error to Database")


# example
sx = Medium(initial_pressure=220,initial_temperature=305)
cp, gamma =sx.specific_heat_ratio()
print(cp, gamma)