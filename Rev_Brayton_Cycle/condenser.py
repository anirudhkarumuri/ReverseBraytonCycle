class Condenser:
    """
    Class handling pressure and temperature values
    """

    def __init__(self, p2_pressure, t2_temp, heat_rejection_efficiency, ambient_temp):
        """

        :param p2_pressure: pressure of the gas at point 2 ( after compression )
        :param t2_temp: temperature of the gas at point 2 ( after compression )
        :param heat_rejection_efficiency: efficiency of heat exchanger
        :param ambient_temp: ambient temperature of the surrounding
        """

        self.p2_pressure = p2_pressure
        self.t2_temperature = t2_temp
        self.efficiency = heat_rejection_efficiency
        self.ambient_temp = ambient_temp
        self.p3_pressure = self.p2_pressure
        self.t3_temperature = None
        self.volume_v3 = None

    def get_output(self):
        # Heat Rejection - Isobaric step in this heat exchanger, releasing heat to the surroundings.
        self.t3_temperature = self.t2_temperature - self.efficiency * (
            self.t2_temperature - self.ambient_temp
        )  # Heat exchanger effectiveness applied
        return self.p3_pressure, self.t3_temperature

    def calculate_volume(self):

        self.volume_v3 = (self.t3_temperature*1000*0.287/self.p3_pressure)
        print("volume v3:",self.volume_v3)
        return self.volume_v3
