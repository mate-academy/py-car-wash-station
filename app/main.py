class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
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
        Calculate the cost of washing a car
        Formula: car's comfort class * (clean_power - car's clean mark) * rating / distance
        """
        price = (car.comfort_class
                 * (self.clean_power - car.clean_mark)
                 * self.average_rating
                 / self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        """
        Wash a single car, updating its clean mark to the station's clean power
        if the car's clean mark is less than the station's clean power
        """
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list) -> float:
        """
        Serve a list of cars, washing only those that can be washed (clean_mark < clean_power)
        Return the total income from washing the cars
        """
        total_income = 0.0

        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(total_income, 1)

    def rate_service(self, rating: float) -> None:
        """
        Add a new rating to the wash station
        Recalculate the average rating and increment the count of ratings
        """
        # Calculate the total sum of all previous ratings
        total_sum = self.average_rating * self.count_of_ratings

        # Add the new rating
        self.count_of_ratings += 1

        # Calculate the new average
        self.average_rating = round((total_sum + rating) / self.count_of_ratings, 1)

