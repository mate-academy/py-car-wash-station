class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center : float, clean_power: int, average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    '''Create a method to provide a service of  car washing and calculate income from all cars(stored through Car class)
        that we washed'''
    def serve_cars(self, car : list[Car]) -> float:
        income = 0
        for car_class in car:
            if car_class.clean_mark > self.clean_power:
                continue
            else:
                income += self.calculate_washing_price(car_class) # no formula in README so asking GPT
                self.wash_single_car(car_class)
        return round(income, 1)

    '''Create a method to calculate washing price for a single car(stored through Car class)'''
    def calculate_washing_price(self, car : Car) -> float:
        washing_price = (car.comfort_class * (self.clean_power - car.clean_mark)
                         * self.average_rating / self.distance_from_city_center)
        return round(washing_price, 1)

    '''Create a one car wash method, and we just change parameter clean_mark in Car'''
    def wash_single_car(self, car : Car) -> int:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power #we don't return result, just apply data inside class method,
        return car.clean_mark                                      # so maybe will need to rewrite this method after

    '''Change rating of our WAsh station after client ratings'''
    def rate_service(self, client_rating : float) -> tuple[float, int]:
        self.count_of_ratings += 1
        self.average_rating = (self.average_rating + client_rating) / self.count_of_ratings
        return self.average_rating, self.count_of_ratings