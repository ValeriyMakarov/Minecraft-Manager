import argparse


class Arguments:
    """Отвечает за настройку парсера."""
    __instance = None

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
        alternative_remove_group = self.parser.add_mutually_exclusive_group()
        alternative_transfer_group = self.parser.add_mutually_exclusive_group()

        alternative_transfer_group.add_argument(
            '-c', '--copy', '/c',
            action='store_true', dest='copy',
            help='Копирует содержимое'
        )
        alternative_remove_group.add_argument(
            '-d', '--delete', '/d',
            action='store_true', dest='delete',
            help='Очищает папку'
        )
        self.parser.add_argument(
            '-p', '--press', '/p',
            action='store_true', dest='press',
            help='Создаёт архив из содержимого'
        )
        self.parser.add_argument(
            '-h', '--help', '/h',
            action="help", help='Выводит этот текст и выходит'
        )
        alternative_remove_group.add_argument(
            '-r', '--remove', '/r',
            action='store_true', dest='remove',
            help='Удаляет содержимое папки'
        )
        alternative_transfer_group.add_argument(
            '-s', '--swap', '/s',
            action='store_true', dest='swap',
            help='Меняет содержимое папки'
        )

    def get(self) -> argparse.Namespace:
        """Возвращает пространство имён с ключами."""
        return self.parser.parse_args()