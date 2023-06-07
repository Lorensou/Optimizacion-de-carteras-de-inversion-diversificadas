
import cvxpy as cp
import numpy as np
import pandas as pd

def frontera_eficiente(rendimientos, volatilidades):


    rendimientos = rendimientos.values
    volatilidades = volatilidades.values

# Supongamos que tienes los rendimientos y volatilidades de títulos individuales en los arrays rendimientos y volatilidades

    n = len(rendimientos)
    w = cp.Variable(n)  # Variable de los pesos de los activos
    mu = rendimientos    # Vector de rendimientos esperados
    Sigma = np.diag(volatilidades)  # Matriz de covarianza de las volatilidades

# Definir el problema de optimización
    gamma = cp.Parameter(nonneg=True)
    rendimiento_objetivo = cp.Parameter()
    prob = cp.Problem(cp.Maximize(mu @ w - gamma * cp.quad_form(w, Sigma)),
                  [cp.sum(w) == 1, w >= 0, mu @ w >= rendimiento_objetivo])

# Calcular la frontera eficiente para diferentes valores de gamma
    n_puntos = 500
    gamma_values = np.logspace(-2, 1, n_puntos)
    rendimientos_eficientes = np.zeros(n_puntos)
    volatilidades_eficientes = np.zeros(n_puntos)

    for i, gamma_value in enumerate(gamma_values):
        rendimiento_objetivo.value = np.min(mu)
        gamma.value = gamma_value
        prob.solve()
        rendimientos_eficientes[i] = cp.sum(mu @ w).value
        volatilidades_eficientes[i] = cp.sqrt(w.T @ Sigma @ w).value

    pesos_carteras_eficientes = []

# Generar carteras eficientes para diferentes valores de gamma
  
    for gamma_value in gamma_values:
        rendimiento_objetivo.value = np.min(mu)
        gamma.value = gamma_value
        prob.solve()
        indices = ['Ibex', 'S&P', 'DJ', 'NASDAQ_COMP', 'NASDAQ_100', 'FTSE', 'CAC', 'EUSTOXX', 'GDA', 'NIKKEI', 'NIFTY', 'HANGSENG']
        pesos_cartera = {str(titulo): weight for titulo, weight in zip(indices, w.value)}  #formato diccionario con los indices como key
        pesos_carteras_eficientes.append(pesos_cartera)

    
    data = {
        'Rendimiento': rendimientos_eficientes,
        'Volatilidad': volatilidades_eficientes,
        'Pesos Cartera': pesos_carteras_eficientes     #me interesa tener los pesos de cada indice
    }
    df_frontera_eficiente = pd.DataFrame(data)


    return df_frontera_eficiente    #   Que me lo devuelva masticadito




