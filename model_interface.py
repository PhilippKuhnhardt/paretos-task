class ModelInterface:
    def __init__(self, input_parameters: dict):
        self.parameters: dict = {}
        self.valid_parameters = self.set_parameters(input_parameters)

    def calc(self) -> float:
        """In this function the logic of the model should be contained"""
        pass

    def set_parameters(self, input_parameters: dict) -> bool:
        for parameter in self.parameter_list:
            result = self.set_parameter(input_parameters, parameter)
            if(result == False):
                return False
        return True

    # Trying to convert input_parameter to float and put it into local parameter list, return true if successful, false if not successful
    def set_parameter(self, input_parameters: str, parameter_name: str) -> bool:
        if parameter_name in input_parameters:
            try:
                self.parameters[parameter_name] = float(input_parameters[parameter_name])
            except ValueError:
                return False
        else:
            return False
        return True