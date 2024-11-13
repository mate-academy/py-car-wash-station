class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        if self.distance_from_city_center != 0:
            comfort_clss = car.comfort_class
            difference_clean = self.clean_power - car.clean_mark
            wash_station_rating = self.average_rating
            distance_to_the_center = self.distance_from_city_center
            price = (comfort_clss * difference_clean
                     * (wash_station_rating / distance_to_the_center))
            return round(price, 1)
        return 0.0

    def serve_cars(self, cars_list: list) -> float:
        calculating_car = []
        for car in cars_list:
            if car.clean_mark < self.clean_power:
                calculating_car.append(self.calculate_washing_price(car))
                self.wash_single_car(car)
        return sum(calculating_car)

    def wash_single_car(self, car: Car) -> Car:
        car.clean_mark = self.clean_power
        return car

    def rate_service(self, rating: int) -> float:
        last_rating = self.average_rating * self.count_of_ratings
        rating_new = round((last_rating + rating)
                           / (self.count_of_ratings + 1), 1)
        self.average_rating = rating_new
        self.count_of_ratings = self.count_of_ratings + 1
        return rating_new
