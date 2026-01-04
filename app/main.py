class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car):
        """Calculates the washing price for a single car based on the given formula."""
        return round(
            car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating / self.distance_from_city_center,
            1,
        )

    def wash_single_car(self, car):
        """Washes a single car if its clean_mark is below clean_power."""
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars):
        """Washes eligible cars and returns total income."""
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(income, 1)

    def rate_service(self, new_rating):
        """Updates the wash station's rating based on a new rating received."""
        total_rating = self.average_rating * self.count_of_ratings
        total_rating += new_rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)
