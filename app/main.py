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

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income = income + self.calculate_washing_price(car)
                car.clean_mark = self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        price = round(car.comfort_class * (self.clean_power - car.clean_mark)
                      * self.average_rating / self.distance_from_city_center, 1)
        return price

    def wash_single_car(self, car: Car) -> int:
        car.clean_mark = self.clean_power
        return car.clean_mark

    def rate_service(self, rate: int) -> float:
        new_rating = round(((self.average_rating * self.count_of_ratings)
                            + rate) / (self.count_of_ratings + 1), 1)
        self.average_rating = new_rating
        self.count_of_ratings += 1
        return self.average_rating

bmw = Car(comfort_class=3, clean_mark=3, brand='BMW')
audi = Car(comfort_class=4, clean_mark=9, brand='Audi')

wash_station = CarWashStation(
    distance_from_city_center=5,
    clean_power=6,
    average_rating=3.5,
    count_of_ratings=6
)
