# Pac-Man: Way of the Katana ⚔️

Este projeto consiste na implementação do algoritmo de **Simulated Annealing (Têmpera Simulada)** para o agente Pac-Man, desenvolvido como parte da disciplina **MATA64 – Inteligência Artificial**.

## 🎯 Objetivo

O objetivo principal é permitir que o Pac-Man encontre o caminho de um estado inicial até um estado final (objetivo) utilizando as etapas do método de Simulated Annealing, simulando o processo físico de resfriamento de metais para escapar de ótimos locais e encontrar soluções globais.

## 🛠️ Tecnologias e Algoritmo

O projeto foi construído sobre o framework clássico do UC Berkeley AI Pacman. 

A implementação está localizada inteiramente no arquivo `search.py` dentro da função `simulatedAnnealingSearch`. O algoritmo utiliza:
- **Energia:** Baseada na Distância de Manhattan até o objetivo.
- **Critério de Aceitação:** Probabilidade baseada na distribuição de Boltzmann ($P = e^{-\Delta E / T}$).
- **Resfriamento:** Decaimento geométrico ($T = T \times \alpha$).

### Variáveis de Controle
- `T` (Temperatura Inicial): 1000.0
- `alpha` (Taxa de Resfriamento): 0.995
- `Tmin` (Temperatura Mínima): 0.01

## 📁 Estrutura do Projeto

Abaixo está a estrutura de diretórios e os arquivos principais do projeto:

```text
📦 projeto-mata64-simulatedAnnealing
 ┣ 📂 layouts/           # Pastas com os arquivos de labirintos (ex: mediumMaze.lay)
 ┣ 📂 test_cases/        # Casos de teste e configurações do autograder original
 ┣ 📜 pacman.py          # Arquivo principal para rodar o jogo
 ┣ 📜 search.py          # ONDE O CÓDIGO FOI FEITO: Implementação do Simulated Annealing
 ┣ 📜 searchAgents.py    # Define os agentes de busca (avaliação de custo, objetivo)
 ┣ 📜 util.py            # Estruturas de dados e funções utilitárias (ex: manhattanDistance)
 ┣ 📜 game.py            # Lógica central do estado e regras do jogo Pac-Man
 ┗ 📜 README.md          # Este arquivo de documentação
```

## 🚀 Como Executar

Para rodar o Pac-Man utilizando o algoritmo de Simulated Annealing, utilize o seguinte comando no terminal:

```bash
python pacman.py -l mediumMaze -p SearchAgent -a fn=sa
```

### Outras Opções de Execução:

Para testar em um labirinto menor e mais rápido:
```bash
python pacman.py -l tinyMaze -p SearchAgent -a fn=sa
```

Para rodar sem a interface gráfica (apenas estatísticas):
```bash
python pacman.py -l mediumMaze -p SearchAgent -a fn=sa -q
```
---
## ✍️ Autoria

Este projeto foi desenvolvido por:

- Samuel Santos
Estudante de Sistemas de Informação – UFBA.
GitHub: [samucaasantos](https://github.com/samucaasantos)

- Jorge Ferreira
Estudante de Sistemas de Informação – UFBA.
GitHub: [Jorgefrgs](https://github.com/Jorgefrgs)

---
*Este projeto foi desenvolvido para fins acadêmicos na Universidade Federal da Bahia (UFBA).*
