class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:

        clean_difference = max(0, self.clean_power - car.clean_mark)

        cost = (
            car.comfort_class * clean_difference
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(cost, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list) -> float:
        total_income = 0.0

        for car in cars:
            if car.clean_mark < self.clean_power:
                cost = round(self.calculate_washing_price(car), 1)
                total_income += cost

                self.wash_single_car(car)

        return total_income

    def rate_service(self, new_rate: int) -> None:

        total_points = self.average_rating * self.count_of_ratings

        new_total_points = total_points + new_rate
        new_count = self.count_of_ratings + 1
        self.count_of_ratings = new_count
        self.average_rating = round(new_total_points / new_count, 1)
