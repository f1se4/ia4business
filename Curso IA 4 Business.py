#!/usr/bin/env python
# coding: utf-8

# # Optimización flujo trabajo en un almacén con Q-Learning

#%% Importar Librerias
import numpy as np

#%% ## Definición del entorno

### Definición de los estados
# Diccionario de localizaciones de letras a números
location_to_state = {
    'A':0,
    'B':1,
    'C':2,
    'D':3,
    'E':4,
    'F':5,
    'G':6,
    'H':7,
    'I':8,
    'J':9,
    'K':10,
    'L':11
}

#Definición acciones
actions = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11]

#Definición de las recompensas
#    A,B,C,D,E,F,G,H,I,J,K,L
raw_matrix = [
    [0,1,0,0,0,0,0,0,0,0,0,0], #A
    [1,0,1,0,0,1,0,0,0,0,0,0], #B
    [0,1,0,0,0,0,1,0,0,0,0,0], #C
    [0,0,0,0,0,0,0,1,0,0,0,0], #D
    [0,0,0,0,0,0,0,0,1,0,0,0], #E
    [0,1,0,0,0,0,0,0,0,1,0,0], #F
    [0,0,1,0,0,0,1,1,0,0,0,0], #G
    [0,0,0,1,0,0,1,0,0,0,0,1], #H
    [0,0,0,0,1,0,0,0,0,1,0,0], #I
    [0,0,0,0,0,1,0,0,1,0,1,0], #J
    [0,0,0,0,0,0,0,0,0,1,0,1], #K
    [0,0,0,0,0,0,0,1,0,0,1,0], #L
]
#Convertimos a array de numpy para cálculos con matrices
R = np.array(raw_matrix)

# Diccionario inverso para estados
state_to_location = {state: location for location,state in location_to_state.items()}

#%% ### Implementación del proceso de Q-Learning

def f_definir_modelo(R):
    #Hyperparametros
    gamma = 0.75
    alpha = 0.9
    # Inicialización de los valores Q
    Q = np.zeros([12,12])
    # Para cada instante t>=1 repeterimes cierto número de veces (1000 en nuestro códgio)
    for i in range(1000):
        # Seleccionar un estado aleatorio s_1 de nuestros estados posibles (12)
        current_state = np.random.randint(0,12)
        # Acción aleatoria a_t que puede conducir al next estado posible recompensa positiva
        playable_actions = []
        for j in range(R.shape[0]):
            if R[current_state, j] > 0:
                playable_actions.append(j)
        next_state = np.random.choice(playable_actions)
        # Calcular la diferencia temporal
        TD = R[current_state, next_state] + (
            gamma*Q[next_state, np.argmax(Q[next_state,:])] - Q[current_state, next_state])
        Q[current_state, next_state] = Q[current_state, next_state] + alpha*TD
    return Q


#%% Crear la función final que nos devuelva la ruta óptima
def f_route(starting_location, ending_location):
    R_new = R.copy()
    route = [starting_location]
    next_location = starting_location
    ending_state = location_to_state[ending_location]
    R_new[ending_state, ending_state] = 1000
    Q = f_definir_modelo(R_new)
    while(next_location != ending_location):
        starting_state = location_to_state[starting_location]
        next_state = np.argmax(Q[starting_state,:])
        next_location = state_to_location[next_state]
        route.append(next_location)
        starting_location = next_location
    return route

#%% Crear la función final que nos devuelva la ruta óptima pasándo por K
def route_prio(starting_location, ending_location, priorize_location):
    route1 = f_route(starting_location, priorize_location)
    route2 = f_route(priorize_location, ending_location)
    return route1[:-1] + route2
    
#%% Ejecución
print(route_prio('A','G','K'))

