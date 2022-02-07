class ModelInterface:
    def set_parameters(self, input_parameters: dict) -> bool:
        """Checks if input parameters are valid"""
        pass

    def calc(self) -> float:
        """Calculated solution"""
        pass