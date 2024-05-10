from dataclasses import dataclass
from states.scrapping import Scrapping_state
from utils.utis import Console_Message
from interface.interface import Transition_state

@dataclass
class Init_state(Transition_state):
    """
        La maquina de estado en un estado inicial purede transicionar a todos los estados menos al "INIT"
    """
    _console_message  = Console_Message()

    def transition_init(self, machine):   
        print("El sistema ya se encuentra en estado Init")
    
    def transition_scrapping(self, machine):
        try:
           self._console_message.transition_message("scrapping") #Mensaje de transicion de estado
           machine._state = Scrapping_state() #Cambio el estado de la maquina a scrapping

        except Exception as error:
            raise error
    
    def transition_to_charge(self, machine):
        pass

    def transition_charge(self, machine):
        pass

    def transition_finish(self, machine):
        pass

    def transition_error(self, machine):
        pass

    def transition_aborted(self, machine):
        pass
    