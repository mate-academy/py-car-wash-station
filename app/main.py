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
                 clean_power: int,  # compared with Car(clean_mark)
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car_list: list) -> float:
        income = 0
        for car in car_list:
            if self.clean_power > car.clean_mark:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        result = round((car.comfort_class * (
            self.clean_power - car.clean_mark) * (
            self.average_rating / self.distance_from_city_center)),
            1)
        return result

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, single_rate: int) -> None:
        if single_rate:
            self.average_rating = round((((
                self.average_rating * self.count_of_ratings)
                + single_rate)
                / (self.count_of_ratings + 1)), 1)
            self.count_of_ratings += 1
        return
