class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        if comfort_class < 1 or comfort_class > 7:
            raise ValueError("comfort_class must be between 1 and 7")
        if clean_mark < 1 or clean_mark > 10:
            raise ValueError("clean_mark must be between 1 and 10")
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

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power >= car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list) -> float:
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                total_income += price
                self.wash_single_car(car)
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        cost = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(cost, 1)

    def rate_service(self, new_rating: float) -> None:
        total_score = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        total_score += new_rating
        self.average_rating = round(total_score / self.count_of_ratings, 1)
