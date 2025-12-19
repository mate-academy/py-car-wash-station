class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self, distance_from_city_center, clean_power, average_rating, count_of_ratings
    ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        price_list = []
        for car in cars:
            if car.clean_mark < self.clean_power:
                price_list.append(self.calculate_washing_price(car))
                self.wash_single_car(car)
        return round(sum(price_list), 1)

    def rate_service(self, rating: float) -> None:
        new_rating = ((self.average_rating * self.count_of_ratings) + rating) / (
            self.count_of_ratings + 1
        )
        self.average_rating = round(new_rating, 1)
        self.count_of_ratings += 1
