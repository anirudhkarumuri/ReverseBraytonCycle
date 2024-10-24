from .medium import Medium
class Evaporator(Medium):

    def __init__(self, p4_pressure, t4_temp):
        """
        :param p2_pressure: pressure of the gas at point 2 ( after compression )
        :param t2_temp: temperature of the gas at point 2 ( after compression )
        :param heat_rejection_efficiency: efficiency of heat exchanger
        :param ambient_temp: ambient temperature of the surrounding
        """
        super().__init__(p4_pressure, t4_temp)
        self.p4_pressure = p4_pressure
        self.t4_temperature = float(t4_temp)


    def get_heat_added(self, inlet_temperature):
        print('Initial temperature inside get_heat_added:', inlet_temperature)
        delta_temp = inlet_temperature-float(self.t4_temperature)
        print(delta_temp ,self.t4_temperature)
        cp, gamma =self.specific_heat_ratio()
        heat_added = delta_temp * cp
        # considering unit mass flow
        print(cp, gamma, heat_added)
        return heat_added

