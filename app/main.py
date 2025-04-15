class Car:
    def __init__(self, comfort_class, clean_mark, brand) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings
                ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings


    def serve_cars(self, cars: list) -> float:
        cars_to_wash = [car for car in cars if car.clean_mark < self.clean_power]
        income = sum([self.wash_single_car(car) for car in cars_to_wash])
        return income


    def calculate_washing_price(self, car: Car) -> float:
        return round(car.comfort_class * (self.clean_power - car.clean_mark) * (self.average_rating / self.distance_from_city_center), 1)


    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            result = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return result
        return 0


    def rate_service(self, rate: float) -> None:
        new_rating = (self.average_rating * self.count_of_ratings) + rate
        self.count_of_ratings += 1
        self.average_rating = round(new_rating / self.count_of_ratings, 1)
