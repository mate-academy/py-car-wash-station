class Car:

    def __init__(self, comfort_class, clean_mark, brand):
        self,comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

class CarWashStation:
    # write your code here
    # pass
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

        def serve_cars(sef, cars):
            income = 0.0
            for car in cars:
                if car.clean_mark < self.clean_power:
                    wash_price = round(car.comfort_class * self.average_rating / self. distance_from_city_center, 1)
                    income += wash_price
                    car.clean_mark = self.clean_power
            return  round(income, 1)
