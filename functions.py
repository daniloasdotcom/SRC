def calcula_necessidade_de_calagem(ca, mg, k, na, hal, v1, pf):
    ctctotal = ca + mg + (k/390) + (na/230) + hal
    sb = ca + mg + (k/390) + (na/230)
    v2 = sb/ctctotal*100
    return round(((ctctotal * (v1 - v2))/100 * (pf/20)), 2)