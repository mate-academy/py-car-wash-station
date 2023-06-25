class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) \
            -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car_item: Car) -> float:
        washing_price = car_item.comfort_class \
            * (self.clean_power - car_item.clean_mark) \
            * self.average_rating \
            / self.distance_from_city_center
        return round(washing_price, 1)

    def wash_single_car(self, car_item: Car) -> None:
        car_item.clean_mark = self.clean_power
        pass

    def rate_service(self, rating: int) -> None:
        new_average_rating = (self.average_rating * self.count_of_ratings
                              + rating) / (self.count_of_ratings + 1)
        self.average_rating = round(new_average_rating, 1)
        self.count_of_ratings += 1
        pass

    def serve_cars(self, cars_list: list) -> float:
        total_sum = 0
        for car_item in cars_list:
            if self.clean_power > car_item.clean_mark:
                total_sum += self.calculate_washing_price(car_item)
                self.wash_single_car(car_item)
        return total_sum
