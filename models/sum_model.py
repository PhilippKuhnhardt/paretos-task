from model_interface import ModelInterface


class SumModel(ModelInterface):

    def __init__(self, input_parameters: dict):
        self.parameter_list = ["number1", "number2", "number3"]
        super().__init__(input_parameters)

    def calc(self) -> float:
        return self.parameters['number1'] + self.parameters['number2'] + self.parameters['number3']