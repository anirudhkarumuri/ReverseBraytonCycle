from .medium import Medium


class Compressor(Medium):

    """
    Class handles computation of pressure and temperature calculations.
    """

    __slots__ = ["initial_pressure", "initial_temperature", "compression_ratio"]
    # slots will make the access of the variables faster.

    def __init__(self, initial_pressure: float, initial_temperature: float, compression_ratio: float):
        super().__init__(initial_pressure,initial_temperature)
        self.compression_ratio : float = compression_ratio


    def calculate_pressure_temperature(self):
    # Performs isentropic compression
        """
        Calculates the pressure and temperature of the gas"""

        gamma = self.specific_heat_ratio()
        pressure_p2= self.initial_pressure*pow(self.compression_ratio,gamma)
        t2_temperature = self.initial_temperature*pow(pressure_p2/self.initial_pressure,(1-1/gamma))
        return pressure_p2, t2_temperature

    def calculate_word_done(self):

        # work done = m (kg/s) * (h2-h1)
        pass

