class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0.0

        for car in cars:
            price = self.calculate_washing_price(car)
            if price > 0:
                total_income += price
                self.wash_single_car(car)

        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        dirt_difference = self.clean_power - car.clean_mark
        if dirt_difference <= 0:
            return 0.0

        price = (
            car.comfort_class
            * dirt_difference
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        if not 1 <= rate <= 5:
            raise ValueError("Rating must be between 1 and 5")

        total_score = self.average_rating * self.count_of_ratings
        total_score += rate
        self.count_of_ratings += 1
        self.average_rating = round(total_score / self.count_of_ratings, 1)
