from model_interface import ModelInterface


class DivisionModel(ModelInterface):

    def __init__(self):
        self.parameters: dict = {}

    def set_parameters(self, input_parameters: dict) -> bool:
        if 'number1' in input_parameters:
            try:
                self.parameters['number1'] = float(input_parameters['number1'])
            except ValueError:
                return False
        else:
            return False

        if 'number2' in input_parameters:
            try:
                self.parameters['number2'] = float(input_parameters['number2'])
            except ValueError:
                return False
        else:
            return False

        return True

    def calc(self) -> float:
        return self.parameters['number1'] / self.parameters['number2']