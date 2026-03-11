class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
        self.distance_from_city_center = float(distance_from_city_center)
        self.clean_power = clean_power
        self.average_rating = float(average_rating)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car):
        """Calculates the price for a potential wash."""
        price = (car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating /
                 self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car):
        """Washes the car to the station's clean_power capacity."""
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars):
        """Serves a list of cars, updates their status, and returns total income."""
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(total_income, 1)

    def rate_service(self, new_rate):
        """Updates the station's average rating based on a new review."""
        total_score = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round((total_score + new_rate) / self.count_of_ratings, 1)
