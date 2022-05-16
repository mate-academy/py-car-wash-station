class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(
            self,
            distance_from_city_center,
            clean_power, average_rating,
            count_of_ratings
    ):

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings
        self.all_rate = average_rating * count_of_ratings

    def serve_cars(self, all_cars):
        income = 0

        for car in all_cars:
            if car.clean_mark < self.clean_power:
                print(car.clean_mark)
                income += float(self.calculate_washing_price(car))
            self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car):
        cc = car.comfort_class
        cp = self.clean_power
        cm = car.clean_mark
        ar = self.average_rating
        dfcc = self.distance_from_city_center

        return f'{(cc * (cp - cm) * ar / dfcc):.1f}'

    def wash_single_car(self, car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate):
        self.all_rate += rate
        self.count_of_ratings += 1
        self.average_rating = round(self.all_rate / self.count_of_ratings, 1)
