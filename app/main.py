class Car:
    def __int__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __int__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_car: list):
        result = 0
        for car in list_of_car:
            if car.clean_mark < self.clean_power:
                result += self.calculate_washing_price(car)
        return result
    
    def calculate_washing_price(self, car: Car):
        result = (
                car.comfort_class
                * (self.clean_power - car.clean_mark)
                * self.average_rating
                / self.distance_from_city_center
        )
        return round(result, 1)


    def wash_single_car(self):
        """
        - метод, который моет одну машину,
         поэтому у него clean_mark должен быть равен clean_power мойки,
         если wash_station.clean_power больше car.clean_mark;
        :return:
        """

    def rate_service(self):
        """
        метод, добавляющий одну ставку к станции мойки,
         и на основе этой одной ставки следует изменить medium_rating и count_of_ratings:
        :return:
        """
        return

