# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import random
import math

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def simulatedAnnealingSearch(problem, heuristic=None):
    """
    Busca o nó objetivo usando o método de Têmpera Simulada (Simulated Annealing).
    """
    if heuristic is None:
        heuristic = nullHeuristic

    # 1. Variáveis Obrigatórias da Especificação
    T = 1000.0 #temperatura inicial
    alpha = 0.995 #taxa de resfriamento
    Tmin = 0.01 #temperatura mínima para aceitar soluções piores com base em probabilidade

    # 2. Inicialização do estado e caminho
    current_state = problem.getStartState()
    current_path = [] # Guarda as ações (Cima, Baixo, etc.) tomadas pelo Pac-Man

    # 3. Loop de Resfriamento
    while T > Tmin:
        # Verifica se o estado atual já é o objetivo final
        if problem.isGoalState(current_state):
            return current_path

        # Gera todos os movimentos legais a partir da posição atual
        # getSuccessors retorna uma lista de tuplas no formato: (next_state, action, step_cost)
        successors = problem.getSuccessors(current_state)

        if not successors:
            # Se o Pac-Man entrar em um beco sem saída e não tiver sucessores
            break

        # Sorteia um vizinho aleatoriamente
        next_node = random.choice(successors)
        next_state = next_node[0]
        action = next_node[1]

        # 4. Avaliação de Energia (Custo)
        # Queremos minimizar a "energia". Um estado mais próximo do objetivo tem menor energia.
        current_energy = heuristic(current_state, problem)
        next_energy = heuristic(next_state, problem)

        # Se a heurística for a padrão nula, usamos a distância de Manhattan 
        # como energia para guiar o SA e não ser apenas um passeio aleatório.
        if heuristic == nullHeuristic and hasattr(problem, 'goal'):
            current_energy = util.manhattanDistance(current_state, problem.goal)
            next_energy = util.manhattanDistance(next_state, problem.goal)

        # Calcula a diferença de energia (Delta E)
        delta_E = next_energy - current_energy

        # 5. Critério de Aceitação
        if delta_E <= 0:
            # Vizinho é melhor ou igual: aceita automaticamente
            current_state = next_state
            current_path.append(action)
        else:
            # Vizinho é pior: calcula a probabilidade de aceitação usando a fórmula de Boltzmann
            try:
                # P = e^(-DeltaE / T)
                probability = math.exp(-delta_E / T)
            except OverflowError:
                probability = 0 # Previne erro matemático caso os valores explodam

            # Sorteia um número entre 0 e 1 e compara com a probabilidade
            if random.random() < probability:
                # Aceita o movimento ruim para tentar escapar de um ótimo local
                current_state = next_state
                current_path.append(action)
            else:
                # Se rejeitar o movimento, o estado não muda nesta iteração.
                pass

        # 6. Resfriamento
        T = T * alpha

    # Retorna o caminho construído até o limite da temperatura ou até encontrar o objetivo
    return current_path

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
sa = simulatedAnnealingSearch
