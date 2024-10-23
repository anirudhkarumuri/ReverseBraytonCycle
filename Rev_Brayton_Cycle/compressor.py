from .medium import Medium

class Compressor(Medium):

    """
    Class handles computation of pressure and temperature calculations.
    """

    __slots__ = ["initial_pressure", "initial_temperature", "compression_ratio"]

    def __init__(self, initial_pressure: float, initial_temperature: float, compression_ratio: float) -> None:
        """
        Initializes the initial conditions of the compressor
        Args:
            initial_pressure: Pressure of the gas before entering the compressor
            initial_temperature: initial temperature of gas before entering the compressor
            compression_ratio: Pressure compression rate (Centrifugal/axial, not bore and stroke)
        Returns: None
        """

        super().__init__(initial_pressure,initial_temperature)
        self.compression_ratio : float = compression_ratio
        self.cp = None

    def calculate_pressure_temperature(self):
    # Performs isentropic compression
        """
        Calculates the pressure and temperature of the gas"""

        self.cp ,gamma = self.specific_heat_ratio()

        # the following equation is considered only when the compressor is a type of bore and stroke
        # pressure_p2= self.initial_pressure*pow(self.compression_ratio,gamma)

        pressure_p2 = self.initial_pressure*self.compression_ratio
        t2_temperature = self.initial_temperature*pow(pressure_p2/self.initial_pressure,(1-1/gamma))
        return pressure_p2, t2_temperature

    def calculate_work_done(self):
        # work done = m (kg/s) * (h2-h1) ie cp(T2-T1)
        # getcp
        compressor_work = (self.cp * self.initial_temperature* (pow(self.compression_ratio,(self.gamma - 1) / self.gamma) - 1))
        pass

