class Car:
    def __init__(self, cft_clss: str, clean_mark: str, brand: str) -> None:
        self.comfort_class = cft_clss
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, dist_ctr: int, cl_pwr: int, avg_rtg: int,
                 cnt_rtgs: int) -> None:
        self.distance_from_city_center = dist_ctr
        self.clean_power = cl_pwr
        self.average_rating = avg_rtg
        self.count_of_ratings = cnt_rtgs

    def serve_cars(self, cars: tuple) -> callable:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: str) -> callable:
        return round(car.comfort_class
                     * (self.clean_power - car.clean_mark)
                     * self.average_rating / self.distance_from_city_center, 1)

    def wash_single_car(self, car: str) -> callable:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> callable:
        self.count_of_ratings += 1
        self.average_rating = round(((self.average_rating
                                      * (self.count_of_ratings - 1))
                                     + rating) / self.count_of_ratings, 1)
