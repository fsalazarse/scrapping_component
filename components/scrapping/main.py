from dataclasses import dataclass

@dataclass
class Scrapping:

    def main(self):
        try:
            print("Iniciando proceso de scrapping")
        except Exception as error:
            raise error
