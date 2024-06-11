class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        # Властивості авто. Приклад: bmw = Car(3, 2, 'BMW')
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
        # Відстань до центру міста
        self.distance_from_city_center = distance_from_city_center
        # Здатність до очищення
        self.clean_power = clean_power
        # Оцінка автмийки
        self.average_rating = average_rating
        # Кількість оцінок
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars):
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)

    def calculate_washing_price(self, car):
        return round((car.comfort_class
                     * (self.clean_power - car.clean_mark)
                     * self.average_rating)
                     / self.distance_from_city_center, 1)

    def wash_single_car(self, car):
        car.clean_mark = self.clean_power

    def rate_service(self, rating):
        total_rating = self.average_rating * self.count_of_ratings
        total_rating += rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)
