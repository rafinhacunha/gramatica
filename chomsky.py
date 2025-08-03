def para_chomsky(gram):
    novas_regras = {}
    contador = 1

    def novo_simbolo():
        nonlocal contador
        simb = f"X{contador}"
        contador += 1
        return simb

    for v, ps in gram.regras.items():
        novas = []
        for p in ps:
            if len(p) == 1 and p.islower():
                novas.append(p)
            else:
                while any(c.islower() for c in p):
                    for i, c in enumerate(p):
                        if c.islower():
                            novo = novo_simbolo()
                            novas_regras[novo] = [c]
                            p = p[:i] + novo + p[i+1:]
                            break
                while len(p) > 2:
                    novo = novo_simbolo()
                    novas_regras[novo] = [p[:2]]
                    p = novo + p[2:]
                novas.append(p)
        novas_regras[v] = novas
    gram.regras = novas_regras
