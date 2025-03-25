def calcular_centros_quadrados(eixo_X, eixo_Y, lado_quadrado, porcentagem_max):
    """
    Calcula as coordenadas (x, y) dos centros dos quadrados distribuídos uniformemente
    e centralizados no plano X, Y, respeitando um limite máximo de ocupação.

    Parâmetros:
        eixo_X (int): Comprimento do eixo X da área total.
        eixo_Y (int): Comprimento do eixo Y da área total.
        lado_quadrado (int): Lado do quadrado que se deseja posicionar na área.
        porcentagem_max (float): Porcentagem máxima de ocupação permitida (0 a 100).

    Retorna:
        list: Lista de tuplas (x, y) com as coordenadas dos centros dos quadrados.
              Retorna lista vazia se não for possível posicionar nenhum quadrado.
    """
    # Validação da porcentagem
    if not 0 <= porcentagem_max <= 100:
        raise ValueError("A porcentagem deve estar entre 0 e 100.")

    # Calcula a área total e o limite de área ocupável
    area_total = eixo_X * eixo_Y
    limite_area = (porcentagem_max / 100) * area_total
    area_quadrado = lado_quadrado ** 2

    # Verifica se o quadrado cabe individualmente no limite
    if area_quadrado > limite_area:
        return []  # Não cabe nenhum quadrado

    # Calcula quantos quadrados cabem em X e Y
    quadrados_X = eixo_X // lado_quadrado
    quadrados_Y = eixo_Y // lado_quadrado
    total_quadrados = quadrados_X * quadrados_Y

    # Verifica se a área total ocupada excede o limite
    if total_quadrados * area_quadrado > limite_area:
        total_quadrados = int(limite_area // area_quadrado)
        if total_quadrados == 0:
            return []  # Não cabe nenhum quadrado
        
    print(area_quadrado)
    print(limite_area)
    print(total_quadrados)

    # Calcula os centros dos quadrados distribuídos uniformemente e centralizados
    centros = []
    espacamento_X = eixo_X / quadrados_X
    espacamento_Y = eixo_Y / quadrados_Y

    # Ajusta para centralizar os quadrados no plano
    offset_X = (eixo_X - (quadrados_X - 1) * espacamento_X) / 2
    offset_Y = (eixo_Y - (quadrados_Y - 1) * espacamento_Y) / 2

    for i in range(quadrados_X):
        for j in range(quadrados_Y):
            x = offset_X + i * espacamento_X
            y = offset_Y + j * espacamento_Y
            centros.append([x, y])
            if len(centros) >= total_quadrados:
                return centros  # Retorna quando atingir o limite de quadrados

    return centros

# Exemplo de uso:
eixo_X = 800
eixo_Y = 200
lado_quadrado = 40
porcentagem_max = 80

centros = calcular_centros_quadrados(eixo_X, eixo_Y, lado_quadrado, porcentagem_max)
print("Coordenadas dos centros dos quadrados:")
for centro in centros:
    print(centro)