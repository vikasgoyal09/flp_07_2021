class InputProvider:
    def get_input(self):
        pass


class ConsoleInputProvider(InputProvider):
    def get_input(self):
        print('Enter cells like:- J,H,L,H,E,L,H,L,H,J')
        cells = input()
        print('Enter dice output:- 2, 2, 1, 4, 2, 3, 4, 1, 3, 2, 2, 7, 4, 7, 2, 4, 4, 2, 2, 2, 2')
        dice_output = input()
        print('Enter Player count')
        player_count = int(input())
        return {
            'cells': cells.split(','),
            'dice_output': map(int, dice_output.split(',')),
            'player_count': player_count
        }


class FileInputProvider(InputProvider):
    def get_input(self):
        print('Input file path')
        file_path = 'abc.csv'

        return {
            'cells': '',
            'dice_output': [],
            'player_count': 0
        }


class InputProviderFactory:
    @staticmethod
    def get_input_provider(input_type: str = None):
        if not input_type:
            return ConsoleInputProvider()
        elif input_type.lower() == 'f':
            return FileInputProvider()
        return ConsoleInputProvider()
