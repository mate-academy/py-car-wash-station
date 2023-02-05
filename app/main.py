class Car:

    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        self.car = Car
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.wash_station = CarWashStation
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0.0
        for el in cars:
            print(f"Before: {el.clean_mark}")
            if self.clean_power > el.clean_mark:
                income += self.calculate_washing_price(el)
                self.wash_single_car(el)
                print(f"Income func: {self.calculate_washing_price(el)}")
                print(el.clean_mark)
                print(f"Income: {income}")
        print(f"Before: {round(income * (-1), 1)}")
        print()
        income = round(income * (-1), 1)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        number = 0.0

        ccc = car.comfort_class
        ccm = car.clean_mark
        scp = self.clean_power
        sar = self.average_rating
        sdfcc = self.distance_from_city_center
        number = (ccc * (ccm - scp) * sar) / sdfcc

        return number

    def wash_single_car(self, car: Car) -> None:

        if self.clean_power >= car.clean_mark:
            car.clean_mark = self.clean_power

        return car.clean_mark

    def rate_service(self, rate: int) -> None:
        temp = self.count_of_ratings
        self.count_of_ratings += 1
        temp = round((((self.average_rating * temp)
                       + rate) / self.count_of_ratings), 1)
        self.average_rating = temp
