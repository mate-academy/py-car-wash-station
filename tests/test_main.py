import pytest
from app.main import Car, CarWashStation


def test_car_initialization() -> None:
    car = Car(3, 5, "BMW")
    assert car.comfort_class == 3
    assert car.clean_mark == 5
    assert car.brand == "BMW"


def test_calculate_washing_price() -> None:
    car = Car(3, 3, "BMW")
    ws = CarWashStation(5.0, 6, 3.5, 6)
    assert ws.calculate_washing_price(car) == 6.3


def test_serve_cars() -> None:
    bmw = Car(3, 3, "BMW")
    audi = Car(4, 9, "Audi")
    ws = CarWashStation(5.0, 6, 3.5, 6)
    income = ws.serve_cars([bmw, audi])
    assert income == 6.3
    assert bmw.clean_mark == 6
    assert audi.clean_mark == 9