class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int, clean_power: int,
                 average_rating: float, count_of_rating: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_rating

    def serve_cars(self, cars_list: list) -> int | float:
        result = 0
        for car in cars_list:
            print(type(car))
            if car.clean_mark < self.clean_power:
                result += CarWashStation.calculate_washing_price(self, car)
                CarWashStation.wash_single_car(self, car)
            else:
                pass
        return result

    def calculate_washing_price(self, car: Car) -> float:
        return round((car.comfort_class * (self.clean_power - car.clean_mark)
                      * (self.average_rating
                         / self.distance_from_city_center)
                      ), 1)

    def wash_single_car(self, car_info: type) -> None:
        if car_info.clean_mark < self.clean_power:
            car_info.clean_mark = self.clean_power

    def rate_service(self, new_value: int) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + new_value)
            / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
