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
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_cars: list[Car]) -> float:
        all_wash = 0

        for car in list_of_cars:
            if car.clean_mark < self.clean_power:
                all_wash += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(all_wash, 1)

    def calculate_washing_price(self, wash_car: Car) -> float:
        comfort = wash_car.comfort_class
        different_power_clean = self.clean_power - wash_car.clean_mark
        rating = self.count_of_ratings
        distance = self.distance_from_city_center

        return round((comfort * different_power_clean * rating / distance), 1)

    def wash_single_car(self, wash_car: Car):
        wash_car.clean_mark = self.clean_power

    def rate_service(self, mark: int):
        total_rate = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        new_average_rating = (total_rate + mark) / self.count_of_ratings
        self.average_rating = round(new_average_rating, 1)
