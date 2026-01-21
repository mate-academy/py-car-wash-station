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
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car_list: list[Car]) -> float:
        total_income = 0.0

        for car in car_list:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        comfort_class = car.comfort_class
        clean_mark_difference = self.clean_power - car.clean_mark
        rating = self.average_rating
        distance_to_center = self.distance_from_city_center
        cost = ((comfort_class * clean_mark_difference
                 * rating) / distance_to_center)
        return round(cost, 1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        previous_total = self.average_rating * self.count_of_ratings
        new_total = previous_total + rating
        self.average_rating = new_total / (self.count_of_ratings + 1)
        self.count_of_ratings += 1
        self.average_rating = round(self.average_rating, 1)
