class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, single_car: Car) -> float:
        return round((single_car.comfort_class
                      * (self.clean_power - single_car.clean_mark)
                      * self.average_rating
                      / self.distance_from_city_center), 1)

    def serve_cars(self, car_instance: list) -> None:
        total_money = 0
        for i in car_instance:
            if i.clean_mark < self.clean_power:
                money = self.calculate_washing_price(i)
                cleaner = self.wash_single_car(i.clean_mark)
                total_money += money
                i.clean_mark = cleaner
        return total_money

    def wash_single_car(self, clean_level: int) -> None:
        if clean_level < self.clean_power:
            clean_level = self.clean_power
        return clean_level

    def rate_service(self, rate_in: float) -> None:
        self.average_rating = round(((self.average_rating
                                      * self.count_of_ratings)
                                     + rate_in) / (self.count_of_ratings
                                                   + 1), 1)
        self.count_of_ratings += 1
