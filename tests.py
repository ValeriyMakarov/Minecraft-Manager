import unittest

import mcmanager
from mcmanager import InvalidCountOfArgumentsError
from mcmanager import InvalidCommandError

STYLE_RESET, STYLE_SUCCESS = '\033[0m', '\033[32m'


def info(msg: str):
    print(f'{STYLE_SUCCESS}{msg}')


class MinecraftManager(unittest.TestCase):
    def tearDown(self) -> None:
        print(STYLE_RESET)
    # проверить все ошибки (негативные)
    # проверить все рабочие комбинации
    # Модульные тесты
    def testa(self):
        with self.assertRaises(InvalidCommandError) as e:
            mcmanager.parse_args('')
        print(e.exception)
        self.assertEqual(
            str(e.exception),
            "Неверная команда. Список команд: ['get', 'help', 'ls', 'move'].")
        ...

    def test_args_parser_from_str(self):
        command, keys, name, path = mcmanager.parse_args(
            'mcmanager ap move gregtech'
        )

        self.assertTrue(isinstance(command, str),
                        msg=(
                            f'Тип данных должен быть str. '
                            f'Текущий тип: {type(command)}.')
                        )
        self.assertTrue(command == 'move',
                        msg=(
                            f'Имя команды должно быть "move". '
                            f'Текущее имя: "{command}".')
                        )
        info(f'Имя команды верное.')

        self.assertTrue(isinstance(keys, set),
                        msg=(
                            f'Тип данных должен быть set. '
                            f'Текущий тип: {type(keys)}.')
                        )
        self.assertTrue(all(isinstance(i, str) for i in keys),
                        msg=(
                            f'Тип данных в наборе ключей должен быть str. '
                            f'Текущий набор: {keys}.')
                        )
        self.assertTrue(keys == {'a', 'p'},
                        msg=(
                            f"Набор ключей должен равняться {{'a','p'}}. "
                            f"Текущий набор: {keys}.")
                        )
        info(f'Набор ключей верный.')

        self.assertTrue(isinstance(name, str),
                        msg=(
                            f'Тип данных должен быть str. '
                            f'Текущий тип: {type(name)}.')
                        )
        self.assertTrue(command == 'move',
                        msg=(
                            f'Имя команды должно быть "gregtech". '
                            f'Текущее имя: "{name}".')
                        )
        info(f'Имя команды равно.')

        self.assertIsNone(path, msg=f'Переменная path должна содержать None.')
        info(f'Переменнная path содержит None.')


if __name__ == '__main__':
    unittest.main()
