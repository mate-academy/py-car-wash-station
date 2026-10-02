class Car:
    def __init__(comfort_class, clean_mark, brand: list) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(distance_from_city_center, clean_power, average_rating, count_of_ratings: list) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(cars: str) -> None:
        income = 0

        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return income
        
    def calculate_washing_price(car: str) -> None:
        return (comfort_class * (clean_power - clean_mark) * rating / distance)

    def wash_single_car(self, car):
        car.clean_mark = self.clean_power

    def rate_service(self, rating):
        total_rating = (
            self.average_rating * self.count_of_ratings + rating
        )
        self.count_of_ratings += 1
        self.average_rating = total_rating / self.count_of_ratings
