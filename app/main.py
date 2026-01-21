class Car:
    def __init__(self, comfort_cars: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_cars
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_raiting: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_raiting

    def serve_cars(self, dirty_cars: list[Car]) -> float:
        price = 0
        for car in dirty_cars:
            if car.clean_mark < self.clean_power:
                price += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return price

    def calculate_washing_price(self, washing_car: Car) -> float:
        equal_cl = (self.clean_power - washing_car.clean_mark)
        pre_price = washing_car.comfort_class * equal_cl * self.average_rating
        price = pre_price / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, washing_car: Car) -> None:
        washing_car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        current_rating = (self.average_rating * self.count_of_ratings)
        self.count_of_ratings += 1
        new_rat = round((current_rating + rate) / self.count_of_ratings, 1)
        self.average_rating = new_rat
