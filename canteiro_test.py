import math

def distribuir_plantas_no_canteiro(plantas, canteiro_x, canteiro_y):
    # Definindo o canteiro
    canteiro = {
        "emergente": [],
        "alto": [],
        "medio": [],
        "baixo": []
    }
    
    canteiro_x = int(canteiro_x)
    canteiro_y = int(canteiro_y)
    
    # Ordenando as plantas por estrato e tempo de colheita (para priorizar plantas de colheita mais rápida)
    plantas_ordenadas = sorted(plantas, key=lambda x: int(x['tempo_colheita']))
    
    # Distribuindo as plantas nos estratos
    for planta in plantas_ordenadas:
        
        print('planta: ', planta)

        sombra = int(planta['sombra'])
        espacamento = int(planta['espacamento'])
        estrato = planta['estrato']
        
        # numero de plantas possiveis X e Y
        num_plantas_x = math.floor(canteiro_x / espacamento)
        num_plantas_y = math.floor(canteiro_y / espacamento)

        if num_plantas_x > 0 and num_plantas_y > 0:
            # Sobra espaco X e Y nas bordas do canteiro
            diff_esp_x = canteiro_x % (num_plantas_x * espacamento)
            diff_esp_y = canteiro_x % (num_plantas_y * espacamento)
            print( 'diff: ', diff_esp_x, diff_esp_y)

            # Valor iniciais
            x_init = (espacamento / 2) + (diff_esp_x / 2)
            y = (espacamento / 2) + (diff_esp_y / 2)

            num_planta = 0
            for _ in range(num_plantas_y):
                # Iniciando x
                x = x_init

                for _ in range(num_plantas_x):

                    num_planta +=1
                    print(f"planta: {num_planta}: {[x,y]}")

                    # Adicionando a planta ao estrato
                    canteiro[estrato].append({
                        "nome_planta": planta['nome_planta'],
                        "estrato": estrato,
                        "posicao": [x, y],
                        "diametro": espacamento,
                        "tempo_colheita": planta['tempo_colheita']
                    })
                    # atualizando Y
                    x += espacamento

                # atualizando X
                y += espacamento
        else:
             continue
          
    return canteiro

# Dados das plantas
plantas = [
    {
        "espacamento": 200,
        "estrato": "emergente",
        "nome_planta": "Embaúba",
        "sombra": 20,
        "tempo_colheita": 1095
    },
    {
        "espacamento": 100,
        "estrato": "alto",
        "nome_planta": "Jucara",
        "sombra": 40,
        "tempo_colheita": 2555
    },
    {
        "espacamento": 50,
        "estrato": "medio",
        "nome_planta": "Pimenta-do-reino",
        "sombra": 60,
        "tempo_colheita": 1460
    },
    {
        "espacamento": 40,
        "estrato": "baixo",
        "nome_planta": "Abacaxi",
        "sombra": 80,
        "tempo_colheita": 730
    }
]

# Dimensões do canteiro
canteiro_x = 636
canteiro_y = 100

# Distribuindo as plantas no canteiro
plantas_distribuidas = distribuir_plantas_no_canteiro(plantas, canteiro_x, canteiro_y)

# Exibindo o resultado
for estrato in plantas_distribuidas:
    print(f'---Estrato: {estrato}', plantas_distribuidas[estrato])