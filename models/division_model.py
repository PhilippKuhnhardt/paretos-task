from model_interface import ModelInterface


class DivisionModel(ModelInterface):

    def __init__(self):
        self.parameter_list = ["number1", "number2"]
        super().__init__()

    def calc(self) -> float:
        return self.parameters['number1'] / self.parameters['number2']