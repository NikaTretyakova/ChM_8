import pandas as pd
import matplotlib.pyplot as plt
import os

base_folder = r"C:\Users\Veronika\Desktop\ChM_laba8"
data_folder = os.path.join(base_folder, "data")
graphs_folder = os.path.join(base_folder, "graphs")

system = "Совы_Мыши_eq"
system_name = "Совы_Мыши"

color = "#F7D34F"

os.makedirs(graphs_folder, exist_ok=True)
try:
    prey_euler = pd.read_csv(os.path.join(data_folder, f"{system}_prey_euler.csv"))
    pred_euler = pd.read_csv(os.path.join(data_folder, f"{system}_pred_euler.csv"))
    phase_euler = pd.read_csv(os.path.join(data_folder, f"{system}_phase_euler.csv"))

    prey_rk4 = pd.read_csv(os.path.join(data_folder, f"{system}_prey_rk4.csv"))
    pred_rk4 = pd.read_csv(os.path.join(data_folder, f"{system}_pred_rk4.csv"))
    phase_rk4 = pd.read_csv(os.path.join(data_folder, f"{system}_phase_rk4.csv"))

    plt.figure(figsize=(10, 6))
    plt.plot(prey_euler['Time'], prey_euler['Prey'], color=color, linewidth=2)
    plt.xlabel('Время (дни)', fontsize=12)
    plt.ylabel('Численность жертв', fontsize=12)
    plt.title(f'{system_name} - Жертвы\nМетод Эйлера', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.savefig(os.path.join(graphs_folder, f"{system}_prey_euler.png"), 
                dpi=150, bbox_inches='tight')
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.plot(pred_euler['Time'], pred_euler['Predator'], color=color, linewidth=2)
    plt.xlabel('Время (дни)', fontsize=12)
    plt.ylabel('Численность хищников', fontsize=12)
    plt.title(f'{system_name} - Хищники\nМетод Эйлера', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.savefig(os.path.join(graphs_folder, f"{system}_pred_euler.png"), 
                dpi=150, bbox_inches='tight')
    plt.close()

    plt.figure(figsize=(8, 8))
    plt.plot(phase_euler['Prey'], phase_euler['Predator'], color=color, linewidth=2, alpha=0.9)
    plt.xlabel('Численность жертв', fontsize=12)
    plt.ylabel('Численность хищников', fontsize=12)
    plt.title(f'{system_name} - Фазовый портрет\nМетод Эйлера', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.savefig(os.path.join(graphs_folder, f"{system}_phase_euler.png"), 
                dpi=150, bbox_inches='tight')
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.plot(prey_rk4['Time'], prey_rk4['Prey'], color=color, linewidth=2)
    plt.xlabel('Время (дни)', fontsize=12)
    plt.ylabel('Численность жертв', fontsize=12)
    plt.title(f'{system_name} - Жертвы\nМетод РК4', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.savefig(os.path.join(graphs_folder, f"{system}_prey_rk4.png"), 
                dpi=150, bbox_inches='tight')
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.plot(pred_rk4['Time'], pred_rk4['Predator'], color=color, linewidth=2)
    plt.xlabel('Время (дни)', fontsize=12)
    plt.ylabel('Численность хищников', fontsize=12)
    plt.title(f'{system_name} - Хищники\nМетод РК4', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.savefig(os.path.join(graphs_folder, f"{system}_pred_rk4.png"), 
                dpi=150, bbox_inches='tight')
    plt.close()

    plt.figure(figsize=(8, 8))
    plt.plot(phase_rk4['Prey'], phase_rk4['Predator'], color=color, linewidth=2, alpha=0.9)
    plt.xlabel('Численность жертв', fontsize=12)
    plt.ylabel('Численность хищников', fontsize=12)
    plt.title(f'{system_name} - Фазовый портрет\nМетод РК4', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.savefig(os.path.join(graphs_folder, f"{system}_phase_rk4.png"), 
                dpi=150, bbox_inches='tight')
    plt.close()
    
except FileNotFoundError as e:
    print(f"✗ Файлы не найдены для: {system}")
    print(f"  Ошибка: {e}")
    import glob
    existing_files = glob.glob(os.path.join(data_folder, f"{system}*.csv"))
    if existing_files:
        print(f"  Найдены файлы: {[os.path.basename(f) for f in existing_files]}")
    else:
        print(f"  Нет файлов с префиксом: {system}")
