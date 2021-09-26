# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 17:30:13 2021

# IA 4 Business - Minimizing Costs
# Parte Entorno (Caso de Uso)

@author: f1se4
"""
#import libraries
import numpy as np


# CONSTRUIR EL ENTORNO EN UNA CLASE

class Environtment(object):
   
    # INTRODUCIR E INICIALIZAR LOS PARAMETROS Y VARIABLES DE ENTORNO
    def __init__(self, 
                 optimal_temperature=(18.0,24.0), 
                 initial_month = 0, 
                 initial_users = 10, 
                 initial_rate_data = 60):
        self.monthly_atmospheric_temperature = [1.0, 5.0, 7.0, 
                                                10.0, 11.0, 20.0, 
                                                23.0, 24.0, 22.0, 
                                                10.0 , 5.0, 1.0]
        self.initial_month = initial_month
        self.initial_users = initial_users
        self.atmospheric_temperature = self.monthly_atmospheric_temperature[initial_month]
        self.optimal_temperature = optimal_temperature
        self.min_temperature = -20
        self.max_temperature = 80
        self.min_number_users = 10
        self.max_number_users = 100
        self.max_update_users = 5
        self.current_users = initial_users
        self.initial_rate_data = initial_rate_data
        self.current_rate_data = initial_rate_data
        
        # Objetos a ajustar
        self.intrinsec_temperature = ( self.atmospheric_temperature + 
                                       1.25*self.current_users + 
                                       1.25*self.current_rate_data )
        self.temperature_ai = self.intrinsec_temperature
        self.temperature_noai = ( self.optimal_temperature[0] + self.optimal_temperature[1]) / 2.0
        self.total_energy_ai = 0.0
        self.total_energy_noai = 0.0
        
        # Variables útiles
        self.reward = 0.0
        self.game_over = 0  # 0 no end, 1 end
        self.train = 1      # 1 train - 0 explotation
        pass    
    
    # ACTUALIZAR ENTORNO DESPUÉS DE LA EJECUCIÓN ACCIÓN
    
    
    # REINICIAR ENTORNO
    
    
    # GET STATUS, REWARD, GAME-OVER PARA UN INSTANTE t