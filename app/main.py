class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int,
                 cars: list[Car] = None) -> None:
        self.cars = cars if cars is not None else []
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car] = None) -> float:
        cars_to_serve = cars if cars is not None else self.cars
        washed_cars = []
        for car in cars_to_serve:
            if car.clean_mark < self.clean_power:
                old_clean_mark = car.clean_mark
                self.wash_single_car(car)
                washed_cars.append((car, old_clean_mark))
        return self.calculate_washing_price(washed_cars)

    def calculate_washing_price(self, washed_cars: list) -> float:
        if isinstance(washed_cars, Car):
            washed_cars = [(washed_cars, washed_cars.clean_mark)]
        elif (isinstance(washed_cars, tuple)
              and isinstance(washed_cars[0], Car)):
            washed_cars = [washed_cars]

        price = 0
        for car, old_clean_mark in washed_cars:
            price += (((car.comfort_class
                      * (self.clean_power - old_clean_mark))
                      * self.average_rating)
                      / self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car: Car) -> bool:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
            return True
        return False

    def rate_service(self, new_rating: float) -> None:
        total_rating = ((self.average_rating * self.count_of_ratings
                         + new_rating)
                        / (self.count_of_ratings + 1))
        self.count_of_ratings += 1
        self.average_rating = round(total_rating, 1)
