class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str,
                 ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int,
                 ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_cars: list) -> float:
        income = 0
        for i in list_cars:
            if len(list_cars) == 1:
                income = self.wash_single_car(i)
                break
            if i.clean_mark < self.clean_power:
                income += self.calculate_washing_price(i)
                i.clean_mark = self.clean_power
        return income

    def wash_single_car(self, single_car: Car) -> object | int:
        if single_car.clean_mark < self.clean_power:
            washing_price = self.calculate_washing_price(single_car)
            single_car.clean_mark = self.clean_power
            return washing_price
        return 0

    def calculate_washing_price(self, car: Car) -> float:
        part_1 = car.comfort_class * (self.clean_power - car.clean_mark)
        part_2 = self.average_rating / self.distance_from_city_center
        total = part_1 * part_2
        return round(total, 1)

    def rate_service(self, rating_number: float) -> object:
        sum_old_points = self.average_rating * self.count_of_ratings
        sum_new_points = sum_old_points + rating_number
        self.count_of_ratings += 1
        new_average_rating = sum_new_points / self.count_of_ratings
        self.average_rating = round(new_average_rating, 1)
        return self.average_rating
