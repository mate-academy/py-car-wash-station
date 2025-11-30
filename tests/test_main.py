from app.main import Car, CarWashStation


def test_wash_single_car() -> None:
    station = CarWashStation(10, 50, 4.5, 5)
    car = Car(3, 30, "Toyota")
    station.wash_single_car(car)
    assert car.clean_mark == 50


def test_serve_cars() -> None:
    station = CarWashStation(10, 50, 4.5, 5)
    cars = [
        Car(3, 30, "Toyota"),
        Car(5, 60, "BMW"),
        Car(2, 40, "Lada"),
    ]
    income = station.serve_cars(cars)
    assert income == 36.0   # ← исправлено
    assert cars[0].clean_mark == 50
    assert cars[1].clean_mark == 60
    assert cars[2].clean_mark == 50


def test_calculate_washing_price() -> None:
    station = CarWashStation(10, 50, 4.5, 5)
    car = Car(3, 30, "Toyota")
    price = station.calculate_washing_price(car)
    assert price == 27.0


def test_rate_service() -> None:
    station = CarWashStation(10, 50, 4.5, 5)
    station.rate_service(5.0)
    assert station.average_rating == 4.6
    assert station.count_of_ratings == 6
