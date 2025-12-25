class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:

        if comfort_class < 1 or comfort_class > 7:
            raise ValueError("Error, "
                             "you need to change the value of comfort_class, "
                             "it has to be from 1 to 7")

        if clean_mark < 1 or clean_mark > 10:
            raise ValueError("Error, "
                             "you need to change the value of clean_mark, "
                             "it has to be from 1 to 10")

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

        if distance_from_city_center < 1.0 or distance_from_city_center > 10.0:
            raise ValueError("Error, "
                             "istance_from_city_center "
                             "has to be from 1.0 to 10.0")

        if average_rating < 1.0 or average_rating > 5.0:
            raise ValueError("Error, "
                             "you need to change the value of average_rating, "
                             "it has to be from 1.0 to 5.o")
        self.average_rating = average_rating
        self.clean_power = clean_power
        self.count_of_ratings = count_of_ratings
        self.distance_from_city_center = distance_from_city_center

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> int:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        price = (
            car.comfort_class * (self.clean_power - car.clean_mark)
            * (self.average_rating / self.distance_from_city_center)
        )
        return round(price, 1)

    def rate_service(self, rating: int) -> None:
        new_total_rating = self.average_rating * self.count_of_ratings + rating
        self.count_of_ratings += 1
        self.average_rating = round(new_total_rating
                                    / self.count_of_ratings, 1)
