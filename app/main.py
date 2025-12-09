class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        if not (1 <= comfort_class <= 7):
            raise ValueError("comfort_class must be between 1 and 7")
        if not (1 <= clean_mark <= 10):
            raise ValueError("clean_mark must be between 1 and 10")

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

        if not (1.0 <= distance_from_city_center <= 10.0):
            raise ValueError(
                "distance_from_city_center must be between 1 and 10")
        if not (1 <= clean_power <= 10):
            raise ValueError("clean_power must be between 1 and 100")
        if not (1.0 <= average_rating <= 5.0):
            raise ValueError("average_rating must be between 1 and 5")
        if count_of_ratings < 0:
            raise ValueError("count_of_ratings must be non-negative")

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        total_income = (car.comfort_class
                        * (self.clean_power
                           - car.clean_mark)
                        * (self.average_rating
                           / self.distance_from_city_center))
        return round(total_income, 1)

    def wash_single_car(self, car: Car) -> bool:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
            return True
        return False

    def rate_service(self, new_rate: float) -> None:
        total_score = self.average_rating * self.count_of_ratings
        total_score += new_rate
        self.count_of_ratings += 1
        self.average_rating = round(total_score / self.count_of_ratings, 1)

    def serve_cars(self, cars: list) -> float:
        total_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)
