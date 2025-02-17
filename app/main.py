class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class  # comfort level
        self.clean_mark = clean_mark  # cleanliness level
        self.brand = brand  # car brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center  # distance -> center
        self.clean_power = clean_power  # cleaning power
        self.average_rating = average_rating  # average rating
        self.count_of_ratings = count_of_ratings  # number of ratings

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calculate the washing price for one car
        """
        comfort_factor = car.comfort_class
        cleanliness_factor = self.clean_power - car.clean_mark
        distance_factor = self.distance_from_city_center
        rating_factor = self.average_rating

        price = (comfort_factor * cleanliness_factor
                 * rating_factor / distance_factor)
        return price

    def wash_single_car(self, car: Car) -> None:
        """
        Wash the car if it needs
        """
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> None:
        """
        Rate the service and update the average rating
        """
        self.count_of_ratings += 1
        total_ratings = (self.average_rating
                         * (self.count_of_ratings - 1) + rating)
        self.average_rating = round(total_ratings / self.count_of_ratings, 1)

    def serve_cars(self, cars: list[Car]) -> float:
        """
        Serve the cars and calculate the total income
        """
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income = self.calculate_washing_price(car)
                total_income += income
                self.wash_single_car(car)
        return round(total_income, 1)
