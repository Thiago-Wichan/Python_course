from log import LogFileMixin

class Eletronic:
    def __init__(self, name):
        self._name = name
        self._state = False

    def turn_on (self):
        if not self._state:
            self._state = True

    def turn_off (self):
        if self._state:
            self._state = False

class Smartphone (Eletronic, LogFileMixin):
    def turn_on(self):
        super().turn_on()

        if self._state:
            msg = f'{self._name} is on'
            self.log_sucess(msg)
    
    def turn_off(self):
        super().turn_off()
    
        if not self._state:
            msg = f'{self._name} is off'
            self.log_error(msg)
    
