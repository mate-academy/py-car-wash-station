class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str
    ) -> None:
        if not 1 <= comfort_class <= 7:
            raise ValueError("comfort_class must be from 1 to 7")
        self.comfort_class = comfort_class
        if not 1 <= clean_mark <= 10:
            raise ValueError("clean_mark must be from 1 to 10")
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: float,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        if not 1.0 <= distance_from_city_center <= 10.0:
            raise ValueError("distance must be from 1.0 to 10.0")
        self.distance_from_city_center = distance_from_city_center
        if not 1 <= clean_power <= 10:
            raise ValueError("clean_power must be from 1.0 to 10.0 ")
        self.clean_power = clean_power
        if not 1 <= average_rating <= 5.0:
            raise ValueError("rating must be from 1.0 to 5.0")
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            wash_price = (
                car.comfort_class
                * (self.clean_power - car.clean_mark)
                * self.average_rating
                / self.distance_from_city_center
            )
            return round(wash_price, 1)
        return 0.0

    def serve_cars(self, cars: list) -> float:

        income = 0

        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, mark: int) -> None:
        sum_all_marks = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round(
            (sum_all_marks + mark)
            / self.count_of_ratings, 1
        )
