from services.gestion_donnees import GestionDonnees
import time
import utils.banner as bn
class Menu:
    gest = GestionDonnees()
    def banner(self):
        bn.afficher_banner()

    def afficher_menu(self):
        bn.smooth(["1-  Afficher","2-  Ajouter(En construction)","3-  Modifier(En construction)","4-  Rechercher","5-  Export","6-  Quitter"])
        time.sleep(0.5)
        choix = input(':')
        match choix:
            case '1':
                self.affichage()
            case '2':
                self.ajouter()
            case '3':
                self.modifier()
            case '4':
                self.rechercher()
            case '5':
                self.gest.get_json_file()
            case '6':
                bn.clear()
                return
            case _:
                bn.clear()
                self.afficher_menu()


    def affichage(self):
        bn.clear()
        bn.smooth(["1-  Afficher donnees valides","2-  Afficher donnees invalides","3-  Afficher un etudiant(En construction)","4-  Afficher 5 premiers donnees(En construction)","5-  Quitter"])
        choix = input(':')
        match choix:
            case '1':
                self.gest.affichage_valid()
            case '2':
                self.gest.affichage_invalid()
            case '3':
                numero = input("Entrer le numero de l'etudiant: ")
                self.gest.recherche_par_numero(numero)
            case '4':
                self.gest.affichage_cinq()
            case '5':
                bn.clear()
                return
            case _:
                bn.clear()
                self.affichage()

            
    def rechercher(self):
        bn.clear()
        bn.smooth(["1-  Numero", "2-  Code", "3-  Quitter"])
        choix = input(':')
        match choix:
            case '1':
                numero = input("Entrer le numero de l'etudiant: ")
                self.gest.recherche_par_numero(numero)
            case '2':
                code = input("Entrer le code des etudiants: ")
                self.gest.recherche_par_code(code)
            case '3':
                bn.clear()
                return
            case _:
                bn.clear()
                self.rechercher()

    def ajouter(self):
        pass

    def modifier(self):
        pass

