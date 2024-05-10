from contexts.context import Scrapp_Machine

#✅: implementado, 🚫: no implementado
#********************************************************
#(🚫)Implementar loggging para identificar en que proceso se encuentra el scrapping
#(🚫)Implementar un log de errores del sistema completo

def main():

    play = Scrapp_Machine() #Instanciamos la maquina de estados la cual inicia con el esto INIT

    status_message = "scrapp" #Dato dammy para realizar los cambios de estado del registros
    if status_message == "scrapp":
         try:
              
              play.state_scrapping()
              play.state_to_charge()
         except Exception as error:
              print("Error in scrapp: ", error)


if __name__ == "__main__":
     main()