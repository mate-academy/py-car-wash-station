class Car:
    """Class add new car which want to make wash!"""

    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power,
                 average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars):
        cars_nums = 0
        for car in cars:
            if car.clean_mark <= self.clean_power:
                cars_nums += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(cars_nums, 1)

    def calculate_washing_price(self, cars):
        a = cars.comfort_class * (self.clean_power - cars.clean_mark)
        income = a * self.average_rating / self.distance_from_city_center

        return round(income, 1)

    def wash_single_car(self, car):
        if car.clean_mark > self.clean_power:
            return f"{car.brand} wasn't washed"

        car.clean_mark = self.clean_power
        return f"all other cars are washed to {car.clean_mark}"

    def rate_service(self, mark):
        average = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        new_average = (average + mark) / self.count_of_ratings
        self.average_rating = round(new_average, 1)

        return round(new_average, 1)
