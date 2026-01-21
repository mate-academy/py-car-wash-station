class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center,
        clean_power,
        average_rating,
        count_of_ratings
    ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car):
        """Calculate price for a single car wash."""
        diff = self.clean_power - car.clean_mark
        price = (
            car.comfort_class
            * diff
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car):
        """Wash car up to clean_power."""
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars):
        """Serve list of cars and return total income."""
        total_income = 0.0

        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(total_income, 1)

    def rate_service(self, new_rating):
        """Add one new rating and recalculate average."""
        total_sum = (
            self.average_rating * self.count_of_ratings + new_rating
        )
        self.count_of_ratings += 1
        self.average_rating = round(
            total_sum / self.count_of_ratings, 1
        )
