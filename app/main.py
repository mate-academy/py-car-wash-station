class Car:
    MAX_COMFORT_CLASS = 7
    MIN_COMFORT_CLASS = 1
    MAX_CLEAN_MARK = 10
    MIN_CLEAN_MARK = 1

    def __init__(self, comfort_class, clean_mark, brand):
        if comfort_class > self.MAX_COMFORT_CLASS \
                or comfort_class < self.MIN_COMFORT_CLASS:
            raise ValueError(
                f"comfort_class value is {comfort_class},"
                f" which is out of bounds({self.MIN_COMFORT_CLASS}"
                f"...{self.MAX_COMFORT_CLASS})")
        elif clean_mark > self.MAX_CLEAN_MARK\
                or clean_mark < self.MIN_CLEAN_MARK:
            raise ValueError(
                f"clean_mark value is {clean_mark},"
                f" which is out of bounds({self.MIN_CLEAN_MARK}"
                f"...{self.MAX_CLEAN_MARK})")
        else:
            self.comfort_class = comfort_class
            self.clean_mark = clean_mark
            self.brand = brand


class CarWashStation:
    MAX_DISTANCE_FROM_CENTER = 10.0
    MIN_DISTANCE_FROM_CENTER = 1.0

    MAX_AVERAGE_RATING = 5.0
    MIN_AVERAGE_RATING = 1.0

    ROUND_DIGITS = 1

    def __init__(
            self,
            distance_from_city_center,
            clean_power,
            average_rating,
            count_of_ratings):
        if distance_from_city_center > self.MAX_DISTANCE_FROM_CENTER or\
                distance_from_city_center < self.MIN_DISTANCE_FROM_CENTER:
            raise ValueError(
                f"distance_from_city_center is {distance_from_city_center},"
                f" which is out of bounds{self.MIN_DISTANCE_FROM_CENTER}"
                f"...{self.MAX_DISTANCE_FROM_CENTER}")
        elif average_rating > self.MAX_AVERAGE_RATING or\
                average_rating < self.MIN_AVERAGE_RATING:
            raise ValueError(
                f"average_rating value is {average_rating},"
                f" which is out of bounds({self.MIN_AVERAGE_RATING}"
                f"...{self.MAX_AVERAGE_RATING})")
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
        return round(result_income, self.ROUND_DIGITS)

    def calculate_washing_price(self, car_obj):
        if self.clean_power > car_obj.clean_mark:
            result = car_obj.comfort_class \
                * (self.clean_power - car_obj.clean_mark) \
                * self.average_rating / self.distance_from_city_center
            return round(result, self.ROUND_DIGITS)
        else:
            return 0

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, mark):
        new_rating = self.average_rating \
            * (self.count_of_ratings / (self.count_of_ratings + 1)) \
            + mark / (self.count_of_ratings + 1)

        self.average_rating = round(new_rating, self.ROUND_DIGITS)
        self.count_of_ratings += 1


