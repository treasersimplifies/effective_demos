# rule no.17


class ReadVisits(object):

    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


# rule no.25 use super to initialize father class


class Father(object):

    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


class SonOlder(Father):

    def __init__(self, value):
        super().__init__(value)   # super() instead of Father


# rule no.27 modify private attributes


class Dota(object):

    def __init__(self, verison):
        self.version = verison
        self._agency = "Perfect World"
        self.__company = "VALUE"

    def get_company(self):
        return self.__company