sensibilidad = 95
especificidad = 75
prevalencia = 20
def valor_predictivo_positivo(sensibilidad, especificidad, prevalencia):
    valor_pred_pos = sensibilidad*prevalencia / ((sensibilidad*prevalencia) + (1-especificidad)*(1-prevalencia))
    return valor_pred_pos*100


def valor_predictivo_negativo(sensibilidad, especificidad, prevalencia):
    valor_pred_neg = (especificidad*(1-prevalencia))/(((1-sensibilidad)*prevalencia) + (especificidad*(1-prevalencia)))
    prevalencia*especificidad / ((especificidad*prevalencia) + (1-especificidad)*(1-prevalencia))
    return valor_pred_neg*100


print(f'[1] + Valor predictivo positivo con 20% prevalencia : {valor_predictivo_positivo(95, 75, 20)}\n')
print(f'[1.2] + Valor predictivo positivo con 80% prevalencia : {valor_predictivo_positivo(95, 75, 80)}\n')
print(f'[2] + Valor predictivo negativo con 20% prevalencia: {valor_predictivo_negativo(95, 75, 20)}\n')
print(f'[2.1] + Valor predictivo negativo con 80% prevalencia: {valor_predictivo_negativo(95, 75, 80)}\n')



#kaixo alex mattie

