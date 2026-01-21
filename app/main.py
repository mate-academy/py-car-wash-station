class Car:
    def __init__(self
                 , comfort_class: int
                 , clean_mark: int
                 , brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self
                 , distance_from_city_center: float
                 , clean_power: int
                 , average_rating: float
                 , count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * (self.average_rating / self.distance_from_city_center),
            1
        )

    def wash_single_car(self, car: Car) -> None:
        # if self.clean_power > car.clean_mark:
        car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        """
        Serve a list of cars and calculate total income.
        """
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                # Calculate washing price and update the total income
                price = self.calculate_washing_price(car)
                total_income += price
                # Wash the car
                self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, new_mark: float) -> None:
        """
        Add a single rating and update the average rating.
        """
        total_rating_sum = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round(
            (total_rating_sum + new_mark) / self.count_of_ratings, 1
        )
