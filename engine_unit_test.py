import unittest
from datetime import date
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class EngineUnitTest(unittest.TestCase):
    def test_Capulet(self):
        self.engine = CapuletEngine(20000, 4000)
        self.assertEqual(self.engine.needs_service(), False)

        self.engine = CapuletEngine(80000, 4000)
        self.assertEqual(self.engine.needs_service(), True)

        self.engine = CapuletEngine(30001, 0)
        self.assertEqual(self.engine.needs_service(), True)

    def test_Sternman(self):
        self.engine = SternmanEngine(True)
        self.assertEqual(self.engine.needs_service(), True)

        self.engine = SternmanEngine(False)
        self.assertEqual(self.engine.needs_service(), False)

    def test_Willoughby(self):
        self.engine = WilloughbyEngine(20000, 4000)
        self.assertEqual(self.engine.needs_service(), False)

        self.engine = WilloughbyEngine(80000, 4000)
        self.assertEqual(self.engine.needs_service(), True)

        self.engine = WilloughbyEngine(60001, 0)
        self.assertEqual(self.engine.needs_service(), True)

if __name__ == "__main__":
    unittest.main()