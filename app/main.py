class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def serve_cars(self, cars: list) -> None:
        washing_price = 0.0
        for car in cars:
            if self.clean_power > car.clean_mark:
                washing_price += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return washing_price

    def rate_service(self, new_rating: int) -> None:
        total_score = self.average_rating * self.count_of_ratings + new_rating
        self.count_of_ratings += 1
        self.average_rating = round(total_score / self.count_of_ratings, 1)


wash_station = CarWashStation(
    distance_from_city_center=6.0,
    clean_power=8,
    average_rating=3.9,
    count_of_ratings=11
)

bmw = Car(comfort_class=3, clean_mark=3, brand="BMW")
audi = Car(4, 9, "Audi")
