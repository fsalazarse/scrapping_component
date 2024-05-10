class Console_Message:

   def transition_message(self, state):
    """Mensaje por consola que indica el estado  al cual transiciona la maquina"""
    try:
        print("*" * 60)
        print(f"   El sistema ha cambiando al estado: {state}")
        print("*" * 60)
    except Exception as error:
        raise error