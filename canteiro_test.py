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
        
        ## numero de plantas possiveis X e Y
        #num_plantas_x = canteiro_x // espacamento
        #print("X: ", num_plantas_x)
        #
        #num_plantas_y = canteiro_y // espacamento
        #print("Y: ", num_plantas_y)
        #
        #num_plantas_possiveis = num_plantas_x * num_plantas_y
        #
        ## Verifica se a área total ocupada excede o limite
        #if num_plantas_possiveis * area_planta > estrato_disponivel:
        #    num_plantas_possiveis = int(estrato_disponivel // area_planta)
        #    if num_plantas_possiveis == 0:
        #        continue
        #
        #print('num_plantas_possiveis: ', num_plantas_possiveis)
        #    
        ## Calcula a posição das plantas distribuídas uniformemente
        #espacamento_X = canteiro_x / num_plantas_x
        #espacamento_Y = canteiro_y / num_plantas_y 
        # 
        ## Ajusta para centralizar as plantas no plano
        #offset_X = (canteiro_x - (num_plantas_x - 1) * espacamento_X) / 2
        #offset_Y = (canteiro_y - (num_plantas_y - 1) * espacamento_Y) / 2
        
        num_plantas_possiveis = int(estrato_disponivel // area_planta)
        if num_plantas_possiveis == 0:
            continue
        
        print('numero plantas possiveis:', num_plantas_possiveis)
        
        num_plantas_y = 1
        num_plantas_x = num_plantas_possiveis
        espacamento_x = canteiro_x // (num_plantas_x + 1)
        espacamento_y = canteiro_y // (num_plantas_y + 1)
        
        print(f"espacamentoX: {espacamento_x}, espacamentoY: {espacamento_y}")
        print(f'num_plantas_x: {num_plantas_x}, num_plantas_y: {num_plantas_y}')
          
        count = 0  
        while espacamento_x < espacamento:
            num_plantas_x = num_plantas_possiveis
            if espacamento_y < espacamento:
                continue
            num_plantas_y += 1
            num_plantas_x /= num_plantas_y
            espacamento_x = int(canteiro_x // (num_plantas_x + 1))
            espacamento_y = int(canteiro_y // (num_plantas_y + 1))
        print(f"espacamentoX: {espacamento_x}, espacamentoY: {espacamento_y}")
        print(f'num_plantas_x: {num_plantas_x}, num_plantas_y: {num_plantas_y}')
        
        num_plantas_x = int(num_plantas_x)
        num_plantas_y = int(num_plantas_y)

        # Ajusta o offset para centrar as plantas no canteiro
        offset_x = (canteiro_x / num_plantas_x) // 2
        offset_y = (canteiro_y / num_plantas_y) // 2
        
        x = offset_x
        y = offset_y
        
        num_planta = 0 
        for i in range(num_plantas_y):
            for j in range(num_plantas_x):
                
                canteiro[estrato].append({
                    "nome_planta": planta['nome_planta'],
                    "estrato": estrato,
                    "posicao": [x, y],
                    "diametro": espacamento,
                    "tempo_colheita": planta['tempo_colheita']
                })
                
                num_planta +=1
                print(f"planta: {num_planta}: {[x,y]}")
                
                x += espacamento_x
                
                #if len(canteiro[estrato]) >= num_plantas_possiveis:
                #    continue  # Retorna quando atingir o limite de plantas
            
            y += espacamento_y
        
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


print(len(str(plantas_distribuidas)))