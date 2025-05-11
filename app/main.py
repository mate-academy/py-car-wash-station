from decimal import Decimal, ROUND_HALF_UP

class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: str, clean_power: str, average_rating: str, count_of_ratings: str) -> None:
        self.distance_from_city_center = Decimal(distance_from_city_center)
        self.clean_power = Decimal(clean_power)
        self.average_rating = Decimal(average_rating)
        self.count_of_ratings = int(count_of_ratings)

    def serve_cars(self, cars: list[Car]) -> float:
        total_price = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_price += self.wash_single_car(car)
                car.clean_mark = int(self.clean_power)
        return total_price

    def calculate_washing_price(self, car: Car) -> float:
        total_price = 0
        price = (Decimal(car.comfort_class) * (self.clean_power - Decimal(car.clean_mark)) * self.average_rating) / self.distance_from_city_center
        price = float(price.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
        total_price += price
        return total_price

    def wash_single_car(self, car: Car) -> float:
        price = (Decimal(car.comfort_class) * (self.clean_power - Decimal(car.clean_mark)) * self.average_rating) / self.distance_from_city_center
        price = float(price.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
        car.clean_mark = int(self.clean_power)
        return price

    def rate_service(self, new_rating: str) -> None:
        new = Decimal(new_rating)
        total = (self.average_rating * Decimal(self.count_of_ratings)) + new
        self.count_of_ratings += 1
        updated_average = total / Decimal(self.count_of_ratings)
        self.average_rating = float(updated_average.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
