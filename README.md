# Particle Collision System

Este projeto implementa um sistema de simulação de colisão de partículas usando a biblioteca Pygame. As partículas têm a capacidade de detectar colisões com as bordas da janela e entre si. Para otimizar a detecção de colisão, foi implementado um algoritmo inspirado no Uniform Grid, dividindo as partículas em células com base no tamanho da janela. Isso permite que a detecção de colisão seja realizada apenas entre partículas que ocupam a mesma célula ou células adjacentes, reduzindo significativamente o número de comparações por quadro.

## Instalação e Execução

### Pré-requisitos

Certifique-se de ter o Python instalado. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

### Instalação das Dependências

Abra um terminal e instale a biblioteca Pygame com o seguinte comando:

```bash
pip install pygame
```

### Executando

```bash
python main.py
```

