class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: int,
        clean_power: int,
        average_rating: int,
        count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car: dir, is_served: bool = True) -> int:
        income_from_curr_car = 0

        wash_diff = self.clean_power - car.clean_mark
        if wash_diff > 0:
            income_from_curr_car += (
                (car.comfort_class * wash_diff * self.average_rating)
                / self.distance_from_city_center
            )
            if is_served:
                car.clean_mark = self.clean_power

        return round(income_from_curr_car, 1)

    def serve_cars(self, cars_list: list) -> int:
        overall_income = 0

        for car in cars_list:
            overall_income += self.wash_single_car(car)

        return round(overall_income, 1)

    def calculate_washing_price(self, car: dir) -> int:
        return self.wash_single_car(car, False)

    def rate_service(self, new_mark: int) -> None:
        prev_mark_sum = self.average_rating * self.count_of_ratings
        new_count_of_ratings = self.count_of_ratings + 1
        new_average_rating = round(
            (prev_mark_sum + new_mark) / new_count_of_ratings, 1
        )
        self.count_of_ratings = new_count_of_ratings
        self.average_rating = new_average_rating
