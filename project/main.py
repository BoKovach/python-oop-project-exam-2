from project.managing_app import ManagingApp
from project.user import User

# user = User('Tong', 'B0', '1930')

user_manage = ManagingApp()

print(user_manage.register_user('Tong', 'Bo', '1234'))
print(user_manage.register_user('Jonh', 'Jones', '1234'))

print(user_manage.upload_vehicle('PassengerCar', 'Jiguli', '1200', '1930'))
print(user_manage.upload_vehicle('PassengerCar', 'Chrysler', '200C', '1930'))
print(user_manage.upload_vehicle('PassengerCar', 'Chrysler', '200C', '1730'))

