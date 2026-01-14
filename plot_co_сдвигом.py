import pandas as pd
import matplotlib.pyplot as plt
import os

# Пути к папкам
base_folder = r"C:\Users\Veronika\Desktop\ChM_laba8"
data_folder = os.path.join(base_folder, "data")
graphs_folder = os.path.join(base_folder, "graphs")

# ТОЛЬКО СЛУЧАЙ С МАЛЫМИ ОТКЛОНЕНИЯМИ (СДВИГ)
system = "Совы_Мыши_pert"
system_name = "Совы_Мыши"

# Цвет графика (светло-желтый)
color = "#F7D34F"

# Создаем папку для графиков
os.makedirs(graphs_folder, exist_ok=True)

print(f"Создание графиков для: {system_name} (малые отклонения от равновесия)")

try:
    # Загрузка данных ДЛЯ МЕТОДА ЭЙЛЕРА
    prey_euler = pd.read_csv(os.path.join(data_folder, f"{system}_prey_euler.csv"))
    pred_euler = pd.read_csv(os.path.join(data_folder, f"{system}_pred_euler.csv"))
    phase_euler = pd.read_csv(os.path.join(data_folder, f"{system}_phase_euler.csv"))
    
    # Загрузка данных ДЛЯ МЕТОДА РК4
    prey_rk4 = pd.read_csv(os.path.join(data_folder, f"{system}_prey_rk4.csv"))
    pred_rk4 = pd.read_csv(os.path.join(data_folder, f"{system}_pred_rk4.csv"))
    phase_rk4 = pd.read_csv(os.path.join(data_folder, f"{system}_phase_rk4.csv"))
    
    # === МЕТОД ЭЙЛЕРА ===
    # 1. График жертв (Эйлер)
    plt.figure(figsize=(10, 6))
    plt.plot(prey_euler['Time'], prey_euler['Prey'], color=color, linewidth=2)
    plt.xlabel('Время (дни)', fontsize=12)
    plt.ylabel('Численность жертв', fontsize=12)
    plt.title(f'{system_name} - Жертвы\nМетод Эйлера (со сдвигом)', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.savefig(os.path.join(graphs_folder, f"{system}_prey_euler.png"), 
                dpi=150, bbox_inches='tight')
    plt.close()
    
    # 2. График хищников (Эйлер)
    plt.figure(figsize=(10, 6))
    plt.plot(pred_euler['Time'], pred_euler['Predator'], color=color, linewidth=2)
    plt.xlabel('Время (дни)', fontsize=12)
    plt.ylabel('Численность хищников', fontsize=12)
    plt.title(f'{system_name} - Хищники\nМетод Эйлера (со сдвигом)', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.savefig(os.path.join(graphs_folder, f"{system}_pred_euler.png"), 
                dpi=150, bbox_inches='tight')
    plt.close()
    
    # 3. Фазовый портрет (Эйлер)
    plt.figure(figsize=(8, 8))
    plt.plot(phase_euler['Prey'], phase_euler['Predator'], color=color, linewidth=2, alpha=0.9)
    plt.xlabel('Численность жертв', fontsize=12)
    plt.ylabel('Численность хищников', fontsize=12)
    plt.title(f'{system_name} - Фазовый портрет\nМетод Эйлера (со сдвигом)', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.savefig(os.path.join(graphs_folder, f"{system}_phase_euler.png"), 
                dpi=150, bbox_inches='tight')
    plt.close()
    
    # === МЕТОД РК4 ===
    # 4. График жертв (РК4)
    plt.figure(figsize=(10, 6))
    plt.plot(prey_rk4['Time'], prey_rk4['Prey'], color=color, linewidth=2)
    plt.xlabel('Время (дни)', fontsize=12)
    plt.ylabel('Численность жертв', fontsize=12)
    plt.title(f'{system_name} - Жертвы\nМетод РК4 (со сдвигом)', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.savefig(os.path.join(graphs_folder, f"{system}_prey_rk4.png"), 
                dpi=150, bbox_inches='tight')
    plt.close()
    
    # 5. График хищников (РК4)
    plt.figure(figsize=(10, 6))
    plt.plot(pred_rk4['Time'], pred_rk4['Predator'], color=color, linewidth=2)
    plt.xlabel('Время (дни)', fontsize=12)
    plt.ylabel('Численность хищников', fontsize=12)
    plt.title(f'{system_name} - Хищники\nМетод РК4 (со сдвигом)', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.savefig(os.path.join(graphs_folder, f"{system}_pred_rk4.png"), 
                dpi=150, bbox_inches='tight')
    plt.close()
    
    # 6. Фазовый портрет (РК4)
    plt.figure(figsize=(8, 8))
    plt.plot(phase_rk4['Prey'], phase_rk4['Predator'], color=color, linewidth=2, alpha=0.9)
    plt.xlabel('Численность жертв', fontsize=12)
    plt.ylabel('Численность хищников', fontsize=12)
    plt.title(f'{system_name} - Фазовый портрет\nМетод РК4 (со сдвигом)', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.savefig(os.path.join(graphs_folder, f"{system}_phase_rk4.png"), 
                dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Созданы 6 графиков для: {system_name} (малые отклонения)")
    print(f"  - Метод Эйлера: жертвы, хищники, фазовый портрет")
    print(f"  - Метод РК4: жертвы, хищники, фазовый портрет")
    
except FileNotFoundError as e:
    print(f"✗ Файлы не найдены для: {system}")
    print(f"  Ошибка: {e}")
    # Проверим, какие файлы действительно существуют
    import glob
    existing_files = glob.glob(os.path.join(data_folder, f"{system}*.csv"))
    if existing_files:
        print(f"  Найдены файлы: {[os.path.basename(f) for f in existing_files]}")
    else:
        print(f"  Нет файлов с префиксом: {system}")

print(f"\nВсе графики сохранены в: {graphs_folder}")
print("\nСозданы файлы:")
print(f"  1. {system}_prey_euler.png")
print(f"  2. {system}_pred_euler.png")
print(f"  3. {system}_phase_euler.png")
print(f"  4. {system}_prey_rk4.png")
print(f"  5. {system}_pred_rk4.png")
print(f"  6. {system}_phase_rk4.png")
