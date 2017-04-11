from windpowerlib.density import (temperature_gradient, temperature_interpol,
                                  rho_barometric, rho_ideal_gas)
import pandas as pd
from pandas.util.testing import assert_series_equal

class TestDensityTemperature:

    @classmethod
    def setUpClass(self):
        self.h_hub = 100
        self.weather = {'temp_air': pd.Series(data=[267, 268]),
                        'temp_air_2': pd.Series(data=[267, 266]),
                        'pressure': pd.Series(data=[101125, 101000])}
        self.data_height = {'temp_air': 2,
                            'temp_air_2': 10,
                            'pressure': 0}

    def test_temperature_gradient(self):
        T_hub_exp = pd.Series(data=[266.363, 267.36300])
        assert_series_equal(temperature_gradient(self.weather['temp_air'],
                                                 self.data_height['temp_air'],
                                                 self.h_hub), T_hub_exp)

    def test_temperature_interpol(self):
        T_hub_exp = pd.Series(data=[267.0, 243.5])
        assert_series_equal(temperature_interpol(
            self.weather['temp_air'], self.weather['temp_air_2'],
            self.data_height['temp_air'], self.data_height['temp_air_2'],
            self.h_hub), T_hub_exp)

    def test_rho_barometric(self):
        rho_exp = pd.Series(data=[1.30305, 1.29657])
        assert_series_equal(
            rho_barometric(self.weather['pressure'],
                           self.data_height['pressure'], self.h_hub,
                           self.weather['temp_air']), rho_exp)

    def test_rho_ideal_gas(self):
        rho_exp = pd.Series(data=[1.3030943, 1.29661])
        assert_series_equal(rho_ideal_gas(
            self.weather['pressure'], self.data_height['pressure'],
            self.h_hub, self.weather['temp_air']), rho_exp)
