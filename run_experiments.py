import subprocess
import os
import re

def run_pacman(alpha, t_init, layout="mediumMaze"):
    env = os.environ.copy()
    env["SA_ALPHA"] = str(alpha)
    env["SA_T"] = str(t_init)
    
    cmd = ["python", "pacman.py", "-l", layout, "-p", "SearchAgent", "-a", "fn=sa", "-q"]
    try:
        output = subprocess.check_output(cmd, env=env, stderr=subprocess.STDOUT, timeout=30).decode()
        
        cost_match = re.search(r"Path found with total cost of (\d+)", output)
        nodes_match = re.search(r"Search nodes expanded: (\d+)", output)
        
        cost = int(cost_match.group(1)) if cost_match else "N/A"
        nodes = int(nodes_match.group(1)) if nodes_match else "N/A"
        return cost, nodes
    except subprocess.TimeoutExpired:
        return "Timeout", "Timeout"
    except Exception as e:
        return "Error", "Error"

print("--- Experimento 1: Variando Alpha (T=1000, mediumMaze) ---")
alphas = [0.9, 0.95, 0.99, 0.995, 0.999]
print(f"{'Alpha':<10} | {'Custo':<10} | {'Nós Exp.':<10}")
print("-" * 35)
for a in alphas:
    cost, nodes = run_pacman(a, 1000.0)
    print(f"{a:<10} | {cost:<10} | {nodes:<10}")

print("\n--- Experimento 2: Variando Temperatura Inicial (Alpha=0.995, mediumMaze) ---")
temps = [10, 100, 1000, 10000]
print(f"{'Temp':<10} | {'Custo':<10} | {'Nós Exp.':<10}")
print("-" * 35)
for t in temps:
    cost, nodes = run_pacman(0.995, t)
    print(f"{t:<10} | {cost:<10} | {nodes:<10}")

print("\n--- Experimento 3: Diferentes Layouts (Alpha=0.995, T=1000) ---")
layouts = ["tinyMaze", "smallMaze", "mediumMaze"]
print(f"{'Layout':<15} | {'Custo':<10} | {'Nós Exp.':<10}")
print("-" * 40)
for l in layouts:
    cost, nodes = run_pacman(0.995, 1000.0, l)
    print(f"{l:<15} | {cost:<10} | {nodes:<10}")
