class agendamento:
    def __init__(self, paciente: str, medico: str, horario: str):
        self.paciente = paciente
        self.medico = medico
        self.horario = horario
        self.status = "criado"
    def confirmarAgendamento(self):
        if not self.paciente.ativo:
            raise ValueError("O paciente informado não está ativo.")
        if not self.medico.disponivel(self.horario):
            raise ValueError("O médico solicitado não possui disponibilidade de horário.")
        self.medico.removerHorario(self.horario)
        self.status = "confirmado"
    def realizarAgendamento(self):
        if self.status != "confirmado":
            raise ValueError("Agendamento não realizado por falta de confirmação.")
        self.status = "realizado"
    def cancelarAgendamento(self):
        if self.status != "realizado":
            self.status = "cancelado"
        else:
            self.status = "realizado"