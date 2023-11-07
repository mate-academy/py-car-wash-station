class Car:
    # write your code here
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    # write your code here
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        # print(cars)
        # print(car for car in cars if car.clean_mark < self.clean_power)
        # return [car for car in cars if car.clean_mark < self.clean_power]
    def calculate_washing_price(self, car_washing: Car) -> float:
        num = car_washing.comfort_class * (self.clean_power - car_washing.clean_mark) * self.average_rating
        de_num = self.distance_from_city_center
        return round(num / de_num, 1)











