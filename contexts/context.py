from dataclasses import dataclass
from states.init import Init_state


@dataclass
class Scrapp_Machine:
    
    _state = Init_state() #Estado inicial del sistema

    """
        Todos los estados que tiene la maquina abtrayendose de su implementacion
    """

    def state_init(self):
        try:
            self._state.transition_init(self)
        except Exception as error:
            raise error

    def state_scrapping(self):
        try:
            self._state.transition_scrapping(self)
        except Exception as error:
            raise error

    def state_to_charge(self):
        try:
            self._state.transition_to_charge(self)
        except Exception as error:
            raise error

    def state_charge(self):
        try:
            self._state.transition_charge(self)
        except Exception as error:
            raise error

    def state_finish(self):
        try:
            self._state.transition_finish(self)
        except Exception as error:
            raise error

    def state_error(self):
        try:
            self._state.transition_error(self)
        except Exception as error:
            raise error

    def state_aborted(self):
        try:
            self._state.transition_aborted(self)
        except Exception as error:
            raise error