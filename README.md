# Particle Collision System

Simulação de colisão de partículas em tempo real, construída com Python e Pygame. O sistema simula partículas simultaneamente, detectando colisões entre si e com as bordas da janela de forma eficiente através de uma **uniform grid** de particionamento espacial.

[https://github.com/dbseitenfus/particle-collision-system/assets/20246441/8d3e12ff-e1fe-47b1-a78e-fef5f09ca1bc](https://github.com/dbseitenfus/particle-collision-system/assets/20246441/8d3e12ff-e1fe-47b1-a78e-fef5f09ca1bc)

[https://github.com/dbseitenfus/particle-collision-system/assets/20246441/30dc19e9-644c-413a-ba82-c72cf4912d87](https://github.com/dbseitenfus/particle-collision-system/assets/20246441/30dc19e9-644c-413a-ba82-c72cf4912d87)

---

## Funcionalidades

- Simulação de 7.000 partículas em tempo real
- Colisões entre partículas com reflexão
- Reflexão nas bordas da janela
- Detecção de colisão otimizada com uniform grid (particionamento espacial)
- Prevenção de sobreposição entre partículas

---

## Como Funciona

### Uniform Grid (Particionamento Espacial)

A janela de 700×700 px é dividida em células de 10×10 px, formando uma grade de 70×70 células. Cada partícula é alocada na célula correspondente à sua posição. A detecção de colisão ocorre apenas entre partículas da **mesma célula**, reduzindo a complexidade de O(n²) para próximo de O(n).

### Física das Colisões

Ao detectar colisão entre duas partículas, o sistema:

1. Calcula o vetor normal (linha entre os centros)
2. Calcula o vetor tangente (perpendicular ao normal)
3. Projeta as velocidades nesses eixos
4. Troca as componentes normais (colisão elástica)
5. Reposiciona as partículas para evitar sobreposição

### Loop de Simulação (por frame)

```text
Limpar grid → Desenhar partículas → Atualizar posições →
Alocar na grid → Detectar colisões → Refletir nas bordas
```

---

## Estrutura do Projeto

```text
particle-collision-system/
├── main.py               # Ponto de entrada, loop principal e criação das partículas
├── Particle.py           # Classe Particle com física e detecção de colisão
└── particles_manager.py  # Classe ParticlesManager com a uniform grid
```

---

## Instalação e Execução

### Pré-requisitos

- Python 3.x — [python.org](https://www.python.org/downloads/)

### Instalação

```bash
pip install pygame
```

### Executando

```bash
python main.py
```

**Controles:** `ESC` ou fechar a janela para encerrar.

---

## Configuração

Os principais parâmetros estão em [main.py](main.py):


| Parâmetro            | Valor padrão | Descrição                       |
| -------------------- | ------------ | ------------------------------- |
| `WIDTH`, `HEIGHT`    | `700, 700`   | Dimensões da janela             |
| `grid_size`          | `10`         | Tamanho da célula da grade (px) |
| Número de partículas | `7000`       | Quantidade total de partículas  |
| `speed`              | `3`          | Velocidade de movimento         |
| `radius`             | `1`          | Raio das partículas             |
| FPS                  | `30`         | Taxa de quadros alvo            |


