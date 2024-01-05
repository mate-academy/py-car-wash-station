class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: int,
                 count_of_ratings: int
                 ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars_list: list) -> float:
        result = 0
        for car in cars_list:
            if car.clean_mark < self.clean_power:
                result += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return result

    def calculate_washing_price(self, car: Car) -> float:
        different = self.clean_power - car.clean_mark
        rate_to_dist = self.average_rating / self.distance_from_city_center
        price = car.comfort_class * different * rate_to_dist
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        total_rate = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        new_rate = round((total_rate + rate) / self.count_of_ratings, 1)
        self.average_rating = new_rate
