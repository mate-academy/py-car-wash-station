import unittest
from app.main import Car, CarWashStation


class TestCarWashStation(unittest.TestCase):
    def setUp(self):
        self.station = CarWashStation(station_id=1, location_id=101, avg_rating=4.5, num_ratings=200)

    def test_add_car(self):
        car = Car(comfort_class=2, clean_mark=5, brand="Toyota")
        self.station.add_car(car)
        self.assertIn(car, self.station.cars, "Car should be added to the station.")

    def test_remove_car(self):
        car = Car(comfort_class=3, clean_mark=4, brand="BMW")
        self.station.add_car(car)
        self.station.remove_car(car)
        self.assertNotIn(car, self.station.cars, "Car should be removed from the station.")


class TestCar(unittest.TestCase):
    def test_car_initialization(self):
        car = Car(comfort_class=3, clean_mark=4, brand="Audi")
        self.assertEqual(car.comfort_class, 3, "Car comfort_class should be initialized correctly.")
        self.assertEqual(car.clean_mark, 4, "Car clean_mark should be initialized correctly.")
        self.assertEqual(car.brand, "Audi", "Car brand should be initialized correctly.")


if __name__ == '__main__':
    unittest.main()