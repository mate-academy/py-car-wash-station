class Car:
    def __init__(self, 
                 comfort_class: int, 
                 clean_mark: int, 
                 brand: str) -> None:
        self.comfort_class = self.limitation(comfort_class, 1, 7)
        self.clean_mark = self.limitation(clean_mark, 1, 10)
        self.brand = brand
    
    def limitation(self, value: int, min_value: int, max_value: int) -> int:
        return max(min(value, max_value), min_value)


class CarWashStation:
    def __init__(self, 
                 distance_from_city_center: 
                 float, clean_power: int,
                 average_rating: float, 
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = self.limitation(distance_from_city_center, 1.0, 10.0)
        self.clean_power = self.limitation(clean_power, 1, 10)
        self.average_rating = round(self.limitation(average_rating, 1.0, 5.0), 1)
        self.count_of_ratings = count_of_ratings
    
    def limitation(self, value: int, min_value: int, max_value: int) -> int:
        return max(min(value, max_value), min_value)

    def serve_cars(self, cars: list) -> float:
        income = 0
        for index, car in enumerate(cars):
            if self.clean_power > car.clean_mark:
                income += self.calculate_washing_price(cars[index])
                self.wash_single_car(cars[index])
        return income

    def calculate_washing_price(self, car: Car) -> float:
        return round(car.comfort_class * (self.clean_power - car.clean_mark)
                     * self.average_rating / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        self.average_rating = round((self.average_rating
                                     * self.count_of_ratings + rate)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
