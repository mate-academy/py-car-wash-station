class Car:
    # write your code here
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        if 0 < comfort_class <= 7:
            self.comfort_class = comfort_class
        if 0 < clean_mark <= 10:
            self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    # write your code here
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        if 0 < clean_power <= 10:
            self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars):
        clients = []
        for car in cars:
            if car.clean_mark < self.clean_power:
                clients.append(car)
        income = self.calculate_washing_price(clients)
        return income

    def calculate_washing_price(self, clients):
        income = 0
        if isinstance(clients, Car):
            diff = self.clean_power - clients.clean_mark
            income = (clients.comfort_class * diff * self.average_rating) / \
                self.distance_from_city_center
            return round(income, 1)
        else:
            for client in clients:
                diff = self.clean_power - client.clean_mark
                nom = client.comfort_class * diff * self.average_rating
                income += nom / self.distance_from_city_center
                self.set_clean_status(client)
            return round(income, 1)

    def wash_single_car(self, car: Car) -> None:
        self.set_clean_status(car)

    def rate_service(self, rate: int):
        nominator = self.average_rating * self.count_of_ratings + rate
        denominator = self.count_of_ratings + 1
        self.average_rating = round(nominator / denominator, 1)
        self.count_of_ratings += 1

    def set_clean_status(self, car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
