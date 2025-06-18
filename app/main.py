class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        if not isinstance(comfort_class, int) or not (1 <= comfort_class <= 7):
            raise ValueError("comfort_class must be an integer from 1 to 7")

        if not isinstance(clean_mark, int) or not (1 <= clean_mark <= 10):
            raise ValueError("clean_mark must be an integer from 1 to 10")

        if not isinstance(brand, str) or not brand:
            raise ValueError("brand must be a non-empty string")

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
    ):
        if not isinstance(distance_from_city_center, (float, int)) or not (
            1.0 <= distance_from_city_center <= 10.0
        ):
            raise ValueError("distance_from_city_center must be a number from 1.0 to 10.0")

        if not isinstance(clean_power, int) or not (1 <= clean_power <= 10):
            raise ValueError("clean_power must be an integer from 1 to 10")

        if not isinstance(average_rating, (float, int)) or not (1.0 <= average_rating <= 5.0):
            raise ValueError("average_rating must be a number from 1.0 to 5.0")

        if not isinstance(count_of_ratings, int) or count_of_ratings < 0:
            raise ValueError("count_of_ratings must be a non-negative integer")

        self.distance_from_city_center = float(distance_from_city_center)
        self.clean_power = clean_power
        self.average_rating = round(float(average_rating), 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        if self.clean_power <= car.clean_mark:
            return 0.0
        wash_price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(wash_price, 1)

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                total_income += price
                self.wash_single_car(car)
        return round(total_income, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        new_rate = (
            self.average_rating * self.count_of_ratings + rate
        ) / (self.count_of_ratings + 1)
        self.count_of_ratings += 1
        self.average_rating = round(new_rate, 1)
