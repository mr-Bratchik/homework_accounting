from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
from tqdm import tqdm

if __name__ == '__main__':
    print(f"Текущая дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    for i in tqdm(range(10000000)):
        pass
    calculate_salary()
    get_employees()
