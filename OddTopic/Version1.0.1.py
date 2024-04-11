import numpy as np
import matplotlib.pyplot as plt
import random

cube_size = 10 # 定義立方體的邊長和時間間隔
time_interval = 0.05  # 時間間隔
num_fish = 100 # 定義魚的數量
mark_fish = 10 # 標記魚的數量
num_steps = 1000  # 模擬的步數

# 定義魚的速度範圍
min_speed = 0.1
max_speed = 0.5

# 創建立方體
fig = plt.figure() # 創建立方體空間
ax = fig.add_subplot(111, projection='3d') # 創建3D空間，並且占滿整個畫布
ax.grid(False) # 關閉框線
# 隱藏座標軸標籤
ax.set_xticks([]) 
ax.set_yticks([]) 
ax.set_zticks([])
# 設置立方體的範圍
ax.set_xlim([0, cube_size])
ax.set_ylim([0, cube_size]) 
ax.set_zlim([0, cube_size])

# 隨機生成魚的初始位置、速度、方向、顏色
fish_x = [random.uniform(0, cube_size) for _ in range(num_fish)] # 列表推導式 [運算 for _ in range(數量)]
fish_y = [random.uniform(0, cube_size) for _ in range(num_fish)] # 回傳list型態
fish_z = [random.uniform(0, cube_size) for _ in range(num_fish)] # 包含指定的"數量"及每個數的"運算"結果
fish_speed = [random.uniform(min_speed, max_speed) for _ in range(num_fish)] #速度
fish_direction = [random.uniform(0, 2 * np.pi) for _ in range(num_fish)] #方向
fish_colors = ['yellow' if i < mark_fish else 'red' for i in range(num_fish)] #顏色

# 繪製魚的位置
fish_scatter = ax.scatter(fish_x, fish_y, fish_z, c = fish_colors, marker='o', label='Fish')

# 開始模擬魚的游動
for _ in range(num_steps):
    # 更新魚的位置，模擬游動
    for i in range(num_fish):
        fish_x[i] += fish_speed[i] * np.cos(fish_direction[i]) * time_interval
        fish_y[i] += fish_speed[i] * np.sin(fish_direction[i]) * time_interval
        fish_z[i] += fish_speed[i] * np.sin(fish_direction[i]) * time_interval

        # 確保魚不會超出立方體的邊界
        fish_x[i] = max(0, min(fish_x[i], cube_size))
        fish_y[i] = max(0, min(fish_y[i], cube_size))
        fish_z[i] = max(0, min(fish_z[i], cube_size)) 
        
        # 隨機改變魚的方向
        fish_direction[i] += random.uniform(-np.pi/4, np.pi/4)
    
    fish_scatter._offsets3d = (fish_x, fish_y, fish_z)
    fish_scatter._facecolor3d = fish_colors
    
    plt.pause(0.1)
plt.show()
