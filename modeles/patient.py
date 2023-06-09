from modeles.personne import Personne
from untils.date import nowtostr
import json

class Patient(Personne):
    def __init__(self, id, nom, prenom, sexe, date_naissance, group_sanguin, created_at=nowtostr(), updated_at=nowtostr()) -> None:

        Personne.__init__(self, id, nom, prenom, sexe, created_at, updated_at)

        self.date_naissance = date_naissance
        self.group_sanguin = group_sanguin

        self.consultations = list()

    def __str__(self):
        return "{}".format(json.dumps(self.__dict__, indent=4))