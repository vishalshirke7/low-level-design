class Error(Exception):
    pass


class InvalidInputError(Error):
    
    def __init__(self, message, input_data):
        self.message = message
        self.input_data = input_data

    def __str__(self):
        return f'{self.message} -> {self.input_data}'


class AlreadyLoggedInError(Error):
    
    def __init__(self, message, user):
        self.message = message
        self.user = user

    def __str__(self):
        return f'{self.message} -> {self.user}'