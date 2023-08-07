class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:

        self.comfort_class = comfort_class
        if not 1 <= comfort_class <= 7:
            raise ValueError(
                f"The value of comfort_class must be between 1 and 7\n"
                f"Your value: {comfort_class}"
            )

        self.clean_mark = clean_mark
        if not 1 <= clean_mark <= 10:
            raise ValueError(
                f"The value of clean_mark must be between 1 and 10\n"
                f"Your value: {clean_mark}"
            )

        self.brand = brand
        if not type(brand) == str:
            raise ValueError(
                f"Type of brand must be str\n"
                f"Your value have {type(brand)} type"
            )


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:

        self.distance_from_city_center = distance_from_city_center
        if not 1.0 <= distance_from_city_center <= 10.0:
            raise ValueError(
                f"The value of distance_from_city_center"
                f" must be between 1.0 and 10.0\n"
                f"Your value: {distance_from_city_center}"
            )

        self.clean_power = clean_power
        if not 1 <= clean_power <= 10:
            raise ValueError(
                f"The value of clean_power must be between 1 and 10\n"
                f"Your value: {clean_power}"
            )

        self.average_rating = average_rating
        if not 1.0 <= average_rating <= 5.0:
            raise ValueError(
                f"The value of average_rating must be between 1.0 and 5.0\n"
                f"Your value: {average_rating}"
            )

        self.count_of_ratings = count_of_ratings
        if not type(count_of_ratings) == int:
            raise ValueError(
                f"Type of count_of_ratings must be int\n"
                f"Your value have {type(count_of_ratings)} type"
            )

    def calculate_washing_price(self, car: Car) -> float:
        return round((car.comfort_class * (
            self.clean_power - car.clean_mark) * (
            self.average_rating / self.distance_from_city_center)), 1)

    def wash_single_car(self, car: Car) -> float:
        return car.clean_mark < self.clean_power

    def serve_cars(self, cars: list) -> float:
        profit = 0

        for car in cars:
            if self.wash_single_car(car):
                profit += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power

        return profit

    def rate_service(self, rate: int) -> None:
        self.average_rating = (
            self.average_rating * self.count_of_ratings + rate) / (
            self.count_of_ratings + 1)

        self.average_rating = round(self.average_rating, 1)
        self.count_of_ratings += 1
