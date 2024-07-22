import multiprocessing


class WarehouseManager:
    def __init__(self):
        self.data = {}
        self.lock = multiprocessing.Lock()

    def process_request(self, request):
        product, action, quantity = request
        with self.lock:
            if action == "receipt":
                self.data[product] = self.data.get(product, 0) + quantity
            elif action == "shipment":
                if product in self.data and self.data[product] >= quantity:
                    self.data[product] -= quantity

    def run(self, requests):
        with multiprocessing.Pool() as pool:
            pool.map(self.process_request, requests)


if __name__ == '__main__':
    manager = WarehouseManager()  # Создаем менеджера склада

    requests = [  # Множество запросов на изменение данных о складских запасах
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    manager.run(requests)  # Запускаем обработку запросов
    print(manager.data)  # Выводим обновленные данные о складских запасах
