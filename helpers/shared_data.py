# File for data that needs to be shared between multiple files so we dont end up with circular import errors
# Create a new function under the SharedData class and utilize where needed


class SharedData:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.bot_start_time = None
        return cls._instance

    def set_bot_start_time(self, start_time):
        self.bot_start_time = start_time

    def get_bot_start_time(self):
        return self.bot_start_time
