import os

from task import Task

# Пути указываются относительно директории task_1.
task = Task(os.path.join('.', 'data', 'input.txt'), os.path.join('.', 'data', 'output.txt'))

# Запускаем парсинг файла input.txt
task.parse()

# Получаем статистику по функции MakePayment для собщений Validation error, AntiFraud, Unkown (Почему не Unknown?) user.
task.get_statistic("MakePayment", ["Validation error", "AntiFraud", "Unkown user"])
