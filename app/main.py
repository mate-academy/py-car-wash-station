class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings
    def calculate_washing_price(self, cars: Car):
        total_diff = self.clean_power - cars.clean_mark
        if total_diff <= 0:
            return 0
        pricewash = cars.comfort_class * total_diff * self.average_rating / self.distance_from_city_center
        return round(pricewash, 1)

    def wash_single_car(self, cars: Car):
        if self.clean_power > cars.clean_mark:
            cars.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]):
        total_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                pricewash = self.calculate_washing_price(car)
                total_income += pricewash
                self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, rate: int):
        total_rate = self.average_rating * self.count_of_ratings
        total_rate += rate
        self.count_of_ratings += 1
        self.average_rating = round(total_rate / self.count_of_ratings, 1)

