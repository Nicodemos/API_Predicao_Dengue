import pickle as pk
from sklearn.preprocessing import StandardScaler
import numpy as np
class inferencia:
    def __init__(self,nome):
        self.nome_modelo = nome+'.pkl'
        #self.nome_padronizador_y = 'xgboost_normalizay.pkl'
        with open('modelos_para_uso/'+self.nome_modelo, 'rb') as f:
            self.modelo = pk.load(f)

    def start_ml(self,dados):
        _array = np.array(dados).reshape(1,-1)
        resultado = self.modelo.predict(_array)
        return resultado
