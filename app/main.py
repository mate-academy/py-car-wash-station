class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: int,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car_list: list[Car]) -> float:
        price = 0.0
        for car in car_list:
            if car.clean_mark < self.clean_power:
                price += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(price, 1)

    def calculate_washing_price(self, car: Car) -> float:
        clean_dif = self.clean_power - car.clean_mark
        rating_rate = self.average_rating / self.distance_from_city_center
        price = car.comfort_class * clean_dif * rating_rate
        return price

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        self.count_of_ratings += 1
        rate_count = self.count_of_ratings - 1
        rating = self.average_rating * rate_count
        full_rating = rating + rate
        self.average_rating = round((full_rating / self.count_of_ratings), 1)
