class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car):
        price = (car.comfort_class
                 * (self.clean_power - car.clean_mark)
                 * self.average_rating
                 / self.distance_from_city_center)
        round_price = round(price, 1)
        return round_price

    def wash_single_car(self, car: Car):
        car.clean_mark = self.clean_power
        return car.clean_mark

    def serve_cars(self, list_of_cars: list):
        filtered_list_of_cars = [car for car in list_of_cars
                               if car.clean_mark < self.clean_power]
        list_of_prices = []
        for car in filtered_list_of_cars:
            list_of_prices.append(self.calculate_washing_price(car))
            self.wash_single_car(car)
        result = round(sum(list_of_prices), 1)
        return result

    def rate_service(self, one_rate: float):
        self.count_of_ratings += 1
        one_average_rate = ((one_rate
                             - self.average_rating)
                            / self.count_of_ratings)
        rounded_one_average_rate = round(one_average_rate, 1)

        self.average_rating = round(self.average_rating
                                    + rounded_one_average_rate, 1)
        return self.average_rating
