class Gramatica:
    def __init__(self, regras):
        self.regras = self._parse_regras(regras)
        self.variaveis = list(self.regras.keys())

    def _parse_regras(self, regras):
        gramatica = {}
        for linha in regras:
            cabeca, producoes = linha.split("->")
            cabeca = cabeca.strip()
            producoes = [p.strip() for p in producoes.split("|")]
            if cabeca in gramatica:
                gramatica[cabeca].extend(producoes)
            else:
                gramatica[cabeca] = producoes
        return gramatica

    def __str__(self):
        return "\n".join(
            [f"{v} -> {' | '.join(p)}" for v, p in self.regras.items()]
        )
