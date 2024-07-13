from time import sleep, time
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


start_time_functions = time()  # Начало работы функций

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

end_time_functions = time()  # Конец работы функций
print(f"Работа функций {end_time_functions - start_time_functions:.6f}")

start_time_threads = time()  # Начало работы потоков

threads = [
    Thread(target=write_words, args=(10, "example5.txt")),
    Thread(target=write_words, args=(30, "example6.txt")),
    Thread(target=write_words, args=(200, "example7.txt")),
    Thread(target=write_words, args=(100, "example8.txt"))
]

for thread in threads:  # Запускаем каждый поток
    thread.start()

for thread in threads:  # Ожидаем завершения каждого потока
    thread.join()

end_time_threads = time()  # Конец работы потоков
print(f"Работа потоков {end_time_threads - start_time_threads:.6f}")
