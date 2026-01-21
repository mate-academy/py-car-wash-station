class Car:
    def __init__(self,

                 comfort_class: int,
                 clean_mark: int,
                 brand: str

                 ) -> None:

        self.comfort_class: int = comfort_class
        self.clean_mark: int = clean_mark
        self.brand: str = brand


class CarWashStation:
    def __init__(self,

                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int

                 ) -> None:

        self.distance_from_city_center: float = round(
            distance_from_city_center, 1
        )
        self.clean_power: int = clean_power
        self.average_rating: float = average_rating
        self.count_of_ratings: int = round(count_of_ratings, 1)

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class * abs(self.clean_power - car.clean_mark)
            * (self.average_rating / self.distance_from_city_center), 1
        )

    def wash_single_car(self, car: Car) -> float:

        if car.clean_mark < self.clean_power:

            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power

            return price

        else:

            return 0

    def rate_service(self, rate: int) -> float:

        new_rate = (self.count_of_ratings * self.average_rating) + rate
        self.count_of_ratings += 1
        self.average_rating = round(new_rate / self.count_of_ratings, 1)

        return self.average_rating

    def serve_cars(self, cars: list) -> float:

        price = 0

        for car in cars:
            price += self.wash_single_car(car)

        return price
