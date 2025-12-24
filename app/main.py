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

    def serve_cars(self, cars: list) -> float:
        income = []

        for car in cars:
            if car.clean_mark < self.clean_power:
                car_wash_price = self.calculate_washing_price(car)
                income.append(car_wash_price)

                self.wash_single_car(car)

        income_sum = sum(income)
        rounded_income_sum = round(income_sum, 1)

        return rounded_income_sum

    def calculate_washing_price(self, car: Car) -> float:
        # method, that calculates cost for a single car wash,
        # cost is calculated as:
        # car's comfort class * difference between wash station's clean power
        # and car's clean mark
        # * car wash station rating / car wash station distance
        # to the center of the city, returns number rounded to 1 decimal;
        car_comfort_class = car.comfort_class
        power_and_mark_difference = self.clean_power - car.clean_mark
        wash_station_rating = self.average_rating
        wash_station_distance = self.distance_from_city_center

        washing_price = (
            car_comfort_class
            * power_and_mark_difference
            * wash_station_rating
            / wash_station_distance
        )

        rounded_washing_price = round(washing_price, 1)

        return rounded_washing_price

    def wash_single_car(self, car: Car) -> None:
        # it should have clean_mark equals wash station's clean_power,
        # if wash_station.clean_power is greater than car.clean_mark
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        ratings_sum = self.average_rating * self.count_of_ratings
        new_ratings_sum = ratings_sum + rate
        new_ratings_count = self.count_of_ratings + 1
        new_average_rating = new_ratings_sum / new_ratings_count
        rounded_new_average_rating = round(new_average_rating, 1)

        self.count_of_ratings = new_ratings_count
        self.average_rating = rounded_new_average_rating
