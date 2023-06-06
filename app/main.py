class Car:

    def __init__(self, comfort_class: int, clean_mark: int, brand: str) \
            -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int, clean_power: int,
                 average_rating: (int, float), count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_cars: list[Car]) -> object:
        serving_price = 0
        for i in list_of_cars:
            serving_price += self.calculate_washing_price(i)
            self.wash_single_car(i)
        return serving_price

    def calculate_washing_price(self, veh: Car) -> float:
        if self.clean_power > veh.clean_mark:
            price = veh.comfort_class * (self.clean_power - veh.clean_mark) * \
                (self.average_rating / self.distance_from_city_center)
        else:
            return 0
        return round(price, 1)

    def wash_single_car(self, veh: Car) -> None:
        if veh.clean_mark < self.clean_power:
            veh.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        new_amount = self.count_of_ratings + 1
        new_rating = ((self.average_rating * self.count_of_ratings) + rating) \
            / new_amount
        self.average_rating = round(new_rating, 1)
        self.count_of_ratings += 1
