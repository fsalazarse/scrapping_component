from dataclasses import dataclass
from interface.interface import Transition_state
from components.scrapping.main import Scrapping

@dataclass
class Scrapping_state(Transition_state):

    _scrapping_process = Scrapping()
    
    def transition_init(self, machine):
        pass
    
    def transition_scrapping(self, machine):
        print("No es posible trancisionar al estado scrapping")
    
    def transition_to_charge(self, machine):
        self._scrapping_process.main()

    def transition_charge(self, machine):
        pass

    def transition_finish(self, machine):
        pass

    def transition_error(self, machine):
        pass

    def transition_aborted(self, machine):
        pass
    