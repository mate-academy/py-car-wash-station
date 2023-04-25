class Car:
    def __init__(self, comfort_class: None, clean_mark: None,
                 brand: None) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: None, clean_power: None,
                 average_rating: None, count_of_ratings: None) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: None) -> None:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: None) -> None:
        price = car.comfort_class * (((self.clean_power - car.clean_mark)
                                      * self.average_rating)
                                     / self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car: None) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: None) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rating)
            / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
