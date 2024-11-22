# tests/test_main.py
import unittest
from car_wash_station import CarWashStation  # Импортируем модуль из корня проекта

class TestCarWashStation(unittest.TestCase):
    def setUp(self):
        self.station = CarWashStation()

    def test_add_car(self):
        self.station.add_car('Car 1')
        self.assertIn('Car 1', self.station.cars)

    def test_remove_car(self):
        self.station.add_car('Car 1')
        self.station.remove_car('Car 1')
        self.assertNotIn('Car 1', self.station.cars)

if __name__ == '__main__':
    unittest.main()

