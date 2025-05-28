class VaccineError (Exception):
    def __init__(self, message : str = "VaccineError") -> None:
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return self.message


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Mask Error"
