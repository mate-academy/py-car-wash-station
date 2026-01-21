class Car:
    def __init__(self, comfort_class, clean_mark, brand):

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car):

        if car.clean_mark >= self.clean_power:
            return 0.0

        price = (car.comfort_class *
                 (self.clean_power - car.clean_mark) *
                 self.average_rating /
                 self.distance_from_city_center)

        return round(price, 1)

    def wash_single_car(self, car):

        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
            return True
        return False

    def serve_cars(self, cars):

        total_income = 0.0

        for car in cars:
            if car.clean_mark < self.clean_power:
                # Calculate price before washing (while car is still dirty)
                price = self.calculate_washing_price(car)
                total_income += price

                # Now wash the car
                self.wash_single_car(car)

        return round(total_income, 1)

    def rate_service(self, new_rating):

        # Calculate new average: (old_avg * old_count + new_rating) / new_count
        total_points = self.average_rating * self.count_of_ratings
        total_points += new_rating
        self.count_of_ratings += 1
        self.average_rating = round(total_points / self.count_of_ratings, 1)
