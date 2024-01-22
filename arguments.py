import argparse


class Arguments:
    """Отвечает за настройку парсера."""
    __instance = None
    __descriptions = {
        'subparser_info': 'Доступные команды',
        'ls': 'Выводит список имён',
        'get': 'Создаёт новое имя, копируя содержимое из указанной папки',
        'move': 'Управляет именами и содержимым папки',
        'help': 'Выводит этот текст и выходит',
        'delete': 'Очищает папку',
        'remove': 'Удаляет содержимое папки',
        'copy': 'Копирует содержимое',
        'swap': 'Меняет содержимое папки',
        'press': 'Создаёт архив из содержимого',
        'path': 'Путь к папке из которой нужно взять сборку',
        'name': 'Новое имя'
    }

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description=
            """
            Используй:  -s -p чтобы поменять содержимое и добавить его в архив;
                        -c -r чтобы переместить и удалить содержимое;
                        -d чтобы очистить папку.
            Существует две альтернативные группы ключей:
                    "alternative remove group": -d, -r
                    (удалить всё, удалить содержимое);
                    "alternative transfer group": -c, -s
                    (копировать, поменять содержимое).
            Ключ -p указывает на то, нужно ли создавать архив.
            """,
            prefix_chars='-/',
            add_help=False
        )
        subparsers = self.parser.add_subparsers(
            dest='command', help=self.__descriptions['subparser_info']
        )

        command_ls = subparsers.add_parser(
            name='ls', description=self.__descriptions['ls'],
            help=self.__descriptions['ls'],
            prefix_chars='-/', add_help=False
        )
        command_ls.add_argument(
            '-h', '--help', '/h',
            action="help", help=self.__descriptions['help']
        )

        command_get = subparsers.add_parser(
            name='get', description=self.__descriptions['get'],
            help=self.__descriptions['get'],
            prefix_chars='-/', add_help=False
        )
        command_get.add_argument(
            dest='path', action='store',
            help=self.__descriptions['path']
        )
        command_get.add_argument(
            dest='name', action='store',
            help=self.__descriptions['name']
        )
        command_get.add_argument(
            '-h', '--help', '/h',
            action="help", help=self.__descriptions['help']
        )

        subparsers.add_parser(
            name='move', description=self.__descriptions['move'],
            help=self.__descriptions['move'],
            prefix_chars='-/', add_help=False
        )

        alternative_remove_group = self.parser.add_mutually_exclusive_group()
        alternative_transfer_group = self.parser.add_mutually_exclusive_group()

        alternative_transfer_group.add_argument(
            '-c', '--copy', '/c',
            action='store_true', dest='copy',
            help=self.__descriptions['copy']
        )
        alternative_remove_group.add_argument(
            '-d', '--delete', '/d',
            action='store_true', dest='delete',
            help=self.__descriptions['delete']
        )
        self.parser.add_argument(
            '-p', '--press', '/p',
            action='store_true', dest='press',
            help=self.__descriptions['press']
        )
        self.parser.add_argument(
            '-h', '--help', '/h',
            action="help", help=self.__descriptions['help']
        )
        alternative_remove_group.add_argument(
            '-r', '--remove', '/r',
            action='store_true', dest='remove',
            help=self.__descriptions['remove']
        )
        alternative_transfer_group.add_argument(
            '-s', '--swap', '/s',
            action='store_true', dest='swap',
            help=self.__descriptions['swap']
        )

    def get(self) -> argparse.Namespace:
        """Возвращает пространство имён с ключами."""
        return self.parser.parse_args(['-h'])

print(Arguments().get())