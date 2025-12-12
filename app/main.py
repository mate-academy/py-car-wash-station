class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
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

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calculates cost:
        (comfort_class * (clean_power - car_clean_mark) * rating) / distance
        """
        diff = self.clean_power - car.clean_mark
        if diff <= 0:
            return 0.0

        cost = ((car.comfort_class * diff * self.average_rating)
                / self.distance_from_city_center)
        return round(cost, 1)

    def wash_single_car(self, car: Car) -> None:
        """
        Washes a single car if station power is greater than car's clean mark.
        """
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list) -> float:
        """
        Takes a list of cars, calculates income, and washes suitable cars.
        """
        income = 0
        for car in cars:
            # Check if the station can actually clean this car
            if car.clean_mark < self.clean_power:
                # Calculate price BEFORE washing (otherwise difference is 0)
                price = self.calculate_washing_price(car)
                income += price
                # Wash the car
                self.wash_single_car(car)

        return round(income, 1)

    def rate_service(self, rating: int) -> None:
        """
        Adds a single rate and updates average_rating and count_of_ratings.
        """
        total_rating_value = self.average_rating * self.count_of_ratings
        total_rating_value += rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating_value
                                    / self.count_of_ratings, 1)
