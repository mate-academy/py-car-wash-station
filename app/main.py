class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance,
        clean_power,
        average_rating,
        count_of_ratings
    ):
        self.distance = distance
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars):
        income = 0

        for car in cars:
            price = self.calculate_washing_price(car)

            if price > 0:
                income += price
                self.wash_single_car(car)

        return round(income, 1)

    def calculate_washing_price(self, car):
        if car.clean_mark >= self.clean_power:
            return 0

        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance
        )

        return round(price, 1)

    def wash_single_car(self, car):
        car.clean_mark = self.clean_power

    def rate_service(self, mark):
        total_rating = (
            self.average_rating * self.count_of_ratings
            + mark
        )

        self.count_of_ratings += 1

        self.average_rating = round(
            total_rating / self.count_of_ratings,
            1
        )