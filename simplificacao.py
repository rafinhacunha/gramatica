def remover_simbolos_inuteis(gram):
    # Implementação simples: remover variáveis que não derivam terminais
    úteis = set()
    for v in gram.variaveis:
        for p in gram.regras[v]:
            if all(c.islower() or c == 'ε' for c in p):
                úteis.add(v)

    alterado = True
    while alterado:
        alterado = False
        for v in gram.variaveis:
            if v not in úteis:
                for p in gram.regras[v]:
                    if all(c in úteis or c.islower() for c in p):
                        úteis.add(v)
                        alterado = True

    gram.regras = {v: p for v, p in gram.regras.items() if v in úteis}


def remover_producoes_vazias(gram):
    anulaveis = set()
    for v, ps in gram.regras.items():
        if 'ε' in ps:
            anulaveis.add(v)

    for v in list(gram.regras.keys()):
        novas = set()
        for p in gram.regras[v]:
            if any(c in anulaveis for c in p):
                for c in range(len(p)):
                    if p[c] in anulaveis:
                        nova = p[:c] + p[c+1:]
                        if nova: novas.add(nova)
        gram.regras[v].extend(list(novas))


def substituir_producoes_unitarias(gram):
    for v in list(gram.regras.keys()):
        novas = []
        for p in gram.regras[v]:
            if len(p) == 1 and p.isupper():
                novas.extend(gram.regras.get(p, []))
            else:
                novas.append(p)
        gram.regras[v] = novas
