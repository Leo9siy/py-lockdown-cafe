class VaccineError (Exception):
    def __init__(self, message : str = "VaccineError") -> None:
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Mask Error"
