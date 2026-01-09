class Validators:

    @staticmethod
    def check_for_empty_string(value, message):
        if not value.strip():
            raise ValueError(message)
        return True

    @staticmethod
    def check_if_value_lt_zero(value, message):
        if value <= 0:
            raise ValueError(message)
        return True