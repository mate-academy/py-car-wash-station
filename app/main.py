class Car:
    max_comfort_class = 7
    min_comfort_class = 1
    max_clean_mark = 10
    min_clean_mark = 1

    def __init__(self, comfort_class, clean_mark, brand):
        if comfort_class > self.max_comfort_class \
                or comfort_class < self.min_comfort_class:
            raise ValueError(
                f'comfort_class value is {comfort_class},'
                f' which is out of bond({self.min_comfort_class}'
                f'...{self.max_comfort_class})')
        elif clean_mark > self.max_clean_mark\
                or clean_mark < self.min_clean_mark:
            raise ValueError(
                f"clean_mark value is {clean_mark},"
                f" which is out of bond({self.min_clean_mark}"
                f"...{self.max_clean_mark})")
        else:
            self.comfort_class = comfort_class
            self.clean_mark = clean_mark
            self.brand = brand


class CarWashStation:
    max_distance_from_center = 10.0
    min_distance_from_center = 1.0

    max_average_rating = 5.0
    min_average_rating = 1.0

    round_digits = 1

    def __init__(
            self,
            distance_from_city_center,
            clean_power,
            average_rating,
            count_of_ratings):
        if distance_from_city_center > self.max_distance_from_center or\
                distance_from_city_center < self.min_distance_from_center:
            raise ValueError(
                f'distance_from_city_center is {distance_from_city_center},'
                f' which is out of bonds{self.min_distance_from_center}'
                f'...{self.max_distance_from_center}')
        elif average_rating > self.max_average_rating or\
                average_rating < self.min_average_rating:
            raise ValueError(
                f'average_rating value is {average_rating},'
                f' which is out of bond({self.min_average_rating}'
                f'...{self.max_average_rating})')
        else:
            self.average_rating = average_rating
            self.distance_from_city_center = distance_from_city_center
            self.clean_power = clean_power
            self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars):
        result_income = 0
        for car in cars:
            result_income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return round(result_income, self.round_digits)

    def calculate_washing_price(self, car_obj):
        if self.clean_power > car_obj.clean_mark:
            result = car_obj.comfort_class \
                * (self.clean_power - car_obj.clean_mark) \
                * self.average_rating / self.distance_from_city_center
            return round(result, self.round_digits)
        else:
            return 0

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, mark):
        new_rating = self.average_rating \
            * (self.count_of_ratings / (self.count_of_ratings + 1)) \
            + mark / (self.count_of_ratings + 1)

        self.average_rating = round(new_rating, self.round_digits)
        self.count_of_ratings += 1
