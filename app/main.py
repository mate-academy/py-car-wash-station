class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars):
        total_income = 0  # Renamed from income to total_income
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)

    def calculate_washing_price(self, car):
        # Calculate cost based on the given formula
        return round(car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating / self.distance_from_city_center, 1)

    def wash_single_car(self, car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rating):
        # Update the average rating and the count of ratings based on new rating
        total_ratings = self.average_rating * self.count_of_ratings
        total_ratings += rating
        self.count_of_ratings += 1
        self.average_rating = round(total_ratings / self.count_of_ratings, 1)

# Example usage:
bmw = Car(3, 3, 'BMW')
audi = Car(4, 9, 'Audi')
mercedes = Car(7, 1, 'Mercedes')

ws = CarWashStation(6, 8, 3.9, 11)

# Serve cars and calculate income
income = ws.serve_cars([bmw, audi, mercedes])
print(income)  # 41.7

# Check cleaned cars' clean marks
print(bmw.clean_mark)  # 8
print(audi.clean_mark)  # 9
print(mercedes.clean_mark)  # 8

# Calculate the wash price for a new car
ford = Car(2, 1, 'Ford')
wash_cost = ws.calculate_washing_price(ford)
print(wash_cost)  # 9.1
print(ford.clean_mark)  # 1

# Rate the service
ws.rate_service(5)

print(ws.count_of_ratings)  # 12
print(ws.average_rating)  # 4.0
