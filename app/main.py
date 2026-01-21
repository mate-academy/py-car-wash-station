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
                 average_rating: int,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings
        self.income = 0

    def serve_cars(self, cars_list: list) -> float:
        relevant_cars = []

        for car in cars_list:
            if self.wash_single_car(car):
                relevant_cars.append(car)

        for relevant_car in relevant_cars:
            price = self.calculate_washing_price(relevant_car)
            relevant_car.clean_mark = self.clean_power
            self.income = round(self.income + price, 1)

        return self.income

    def calculate_washing_price(self, car: Car) -> int:
        result = (car.comfort_class * (self.clean_power - car.clean_mark)
                  * (self.average_rating
                  / self.distance_from_city_center))
        return result

    def wash_single_car(self, car: Car) -> bool:
        if self.clean_power > car.clean_mark:
            return True
        else:
            return False

    def rate_service(self, number: int) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + number)
            / (self.count_of_ratings + 1), 1)
        self.count_of_ratings = self.count_of_ratings + 1
