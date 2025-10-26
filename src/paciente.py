class paciente:
    def __init__(self, nome: str, cpf: str, ativo: bool = True):
        if not cpf.isdigit() or len(cpf) !=11:
            raise ValueError("CPF não contém digitos o suficiente (11).")
        self.nome = nome
        self.cpf = cpf
        self.ativo = ativo