import json
import sys

from Rev_Brayton_Cycle import *
# sys.path.append("./Rev_Brayton_Cycle")


class RevBraytonCycle:
    def __init__(
        self,
        initial_pressure,
        initial_temperature,
        pressure_ratio,
        heat_rejection_efficiency,
        ambient_temp,
    ):
        # Set initial conditions
        self.initial_pressure = initial_pressure
        self.initial_temperature = initial_temperature
        self.pressure_ratio = pressure_ratio
        self.heat_rejection_efficiency = heat_rejection_efficiency
        self.ambient_temp = ambient_temp
        self.heat_added = None

    def run_cycle(self):

        # Compression stage
        compressor_stage = Compressor(
            self.initial_pressure, self.initial_temperature, self.pressure_ratio
        )
        comp_out_pressure, comp_out_temp = compressor_stage.calculate_pressure_temperature()
        comp_in_volume, comp_out_vol = compressor_stage.calculate_volume()

        print(
            f"Compressor Output: Pressure = {comp_out_pressure} Pa, Temperature = {comp_out_temp} K"
        )
        compressor_work = compressor_stage.calculate_work_done()

        print(
            f"Compressor Output: Pressure = {comp_out_pressure} Pa, Temperature = {comp_out_temp} K, Work Done = {compressor_work} KW"
        )

        # Condenser Stage
        condenser_stage = Condenser(
            comp_out_pressure,
            comp_out_temp,
            self.heat_rejection_efficiency,
            self.ambient_temp,
        )
        cond_out_pressure, cond_out_temp = condenser_stage.get_output()
        v3_volume = condenser_stage.calculate_volume()

        print(
            f"Condenser Output: Pressure = {cond_out_pressure} Pa, Temperature = {cond_out_temp} K"
        )

        # Turbine Stage
        turbine_stage = Turbine(self.pressure_ratio, cond_out_pressure, cond_out_temp)
        turb_out_pressure, turb_out_temp = (
            turbine_stage.calculate_pressure_temperature()
        )
        turbine_work = turbine_stage.calculate_work_done()
        turbine_stage.calculate_volume(v3_volume)

        print(
            f"Turbine Output: Pressure = {turb_out_pressure} Pa, Temperature = {turb_out_temp} K, Work Done = {turbine_work} KW"
        )

        # Evaporator Stage (Heat Addition)
        evaporator_stage = Evaporator(turb_out_pressure, turb_out_temp)
        evap_heat = evaporator_stage.get_heat_added(self.initial_temperature)

        # Cycle Outputs: Return all relevant data
        return {
            "compressor": {
                "pressure_out": comp_out_pressure,
                "temperature_out": comp_out_temp,
                "work_done": compressor_work,
            },
            "condenser": {
                "pressure_out": cond_out_pressure,
                "temperature_out": cond_out_temp,
            },
            "turbine": {
                "pressure_out": turb_out_pressure,
                "temperature_out": turb_out_temp,
                "work_done": turbine_work,
            },
            "evaporator": {"heat_added": evap_heat},
            "net_work": {"net_work": compressor_work - turbine_work},
            "cop": float(self.calculate_cop(compressor_work, turbine_work, evap_heat)),
        }

    def calculate_cop(self, compressor_work, turbine_work, heat_added):
        """
        Calculate the coefficient of performance (COP) for the reverse Brayton cycle.
        COP = Q_evaporator / (W_compressor - W_turbine)
        :param compressor_work: Work done by the compressor
        :param turbine_work: Work done by the turbine (work extracted)
        :param heat_added: Heat added in the evaporator (Q_evaporator)
        :return: COP (coefficient of performance) value
        """

        net_work = compressor_work - turbine_work
        Cop = heat_added / net_work
        return Cop


rev_brayton_cycle = RevBraytonCycle(
    initial_pressure=101325,  # 1 atm
    initial_temperature=300,  # 300 K (ambient temp)
    pressure_ratio=2,  # Compression ratio
    heat_rejection_efficiency=0.8,  # Condenser efficiency
    ambient_temp=295,  # Ambient temperature (K)
)

# The values above have to be taken as inputs from the user from GUI. (Pending)

# Run the cycle
cycle_results = rev_brayton_cycle.run_cycle()

# Output the results including COP
print("\nCycle Results:", json.dumps(cycle_results, indent=3))
