def fatorar_esquerda(gram):
    novas_regras = {}
    for v, ps in gram.regras.items():
        prefixos = {}
        for p in ps:
            chave = p[0]
            prefixos.setdefault(chave, []).append(p)
        novas = []
        for k, grup in prefixos.items():
            if len(grup) > 1:
                novo = v + "'"
                novas_regras[novo] = [g[1:] if len(g) > 1 else 'ε' for g in grup]
                novas.append(k + novo)
            else:
                novas.append(grup[0])
        novas_regras[v] = novas
    gram.regras = novas_regras


def remover_recursao_esquerda(gram):
    novas_regras = {}
    for v, ps in gram.regras.items():
        rec = [p[1:] for p in ps if p.startswith(v)]
        nrec = [p for p in ps if not p.startswith(v)]
        if rec:
            novo = v + "'"
            novas_regras[v] = [p + novo for p in nrec]
            novas_regras[novo] = [p + novo for p in rec] + ['ε']
        else:
            novas_regras[v] = ps
    gram.regras = novas_regras
