"""
Create class Car, its __init__ method takes and stores 3 arguments:
comfort_class - comfort class of a car, from 1 to 7
clean_mark - car cleanness mark, from very dirty - 1 to absolutely clean - 10
brand - brand of the car

Створіть клас Car (Автомобіль), його метод __init__ приймає та зберігає 3 аргументи:
comfort_class - клас комфорту автомобіля, від 1 до 7
clean_mark - оцінка чистоти автомобіля, від дуже брудного - 1 до абсолютно чистого - 10
brand - марка автомобіля
"""
class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


'''
Create class CarWashStation, its __init__ method takes and stores 4 arguments:
distance_from_city_center - how far station from the city center, from 1.0 to 10.0
clean_power - clean_mark to which this car wash station washes (yes, not all stations can clean your car completely)
average_rating - average rating of the station, from 1.0 to 5.0, rounded to 1 decimal
count_of_ratings - number of people who rated

Створіть клас CarWashStation (Автомийка), його метод __init__ приймає та зберігає 4 аргументи:
distance_from_city_center - наскільки далеко станція від центру міста, від 1.0 до 10.0
clean_power - оцінка чистоти (clean_mark), до якої миє ця автомийка (так, не всі станції можуть повністю відмити
вашу машину)
average_rating - середній рейтинг станції, від 1.0 до 5.0, округлений до 1 знака після коми
count_of_ratings - кількість людей, які оцінили
'''
class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    '''
    CarWashStation should have such methods:
    serve_cars - method, that takes a list of Car's, washes only cars with clean_mark < clean_power of wash station
    and returns income of CarWashStation for serving this list of Car's, rounded to 1 decimal:
    Клас CarWashStation повинен мати такі методи:
    serve_cars (обслужити_автомобілі) - метод, який приймає список об'єктів Car, миє лише ті автомобілі, у яких
    clean_mark < clean_power автомийки, і повертає дохід CarWashStation від обслуговування цього списку автомобілів,
    округлений до 1 знака після коми:
    '''
# Повернутися сюди та розібратися що має повертати цей метод:
    def serve_cars(self, cars: list):
        car_served = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                car_served += 1
                self.wash_single_car(self, car)
    '''
    wash_single_car - method, that washes a single car, so it should have clean_mark equals wash station's
    clean_power, if wash_station.clean_power is greater than car.clean_mark;
    wash_single_car (помити_один_автомобіль) - метод, який миє один автомобіль, тож він повинен прирівнювати
    clean_mark помитого автомобіля до clean_power автомийки, якщо wash_station.clean_power більший за
    car.clean_mark;
    '''
    def wash_single_car(self, car: Car):
        car.clean_mark = self.clean_power
    '''
    calculate_washing_price - method, that calculates cost for a single car wash, cost is calculated as:
    car's comfort class * difference between wash station's clean power and car's clean mark * car wash station
    rating / car wash station distance to the center of the city, returns number rounded to 1 decimal;
    calculate_washing_price (розрахувати_вартість_миття) - метод, який розраховує вартість миття одного
    автомобіля, вартість розраховується як: клас комфорту автомобіля * різниця між потужністю миття станції та
    оцінкою чистоти автомобіля * рейтинг автомийки / відстань автомийки до центру міста, повертає число,
    округлене до 1 знака після коми;
    '''
    def calculate_washing_price(self, car: Car):
        return round(car.comfort_class*(self.clean_power-car.clean_mark)/self.distance_from_city_center, 1)
    '''
    rate_service - method that adds a single rate to the wash station, and based on this single rate
    average_rating and count_of_ratings should be changed:
    rate_service (оцінити_сервіс) - метод, який додає одну оцінку до автомийки, і на основі цієї однієї оцінки
    повинні бути змінені average_rating (середній рейтинг) та count_of_ratings (кількість оцінок)
    '''
    def rate_service(self, rating):
        self.average_rating = (self.average_rating*self.count_of_ratings + rating) / (self.count_of_ratings+1)
        self.count_of_ratings += 1
