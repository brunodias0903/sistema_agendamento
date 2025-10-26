import pytest
from src.medico import medico


@pytest.fixture
def setup_medico():
    m = medico("Dra. Ana", "Cardiologia")
    return m


def test_criar_medico(setup_medico):
    m = setup_medico
    assert m.nome == "Dra. Ana"
    assert m.especialidade == "Cardiologia"
    assert m.agenda == []


def test_adicionar_horario_valido(setup_medico):
    m = setup_medico
    m.addHorario("2025-10-27 09:00")
    assert "2025-10-27 09:00" in m.agenda


def test_nao_permitir_horario_duplicado(setup_medico):
    m = setup_medico
    m.addHorario("2025-10-27 10:00")
    with pytest.raises(ValueError):
        m.addHorario("2025-10-27 10:00")


def test_remover_horario_existente(setup_medico):
    m = setup_medico
    m.addHorario("2025-10-27 11:00")
    m.removerHorario("2025-10-27 11:00")
    assert "2025-10-27 11:00" not in m.agenda


def test_remover_horario_inexistente(setup_medico):
    m = setup_medico
    with pytest.raises(ValueError):
        m.removerHorario("2025-10-28 08:00")


def test_verificar_horario_disponivel(setup_medico):
    m = setup_medico
    m.addHorario("2025-10-27 13:00")
    assert m.horarioDisp("2025-10-27 13:00") is True
    assert m.horarioDisp("2025-10-27 14:00") is False
