class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_centre: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int,
    ) -> None:
        self.distance_from_city_centre = distance_from_city_centre
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        cleanness_diff = self.clean_power - car.clean_mark

        price = (
            car.comfort_class
            * cleanness_diff
            * self.average_rating
            / self.distance_from_city_centre
        )
        return round(price, 1)

    # Added missing colon here
    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0.0

        for car in cars:
            # Fixed: changed self.average_rating to self.clean_power
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, rating: int) -> None:
        total_rating_score = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1

        new_average_rating = ((total_rating_score + rating)
                              / self.count_of_ratings)
        # Fixed: matched the variable name to new_average_rating
        self.average_rating = round(new_average_rating, 1)
