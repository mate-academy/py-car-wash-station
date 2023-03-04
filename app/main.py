class Car:

    def __init__(self,
                 comfort_class: int,
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

    def calculate_washing_price(self, other: Car) -> float:
        cost = (other.comfort_class
                * (self.clean_power - other.clean_mark)
                * self.average_rating
                / self.distance_from_city_center)
        return round(cost, 1)

    def wash_single_car(self, other: Car) -> None:
        other.clean_mark = self.clean_power

    def rate_service(self, other: int) -> None:
        final_rate = ((self.average_rating * self.count_of_ratings + other)
                      / (self.count_of_ratings + 1))
        self.average_rating = round(final_rate, 1)
        self.count_of_ratings = self.count_of_ratings + 1

    def serve_cars(self, other: Car) -> list:
        my_list = []
        for car in other:
            if car.clean_mark < self.clean_power:
                my_list.append(self.calculate_washing_price(car))
                self.wash_single_car(car)
        return sum(my_list)
