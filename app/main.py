class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = self.set_comfort_class(comfort_class)
        self.clean_mark = self.get_clean_mark(clean_mark)
        self.brand = brand

    def set_comfort_class(self, comfort_class: int) -> int:
        if 1 <= comfort_class <= 7:
            return comfort_class
        else:
            raise ValueError("comfort class of a car, from 1 to 7")

    def get_clean_mark(self, clean_mark: int) -> int:
        if 1 <= clean_mark <= 10:
            return clean_mark
        else:
            raise ValueError(
                "The cleanliness rating should be between 1 and 10"
            )

    def wash(self, clean_power: int) -> None:
        if clean_power > self.clean_mark:
            self.clean_mark = clean_power


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = \
            (self.set_distance_from_city_center
             (distance_from_city_center)
             )
        self.clean_power = clean_power
        self.average_rating = self.set_average_rating(average_rating)
        self.count_of_ratings = count_of_ratings

    def set_distance_from_city_center(self, distance: float) -> float:
        if 1.0 <= distance <= 10.0:
            return distance
        else:
            raise ValueError("The distance must be between 1.0 and 10.0")

    def set_average_rating(self, rating: float) -> float:
        if 1.0 <= rating <= 5.0:
            return round(rating, 1)
        else:
            raise ValueError(
                "The average rating should be between 1.0 and 5.0"
            )

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            price = ((car.comfort_class * (
                self.clean_power - car.clean_mark
            ) * self.average_rating) / self.distance_from_city_center)
            return round(price, 1)
        return 0.0

    def serve_cars(self, cars: list) -> float:
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                wash_cost = self.calculate_washing_price(car)
                total_income += wash_cost
                car.wash(self.clean_power)
        return round(total_income, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> None:
        if 1.0 <= rating <= 5.0:
            self.count_of_ratings += 1
            total_rating = (self.average_rating * (
                self.count_of_ratings - 1) + rating)
            self.average_rating = (
                round(total_rating / self.count_of_ratings, 1)
            )
        else:
            raise ValueError("The rating must be between 1.0 and 5.0")

