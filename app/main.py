class Car:
    # write your code here
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    # write your code here
    def __init__(self,
                 distance_from_city_center,
                 clean_power,
                 average_rating,
                 count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, *args):
        new_list_of_car, = args
        sum_of_costs = 0
        for one_car in new_list_of_car:
            if one_car.clean_mark < self.clean_power:
                sum_of_costs += self.calculate_washing_price(one_car)
                self.wash_single_car(one_car)
        return round(sum_of_costs, 1)

    def calculate_washing_price(self, one_car):
        difference = self.clean_power - one_car.clean_mark
        multiplication = one_car.comfort_class * self.average_rating
        return round(
            (difference * multiplication / self.distance_from_city_center), 1)

    def wash_single_car(self, one_car):
        if one_car.clean_mark >= self.clean_power:
            return
        one_car.clean_mark = self.clean_power

    def rate_service(self, rate):
        sum_of_rating = self.average_rating * self.count_of_ratings + rate
        self.average_rating = round(
            sum_of_rating / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
