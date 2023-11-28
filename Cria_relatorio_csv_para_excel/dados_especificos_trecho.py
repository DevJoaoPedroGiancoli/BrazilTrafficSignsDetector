# Dados especificos do trecho para base de cálculos
# Carregar o arquivo Excel existente
rota = "ERS-122"
sentido_especifico = "decrescente"
km_inicial = 77
km_final = 122
nomenclatura_escpecifica =  {0: 'A-10b', 1: 'A-11b', 2: 'A-12', 3: 'A-13a', 4: 'A-13b'
                   , 5: 'A-14', 6: 'A-15', 7: 'A-18', 8: 'A-1a', 9: 'A-1b'
                   , 10: 'A-20a', 11: 'A-20b', 12: 'A-21c', 13: 'A-21d'
                   , 14: 'A-21e', 15: 'A-22', 16: 'A-24', 17: 'A-27'
                   , 18: 'A-28', 19: 'A-2a', 20: 'A-2b', 21: 'A-31', 22: 'A-32a'
                   , 23: 'A-32b', 24: 'A-33a', 25: 'A-33b', 26: 'A-3a', 27: 'A-3b'
                   , 28: 'A-42a', 29: 'A-42b', 30: 'A-4a', 31: 'A-4b', 32: 'A-52',
                   33: 'A-5a', 34: 'A-5b', 35: 'A-6', 36: 'A-7a', 37: 'A-7b', 38: 'A-8'
                   , 39: 'Del', 40: 'E-5', 41: 'ESP-20', 42: 'I-4', 43: 'LOC-6', 44: 'MO'
                   , 45: 'MP', 46: 'R-1', 47: 'R-15', 48: 'R-19', 49: 'R-2', 50: 'R-24a',
                   51: 'R-24b', 52: 'R-26', 53: 'R-27', 54: 'R-28', 55: 'R-33', 56: 'R-43',
                   57: 'R-4a', 58: 'R-4b', 59: 'R-5a', 60: 'R-6a', 61: 'R-6b', 62: 'R-6c', 
                   63: 'R-7', 64: 'RQ', 65: 'S-14', 66: 'TUR-4', 67: 'de'}

intervalo_km_dict = {i: km_inicial + i - 1 for i in range(1, km_final - km_inicial + 2)}
print("Dados especificos importados..")