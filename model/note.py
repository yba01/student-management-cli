class Note:
    def __init__(self, matiere, devoirs, exam):
        self.matiere = matiere
        self.devoirs = devoirs
        self.exam = exam
        self.valid = True

    def to_dict(self):
        return self.__dict__
    
    def __str__(self):
        return f"matiere: {self.matiere} devoirs: {self.devoirs}, examen: {self.exam}"

    def mean(self):
        if self.valid:
            return round(((sum(self.devoirs)/len(self.devoirs) + 2*self.exam)/3), 2)