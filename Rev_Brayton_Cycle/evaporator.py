from .medium import Medium
class Evaporator(Medium):

    def __init__(self, p4_pressure, t4_temp, heat_absorption_efficiency):
        """
        :param p2_pressure: pressure of the gas at point 2 ( after compression )
        :param t2_temp: temperature of the gas at point 2 ( after compression )
        :param heat_rejection_efficiency: efficiency of heat exchanger
        :param ambient_temp: ambient temperature of the surrounding
        """
        super().__init__(p4_pressure, t4_temp)
        self.p4_pressure = p4_pressure
        self.t4_temperature = t4_temp
        self.efficiency = heat_absorption_efficiency


    def get_heat_added(self, inlet_temperature):
        delta_temp = inlet_temperature-self.t4_temperature
        cp, gamma =self.specific_heat_ratio()
        heat_added = delta_temp * cp

        return heat_added

