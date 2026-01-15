class Car:

    def __init__(self,
                 comfort_class: int, clean_mark: int,
                 brand: str) -> None:

        if comfort_class < 1 or comfort_class > 7:
            raise ValueError("comfort_class must be between 1 and 7")
        if clean_mark < 1 or clean_mark > 10:
            raise ValueError("clean_mark must be between 1 and 10")
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self,
                 distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        if not 1 <= clean_power <= 10:
            raise ValueError(
                "clean_power must be between 1 and 10"
            )
        if not (1.0 <= distance_from_city_center <= 10.0):
            raise ValueError(
                "distance_from_city_center must be between 1.0 and 10.0"
            )
        if not (1.0 <= average_rating <= 5.0):
            raise ValueError("average_rating must be between 1.0 and 5.0")
        if not (isinstance(count_of_ratings, int) and count_of_ratings >= 0):
            raise ValueError("count_of_ratings must be >= 0")
        self.distance_from_city_center = float(distance_from_city_center)
        self.clean_power = clean_power
        self.average_rating = round(float(average_rating), 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:

        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:

        diff = self.clean_power - car.clean_mark
        if diff <= 0:
            return 0.0
        part = car.comfort_class * diff * self.average_rating
        price = part / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:

        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:

        if not (1.0 <= float(rate) <= 5.0):
            raise ValueError("rate must be between 1.0 and 5.0")
        numerator = self.average_rating * self.count_of_ratings + float(rate)
        new_average = numerator / (self.count_of_ratings + 1)
        self.average_rating = round(new_average, 1)
        self.count_of_ratings += 1