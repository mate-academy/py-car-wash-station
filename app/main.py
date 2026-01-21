class Car:
    def __init__(self,
                 comfort_class,
                 clean_mark, brand):

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center,
                 clean_power,
                 average_rating,
                 count_of_ratings):

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car):
        cleanness = (self.clean_power - car.clean_mark)
        index_rd = (self.average_rating / self.distance_from_city_center)
        return round(car.comfort_class * cleanness * index_rd, 1)

    def serve_cars(self, income: list):
        result = 0
        for separate_car in income:
            if separate_car.clean_mark < self.clean_power:
                result += self.calculate_washing_price(separate_car)
                self.wash_single_car(separate_car)
        return result

    def rate_service(self, mark):
        rating = ((self.average_rating * self.count_of_ratings) + mark)
        self.average_rating = round(rating / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
        return self.average_rating, self.count_of_ratings

    def wash_single_car(self, car):
        if car.clean_mark <= self.clean_power:
            car.clean_mark = self.clean_power
        return car.clean_mark
