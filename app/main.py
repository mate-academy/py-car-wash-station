class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            cleanliness_difference = self.clean_power - car.clean_mark
            base_price_multiplier = car.comfort_class * self.average_rating
            single_car_cost = (base_price_multiplier * cleanliness_difference
                               / self.distance_from_city_center)
            return round(single_car_cost, 1)
        return 0.0

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        income_total = 0

        for car in cars:
            if car.clean_mark >= self.clean_power:
                continue
            income = self.calculate_washing_price(car)
            income_total += income
            self.wash_single_car(car)

        return round(income_total, 1)

    def rate_service(self, rating: int | float) -> float:
        """Updates the average rating based on a new customer rating."""
        self.count_of_ratings += 1
        total_previous_ratings = (self.average_rating
                                  * (self.count_of_ratings - 1))
        total_ratings_with_new = total_previous_ratings + rating
        new_average_rating = total_ratings_with_new / self.count_of_ratings
        self.average_rating = round(new_average_rating, 1)

        return self.average_rating
