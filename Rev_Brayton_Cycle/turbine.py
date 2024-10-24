from .medium import Medium

class Turbine(Medium):

    """
    Class handles computation of pressure and temperature calculations.
    """

    def __init__(self, compression_ratio, pressure_p3, temperature_t3):
        super().__init__(pressure_p3, temperature_t3)
        self.compression_ratio : float = compression_ratio
        self.pressure_p3 : float = pressure_p3
        self.temperature_t3 : float = temperature_t3
        self.cp =None
        self.gamma = None

    def calculate_pressure_temperature(self):
    # Performs isentropic expansion
        """
        Calculates the pressure and temperature of the gas"""
        pressure_p4 = self.pressure_p3/self.compression_ratio
        self.cp, self.gamma = self.specific_heat_ratio()
        t4_temperature = self.temperature_t3*(1/pow(self.compression_ratio,(1-1/self.gamma)))
        return float(pressure_p4), float(t4_temperature)

    def calculate_work_done(self):

        work_done = (self.cp * self.temperature_t3* (1-pow((1/self.compression_ratio),(self.gamma -1)/self.gamma)))
        return float(work_done)

