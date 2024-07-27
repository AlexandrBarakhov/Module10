import threading
import time
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Cafe:
    def __init__(self, tables):
        self.queue = Queue()
        self.tables = tables
        self.customer_count = 1
        self.print_lock = threading.Lock()  # Лок для синхронизации вывода

    def customer_arrival(self):
        # Моделирует приход посетителей (каждую секунду).
        while self.customer_count <= 20:  # Ограничение на 20 посетителей
            time.sleep(1)  # Новый посетитель каждую секунду
            customer = threading.Thread(target=self.serve_customer, args=(self.customer_count,))
            customer.start()
            self.customer_count += 1

    def serve_customer(self, customer_id):
        # Моделирует обслуживание посетителя.
        with self.print_lock:
            print(f"Посетитель номер {customer_id} прибыл")
        if any(table.is_busy == False for table in self.tables):
            for table in self.tables:
                if not table.is_busy:
                    table.is_busy = True
                    with self.print_lock:
                        print(f"Посетитель номер {customer_id} сел за стол {table.number}")
                    time.sleep(5)  # Время обслуживания 5 секунд
                    table.is_busy = False
                    with self.print_lock:
                        print(f"Посетитель номер {customer_id} покушал и ушёл.")
                    break
        else:
            with self.print_lock:
                print(f"Посетитель номер {customer_id} ожидает свободный стол.")
            self.queue.put(customer_id)
            while True:
                if any(table.is_busy == False for table in self.tables):
                    for table in self.tables:
                        if not table.is_busy:
                            table.is_busy = True
                            customer_id = self.queue.get()
                            with self.print_lock:
                                print(f"Посетитель номер {customer_id} сел за стол {table.number}")
                            time.sleep(5)
                            table.is_busy = False
                            with self.print_lock:
                                print(f"Посетитель номер {customer_id} покушал и ушёл.")
                            break
                    break


if __name__ == "__main__":
    # Создаем столики в кафе
    table1 = Table(1)
    table2 = Table(2)
    table3 = Table(3)
    tables = [table1, table2, table3]

    # Инициализируем кафе
    cafe = Cafe(tables)

    # Запускаем поток для прибытия посетителей
    customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
    customer_arrival_thread.start()

    # Ожидаем завершения работы прибытия посетителей
    customer_arrival_thread.join()
