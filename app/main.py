class Car:

    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars_list: list) -> float:
        car_washed_income = []
        for car in cars_list:
            if car.clean_mark < self.clean_power:
                car_washed_income.append(self.calculate_washing_price(car))
                self.wash_single_car(car)
        return sum(car_washed_income)

    def calculate_washing_price(self, car_instance: Car) -> float:
        income = car_instance.comfort_class * \
            (self.clean_power - car_instance.clean_mark) * \
            self.average_rating / self.distance_from_city_center
        return round(income, 1)

    def wash_single_car(self, car_instance: Car) -> None:
        if car_instance.clean_mark < self.clean_power:
            car_instance.clean_mark = self.clean_power

    def rate_service(self, single_rate: int) -> None:
        average_rating = (self.average_rating * self.count_of_ratings
                          + single_rate) / (self.count_of_ratings + 1)
        self.count_of_ratings += 1
        self.average_rating = round(average_rating, 1)
