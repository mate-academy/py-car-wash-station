class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float,
                 count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars_list: list) -> float:
        total_price = 0
        for car in cars_list:
            if car.clean_mark < self.clean_power:
                income_from_washing_single_car = self.calculate_washing_price(car)
                total_price += income_from_washing_single_car
                self.wash_single_car(car)
        return total_price

    def calculate_washing_price(self, instance: Car) -> float:
        price = instance.comfort_class * (
                self.clean_power - instance.clean_mark) * self.count_of_ratings / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, instance: Car):
        instance.clean_mark = self.clean_power

    def rate_service(self, num: int) -> None:
        sum_of_marks = self.count_of_ratings * self.average_rating
        self.count_of_ratings += 1
        new_rating = (sum_of_marks + num) / self.count_of_ratings
        self.average_rating = round(new_rating, 1)
