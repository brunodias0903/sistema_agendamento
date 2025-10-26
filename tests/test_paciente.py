import pytest
from src.paciente import paciente


def test_criar_paciente_valido():
    p = paciente("Maria", "12345678901")
    assert p.nome == "Maria"
    assert p.cpf == "12345678901"
    assert p.ativo is True


def test_criar_paciente_inativo():
    p = paciente("João", "98765432100", ativo=False)
    assert p.nome == "João"
    assert p.ativo is False


def test_cpf_com_letras():
    with pytest.raises(ValueError):
        paciente("Carlos", "abc45678901")


def test_cpf_curto():
    with pytest.raises(ValueError):
        paciente("Ana", "12345")


def test_cpf_longo():
    with pytest.raises(ValueError):
        paciente("Pedro", "1234567890123")
