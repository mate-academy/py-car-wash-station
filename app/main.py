class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_centre = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings
    
    def serve_cars(self, cars: list) -> int:
        result = 0
        for car in cars:
            if self.wash_single_car(car):
                result += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power
        return result

    def calculate_washing_price(self, car: Car) -> int:
        var_1 = self.clean_power - car.clean_mark
        var_2 = self.average_rating / self.distance_from_city_centre
        result = round((car.comfort_class * (var_1) * var_2), 1)
        return result

    def wash_single_car(self, car: Car) -> bool:
        if car.clean_mark <= self.clean_power:
            return True

    def rate_service(self, rate: int) -> None:
        total_ratings = self.average_rating * self.count_of_ratings
        total_ratings += rate
        self.count_of_ratings += 1
        self.average_rating = round((total_ratings / self.count_of_ratings), 1)
