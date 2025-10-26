import pytest
from src.agendamento import agendamento


class PacienteFake:
    def __init__(self, nome, ativo=True):
        self.nome = nome
        self.ativo = ativo


class MedicoFake:
    def __init__(self, nome):
        self.nome = nome
        self.horarios = ["2025-10-26 09:00"]

    def disponivel(self, horario):
        return horario in self.horarios

    def removerHorario(self, horario):
        if horario not in self.horarios:
            raise ValueError("Horário inexistente.")
        self.horarios.remove(horario)


@pytest.fixture
def setup_base():
    paciente = PacienteFake("João", ativo=True)
    medico = MedicoFake("Dra. Paula")
    ag = agendamento(paciente, medico, "2025-10-26 09:00")
    return ag, paciente, medico


def test_confirmar_agendamento_valido(setup_base):
    ag, paciente, medico = setup_base
    ag.confirmarAgendamento()
    assert ag.status == "confirmado"
    assert "2025-10-26 09:00" not in medico.horarios


def test_confirmar_paciente_inativo(setup_base):
    ag, paciente, medico = setup_base
    paciente.ativo = False
    with pytest.raises(ValueError):
        ag.confirmarAgendamento()


def test_confirmar_medico_indisponivel(setup_base):
    ag, paciente, medico = setup_base
    medico.horarios = []
    with pytest.raises(ValueError):
        ag.confirmarAgendamento()


def test_realizar_sem_confirmacao(setup_base):
    ag, paciente, medico = setup_base
    with pytest.raises(ValueError):
        ag.realizarAgendamento()


def test_realizar_agendamento_apos_confirmar(setup_base):
    ag, paciente, medico = setup_base
    ag.confirmarAgendamento()
    ag.realizarAgendamento()
    assert ag.status == "realizado"


def test_cancelar_agendamento_confirmado(setup_base):
    ag, paciente, medico = setup_base
    ag.confirmarAgendamento()
    ag.cancelarAgendamento()
    assert ag.status == "cancelado"


def test_cancelar_agendamento_realizado(setup_base):
    ag, paciente, medico = setup_base
    ag.confirmarAgendamento()
    ag.realizarAgendamento()
    ag.cancelarAgendamento()
    assert ag.status == "realizado"
