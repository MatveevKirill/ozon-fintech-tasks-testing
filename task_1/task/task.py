import os
import re
import typing


class Task(object):

    def __init__(self, input_file: str = None, output_file: str = None) -> None:
        """
        Инициализация задачи:
        :param input_file:  файл с данными.
        :param output_file: файл для вывода данных.
        :return: None.
        """

        # Если input файл не найден, то вызывается ошибка.
        if os.path.exists(input_file) and os.path.isfile(input_file):
            self._input_file = input_file
        else:
            raise FileNotFoundError(f"File \"{input_file}\" not found.")

        # Файл для вывода информации.
        self._output_file = output_file

        # Данные после парсинга файла.
        self._data = []

    def parse(self) -> None:
        """
        Парсинг заданного файла на массив из словарей:
            1) auth_token;
            2) request_token;
            3) function;
            4) message;
            5) user_id;
            6) user_type.
        :return: None
        """
        with open(self._input_file) as f:
            for line in f:
                self._data.append({
                    'auth_token': re.search(r'(auth_token:\"(.*?)\")', line).group(2),
                    'request_token': re.search(r'(request_token:\"(.*?)\")', line).group(2),
                    'function': re.search(r'(function:\"(.*?)\")', line).group(2),
                    'message': re.search(r'(message:\"(.*?)\")', line).group(2),
                    'user_id': re.search(r'(user_id:(\d+))', line).group(2),
                    'user_type': int(re.search(r'(user_type:(\d+))', line).group(2))
                })

    def sort(self, d: dict) -> dict:
        """
        Сортировка словаря по ключу 'count'.
        :param d: словарь для сортировки.
        :return: dict -> отсортированный словарь.
        """
        _d = list(d.items())
        _d.sort(key=lambda x: x[1]['count'])
        _d.reverse()
        return dict(_d)

    def get_statistic(self, function: str, msg_list: typing.List[str]) -> None:
        """
        Получение статистики из файла.
        :param function:
        :param msg_list:
        :return: None.
        """

        # Проверка на data != 0.
        if len(self._data) == 0:
            return None

        # Генерация списка на основе списка сообщений.
        parse_data = {m: {'count': 0, 'user_types': {}} for m in msg_list}

        # Обход массива данных для заполнения сгенерированного списка.
        for element in self._data:
            _function = element['function']
            _user_type = element['user_type']
            _message = element['message']
            _user_id = element['user_id']

            if function == element['function'] and element['message'] in msg_list:
                parse_data[_message]['count'] += 1

                if _user_type not in parse_data[_message]['user_types']:
                    parse_data[_message]['user_types'][_user_type] = {'user_id': [_user_id], 'count': 1}
                else:
                    parse_data[_message]['user_types'][_user_type]['count'] += 1
                    parse_data[_message]['user_types'][_user_type]['user_id'].append(_user_id)

        # Вывод сообщений в файл.
        with open(self._output_file, 'w') as f:
            sorted_messages = self.sort(parse_data)

            # Вывод сообщений.
            for msg in msg_list:

                # Сортировка типа пользователей.
                user_type = list(self.sort(parse_data[msg]['user_types']))[0]
                f.write(f"message \"{msg}\", count {sorted_messages[msg]['count']}, most count user type {user_type}\n")

            # Новые строки.
            f.write('\n\n')

            # Вывод user_id и message.
            for msg in msg_list:
                for user_types in list(parse_data[msg]['user_types'].items()):
                    f.write(''.join([f'{item}\t\"{msg}\"\n' for item in user_types[1]['user_id']]))
