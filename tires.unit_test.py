import unittest
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoPrimeTires

class TiresUnitTest(unittest.TestCase):
    def test_CarriganServiceDate(self):
        self.tires = CarriganTires([0,1,1,0])
        self.assertEqual(self.tires.needs_service(), True)
    
        self.tires = CarriganTires([0,0.2,0.2,0.7])
        self.assertEqual(self.tires.needs_service(), False)

    def test_OctoprimeServiceDate(self):
        self.tires = OctoPrimeTires([0,0,1,0])
        self.assertEqual(self.tires.needs_service(), False)

        self.tires = OctoPrimeTires([1,0.8,1,0.8])
        self.assertEqual(self.tires.needs_service(), True)
        

if __name__ == "__main__":
    unittest.main()
