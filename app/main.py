class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int,
                 clean_power: int,
                 average_rating: int,
                 count_of_ratings: int
                 ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car: str) -> list:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
        return car.clean_mark

    def serve_cars(self, cars_list: list) -> float:
        result_price_lst = []
        for car in cars_list:
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                self.wash_single_car(car)
                result_price_lst.append(price)
        return round(sum(result_price_lst), 1)

    def calculate_washing_price(self, car: str) -> float:
        price_wash_car = car.comfort_class *\
            (self.clean_power - car.clean_mark) *\
            self.average_rating / self.distance_from_city_center
        return price_wash_car

    def rate_service(self, rate: int) -> tuple:
        result_rate = ((self.average_rating * self.count_of_ratings)
                       + rate) / (self.count_of_ratings + 1)
        self.average_rating = round(result_rate, 1)
        self.count_of_ratings += 1
        return self.average_rating, self.count_of_ratings
