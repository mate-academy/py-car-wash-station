class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_centre: float,
                 clean_power: int, average_rating: float, count_of_ratings: int):
        self.distance_from_city_centre = distance_from_city_centre
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars):
        total_amount = 0
        for car in cars:
            if car.clean_mark <= self.clean_power:
                total_amount += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return round(total_amount, 1)

    def calculate_washing_price(self, car):
        price = car.comfort_class * (self.clean_power - car.clean_mark)
        price = price * self.average_rating / self.distance_from_city_centre
        return round(price, 1)

    def wash_single_car(self, car):
        if car.clean_mark > self.clean_power:
            return f"{car.brand} no cleaning because clean_power is low"
        car.clean_mark = self.clean_power
        return f"Cars washed and now {car.clean_mark}"

    def rate_service(self, rate):
        average_rate = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        average_rate = (average_rate + rate) / self.count_of_ratings
        self.average_rating = round(average_rate, 1)
