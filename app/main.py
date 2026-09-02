class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


bmw = Car(comfort_class=4, clean_mark=5, brand="bmw")
audi = Car(comfort_class=3, clean_mark=8, brand="audi")

cars = [bmw, audi]


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings
        self.income = 0

    def serve_cars(self, cars: list) -> float:
        for car in cars:
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                self.wash_single_car(car)
                round(self.income) += price

        return self.income

    def wash_single_car(self, car: object) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: object) -> float:
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return price

    def rate_service(self, rate: float) -> None:
        self.count_of_ratings += 1
        self.average_rating += rate / self.count_of_ratings


west_village = CarWashStation(
    distance_from_city_center=1.0,
    clean_power=7,
    average_rating=1.0,
    count_of_ratings=0
)

west_village.serve_cars(cars)
west_village.calculate_washing_price(bmw)
west_village.wash_single_car(bmw)
west_village.rate_service(2.0)
