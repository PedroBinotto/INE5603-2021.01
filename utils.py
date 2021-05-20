def cria_matriz(n_lin, n_col, valor):
    m = []
    for i in range(n_lin):
        m.append([valor] * n_col)
    return m
