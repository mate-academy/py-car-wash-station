class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        if not (isinstance(comfort_class, int)
                and comfort_class in range(1, 8)):
            raise ValueError("comfort_class argument must be from 1 to 7")
        self.comfort_class = comfort_class

        if not (isinstance(clean_mark, int)
                and clean_mark in range(1, 11)):
            raise ValueError(
                "clean_mark argument must be from very dirty - 1 to clean - 10"
            )
        self.clean_mark = clean_mark

        if not (isinstance(brand, str)):
            raise TypeError("brand argument is not string")
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: int | float,
            clean_power: int,
            average_rating: int | float,
            count_of_ratings: int
    ) -> None:
        if not (isinstance(distance_from_city_center, int | float)
                and distance_from_city_center
                in [value / 10.0 for value in range(1, 101, 1)]):
            raise ValueError(
                "distance_from_city_center argument must be from 1.0 to 10.0"
            )
        self.distance_from_city_center = distance_from_city_center

        if not (isinstance(clean_power, int)
                and clean_power in range(1, 11)):
            raise ValueError(
                "clean_power argument must be from powerful 1 to powerless 10"
            )
        self.clean_power = clean_power

        if not (isinstance(average_rating, int | float)
                and average_rating
                in [value / 10.0 for value in range(1, 51, 1)]):
            raise ValueError("average_rating argument must be from 1.0 to 5.0")
        self.average_rating = average_rating

        if not (isinstance(count_of_ratings, int)):
            raise TypeError("count_of_ratings argument is not integer")
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            if self.clean_power >= car.clean_mark:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        cost = (car.comfort_class
                * (self.clean_power - car.clean_mark)
                * (self.average_rating
                   / self.distance_from_city_center))
        return round(cost, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        self.average_rating = round((self.count_of_ratings
                                     * self.average_rating
                                     + rating)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
