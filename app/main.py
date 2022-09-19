class Car:
    def __init__(self, comfort_class, clean_mark, brand) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self, distance_from_city_center, clean_power,
        average_rating, count_of_ratings
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list):
        cost = 0
        for car_instance in cars:

            car_was_washed = self.wash_single_car(car_instance)

            # Return the amount for the service, otherwise False
            if car_was_washed:
                cost += car_was_washed
        return cost

    def calculate_washing_price(self, car):
        cost = (car.comfort_class * (self.clean_power - car.clean_mark)
                * self.average_rating / self.distance_from_city_center)
        return round(cost, 1)

    def wash_single_car(self, car):
        if car.clean_mark <= self.clean_power:
            cost = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return cost
        return False

    def rate_service(self, rating):
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rating)
            / (self.count_of_ratings + 1),
            1
        )
        self.count_of_ratings += 1
