class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class  # Comfort class of the car (1 to 7)
        self.clean_mark = clean_mark  # Cleanliness mark (1 to 10)
        self.brand = brand  # Brand of the car


# Defining the CarWashStation class
class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center  # Distance to city center (1.0 to 10.0)
        self.clean_power = clean_power  # Maximum clean power of the station
        self.average_rating = round(average_rating, 1)  # Average rating of the station (1.0 to 5.0)
        self.count_of_ratings = count_of_ratings  # Number of ratings the station has received

    def calculate_washing_price(self, car):
        # Washing cost = comfort_class * (clean_power - clean_mark) * average_rating / distance_from_city_center
        price = (
            car.comfort_class *
            (self.clean_power - car.clean_mark) *
            self.average_rating /
            self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars):
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, new_rating):
        # Update average_rating and count_of_ratings based on the new rating
        total_rating_sum = self.average_rating * self.count_of_ratings
        total_rating_sum += new_rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating_sum / self.count_of_ratings, 1)


# Test cases
bmw = Car(3, 3, 'BMW')
audi = Car(4, 9, 'Audi')
mercedes = Car(7, 1, 'Mercedes')

ws = CarWashStation(6, 8, 3.9, 11)

# Testing income calculation and car washing
income = ws.serve_cars([bmw, audi, mercedes])

# Checking results
bmw_clean = bmw.clean_mark
audi_clean = audi.clean_mark
mercedes_clean = mercedes.clean_mark

# Testing cost calculation without washing
ford = Car(2, 1, 'Ford')
wash_cost = ws.calculate_washing_price(ford)
ford_clean = ford.clean_mark  # Should remain the same

# Testing rating system
ws.rate_service(5)
updated_ratings_count = ws.count_of_ratings
updated_average_rating = ws.average_rating

income, bmw_clean, audi_clean, mercedes_clean, wash_cost, ford_clean, updated_ratings_count, updated_average_rating
