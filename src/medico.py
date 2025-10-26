class medico:
    def __init__(self, nome: str, especialidade: str):
        self.nome = nome
        self.especialidade = especialidade
        self.agenda = []
    def addHorario(self, horario: str):
        if horario in self.agenda:
            raise ValueError("Horário já preenchido na agenda médica.")
        self.agenda.append(horario)
    def removerHorario(self, horario: str):
        if horario not in self.agenda:
            raise ValueError("Horário não encontrado na agenda médica.")
        self.agenda.remove(horario)
    def horarioDisp(self, horario: str) -> bool:
        return horario in self.agenda
    
