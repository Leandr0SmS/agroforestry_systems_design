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
        
        # Calculando a área disponível
        area_disponivel = canteiro_x * canteiro_y
        print('area disponivel: ', area_disponivel)
        
        # Calculando a área que a planta pode ocupar no estrato
        estrato_disponivel = area_disponivel * (sombra / 100)
        print('estrato_disponivel: ', estrato_disponivel)
        
        # Calculando a área que a planta pode ocupar
        area_planta = (espacamento ** 2)
        print('area_planta: ', area_planta)
        
        # Verifica se a planta cabe individualmente no limite
        if area_planta > estrato_disponivel:
            continue
        
        # numero de plantas possiveis X e Y
        num_plantas_x = canteiro_x // espacamento
        print("X: ", num_plantas_x)
        
        num_plantas_y = canteiro_y // espacamento
        print("Y: ", num_plantas_y)
        
        num_plantas_possiveis = num_plantas_x * num_plantas_y
        
        # Verifica se a área total ocupada excede o limite
        if num_plantas_possiveis * area_planta > estrato_disponivel:
            num_plantas_possiveis = int(estrato_disponivel // area_planta)
            if num_plantas_possiveis == 0:
                continue
        
        print('num_plantas_possiveis: ', num_plantas_possiveis)
            
        # Calcula a posição das plantas distribuídas uniformemente
        espacamento_X = canteiro_x / num_plantas_x
        espacamento_Y = canteiro_y / num_plantas_y 
         
        # Ajusta para centralizar as plantas no plano
        offset_X = (canteiro_x - (num_plantas_x - 1) * espacamento_X) / 2
        offset_Y = (canteiro_y - (num_plantas_y - 1) * espacamento_Y) / 2
        
        ## Sobra espaco X e Y nos cantos do canteiro
        #diff_esp_x = canteiro_x % num_plantas_x
        #diff_esp_y = canteiro_x % num_plantas_y
        
        ## Valor iniciais
        #x_init = (espacamento / 2) + (diff_esp_x / 2)
        #y = (espacamento / 2) + (diff_esp_y / 2)
        
        num_planta = 0 
        for i in range(num_plantas_x):
            for j in range(num_plantas_y):
                
                x = offset_X + i * espacamento_X
                y = offset_Y + j * espacamento_Y
                canteiro[estrato].append({
                    "nome_planta": planta['nome_planta'],
                    "estrato": estrato,
                    "posicao": [x, y],
                    "diametro": espacamento,
                    "tempo_colheita": planta['tempo_colheita']
                })
                
                num_planta +=1
                print(f"planta: {num_planta}: {[x,y]}")
                
                if len(canteiro[estrato]) >= num_plantas_possiveis:
                    pass  # Retorna quando atingir o limite de quadrados

        pass
        
        #num_planta = 0  
        #for _ in range(num_plantas_y):
        #    # Iniciando x
        #    x = x_init
        #        
        #    for _ in range(num_plantas_x):
        #        
        #        num_planta +=1
        #        print(f"planta: {num_planta}: {[x,y]}")
        #        
        #        # Adicionando a planta ao estrato
        #        canteiro[estrato].append({
        #            "nome_planta": planta['nome_planta'],
        #            "estrato": estrato,
        #            "posicao": [x, y],
        #            "diametro": espacamento,
        #            "tempo_colheita": planta['tempo_colheita']
        #        })
        #        # atualizando Y
        #        x += espacamento
        #        
        #    # atualizando X
        #    y += espacamento

            
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
canteiro_x = 800
canteiro_y = 200

# Distribuindo as plantas no canteiro
plantas_distribuidas = distribuir_plantas_no_canteiro(plantas, canteiro_x, canteiro_y)

## Exibindo o resultado
#for estrato in plantas_distribuidas:
#    print(plantas_distribuidas)