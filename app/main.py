class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int, clean_power: int, average_rating: float, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car_list: list) -> float:
        washed_cars = [car for car in car_list if car.clean_mark < self.clean_power]
        income = 0
        for car in washed_cars:
            price = car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating
            income += price
        return round(income, 1)

    def calculate_washing_price(self, car) -> float:
        price = car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating
        return price / self.distance_from_city_center

    def wash_single_car(self, car: list) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        self.average_rating = (self.average_rating * self.count_of_ratings + rate) / (self.count_of_ratings + 1)
        self.count_of_ratings += 1
