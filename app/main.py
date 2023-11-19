class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        cvs_do_it = self.clean_power - car.clean_mark
        friendly_serv = self.average_rating / self.distance_from_city_center
        coast = car.comfort_class * cvs_do_it * friendly_serv
        return round(coast, 1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        new_count_rat = self.count_of_ratings + 1
        total_score = self.average_rating * self.count_of_ratings
        new_ave_rating = (rate + total_score) / new_count_rat
        self.average_rating = round(new_ave_rating, 1)
        self.count_of_ratings = new_count_rat

    def serve_cars(self, cars: list) -> float:
        coast_cars = 0
        for car in cars:
            if self.clean_power >= car.clean_mark:
                coast_cars += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(coast_cars, 1)

    def volvo(self, car: Car, price: int) -> None:
        if car.brend == "volvo":
            coast_services = price / 2
            return coast_services
