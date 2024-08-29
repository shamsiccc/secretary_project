from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees
import requests

if __name__ == '__main__':
    print("Текущая дата:", datetime.today())
    calculate_salary()
    get_employees()
    response = requests.get("https://netology.ru")
    print(f"Статус ответа: {response.status_code}")
