from abc import  ABC, abstractmethod

class Transition_state(ABC):
    """
        Clase abtracta la cual es utilizada como interfaz
        Con sus metodos abstractos para realizar la conexion entre los estados y el contexto
    """
    @abstractmethod
    def transition_init(self, machine):
        pass
    
    @abstractmethod
    def transition_scrapping(self, machine):
        pass
    
    @abstractmethod
    def transition_to_charge(self, machine):
        pass

    @abstractmethod
    def transition_charge(self, machine):
        pass

    @abstractmethod
    def transition_finish(self, machine):
        pass

    @abstractmethod
    def transition_error(self, machine):
        pass

    @abstractmethod
    def transition_aborted(self, machine):
        pass
    