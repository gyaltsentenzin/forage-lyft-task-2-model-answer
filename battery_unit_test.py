import unittest
from datetime import date
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class BatteryUnitTest(unittest.TestCase):
    def test_NubbinBatteryServiceDate(self):
        self.battery = NubbinBattery(date(2023, 10, 9), date(2022, 10, 9))
        self.assertEqual(self.battery.needs_service(), False)

        self.battery = NubbinBattery(date(2023, 10, 9), date(2014, 10, 9))
        self.assertEqual(self.battery.needs_service(), True)

    def test_SpindlerServiceDate(self):
        self.battery = SpindlerBattery(date(2023, 10, 9), date(2022, 10, 9))
        self.assertEqual(self.battery.needs_service(), False)

        self.battery = SpindlerBattery(date(2023, 10, 10), date(2020, 10, 9))
        self.assertEqual(self.battery.needs_service(), True)

if __name__ == "__main__":
    unittest.main()
