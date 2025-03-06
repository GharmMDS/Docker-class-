import unittest
from trip_calculator import calculate_fuel_needed, calculate_trip_cost

class TestTripCalculator(unittest.TestCase):
    
    def test_calculate_fuel_needed(self):
        self.assertAlmostEqual(calculate_fuel_needed(100), 5.0)
        self.assertAlmostEqual(calculate_fuel_needed(50), 2.5)
        self.assertRaises(ValueError, calculate_fuel_needed, -100)
        self.assertRaises(ValueError, calculate_fuel_needed, 100, -5)
    
    def test_calculate_trip_cost(self):
        self.assertAlmostEqual(calculate_trip_cost(100, 1.5), 7.5)
        self.assertAlmostEqual(calculate_trip_cost(200, 2.0), 20.0)
        self.assertRaises(ValueError, calculate_trip_cost, 100, -1.5)

if __name__ == "__main__":
    unittest.main()