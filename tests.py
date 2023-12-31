import mcmanager
import unittest

STYLE_RESET, STYLE_SUCCESS = '\033[0m', '\033[32m'


def info(msg: str):
    print(f'{STYLE_SUCCESS}{msg}')


class MinecraftManager(unittest.TestCase):
    def tearDown(self) -> None:
        print(STYLE_RESET)

    # Модульные тесты
    def test_args_parser_from_str(self):
        command, keys, name, path = mcmanager.parse_args('mcmanager ap move gregtech')

        self.assertTrue(isinstance(command, str),
                        msg=f'Тип данных должен быть str. Текущий тип: {type(command)}.')
        self.assertTrue(command == 'move',
                        msg=f'Имя команды должно быть "move". Текущее имя: "{command}".')
        info(f'Имя команды верное.')

        self.assertTrue(isinstance(keys, set),
                        msg=f'Тип данных должен быть set. Текущий тип: {type(keys)}.')
        self.assertTrue(all(isinstance(i, str) for i in keys),
                        msg=f'Тип данных в наборе ключей должен быть str. Текущий набор: {keys}.')
        self.assertTrue(keys == {'a', 'p'},
                        msg=f"Набор ключей должен равняться {{'a','p'}}. Текущий набор: {keys}.")
        info(f'Набор ключей верный.')

        self.assertTrue(isinstance(name, str),
                        msg=f'Тип данных должен быть str. Текущий тип: {type(name)}.')
        self.assertTrue(command == 'move',
                        msg=f'Имя команды должно быть "gregtech". Текущее имя: "{name}".')
        info(f'Имя команды равно.')

        self.assertIsNone(path, msg=f'Переменная path должна содержать None.')
        info(f'Переменнная path содержит None.')


if __name__ == '__main__':
    unittest.main()
