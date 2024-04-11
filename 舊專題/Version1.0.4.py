import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Circle
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import random

cube_size = 10 # 定義立方體的邊長和時間間隔
time_interval = 0.05  # 時間間隔
num_fish = 1000 # 定義魚的數量
mark_fish = 200 # 標記魚的數量
num_steps = 100000  # 模擬的步數
small_cube_size = 3 # 漁網大小

# 定義魚的速度範圍
min_speed = 0.1
max_speed = 0.5

# 創建立方體
fig = plt.figure() # 創建立方體空間
ax = fig.add_subplot(111, projection='3d') # 創建3D空間，並且占滿整個畫布
ax.grid(False) # 關閉框線

# 設置立方體的範圍
ax.set_xlim([0, cube_size])
ax.set_ylim([0, cube_size]) 
ax.set_zlim([0, cube_size])

# 隨機生成魚的初始位置、速度、方向、顏色
fish_x = [random.uniform(0, cube_size) for _ in range(num_fish)] # 列表推導式 [運算 for _ in range(數量)]
fish_y = [random.uniform(0, cube_size) for _ in range(num_fish)] # 回傳list型態
fish_z = [random.uniform(0, cube_size) for _ in range(num_fish)] # 包含指定的"數量"及每個數的"運算"結果
fish_speed = [random.uniform(min_speed, max_speed) for _ in range(num_fish)] # 速度
fish_direction = [random.uniform(0, 2 * np.pi) for _ in range(num_fish)] # 方向
fish_colors = ['yellow' if i < mark_fish else 'red' for i in range(num_fish)] # 顏色

# 繪製魚的位置
fish_scatter = ax.scatter(fish_x, fish_y, fish_z, c = fish_colors, marker='o', label='Fish')

catch_count = 0 # 捕捉計數器
save_list = 0

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
    
    if(catch_count % 10 == 0):
        crit_x = random.uniform(0 , 7) 
        crit_y = random.uniform(0 , 7) 
        crit_z = random.uniform(0 , 7) 
        # 定義長方體的八個頂點
        vertices = np.array([
            [crit_x, crit_y, crit_z],
            [crit_x + small_cube_size, crit_y, crit_z],
            [crit_x + small_cube_size, crit_y + small_cube_size, crit_z],
            [crit_x, crit_y + small_cube_size, crit_z],
            [crit_x, crit_y, crit_z + small_cube_size],
            [crit_x + small_cube_size, crit_y, crit_z + small_cube_size],
            [crit_x + small_cube_size, crit_y + small_cube_size, crit_z + small_cube_size],
            [crit_x, crit_y + small_cube_size, crit_z + small_cube_size]
        ])
        # 定義長方體的六個面（每個面都是四個頂點的索引）
        faces = [
            [vertices[0], vertices[1], vertices[5], vertices[4]],
            [vertices[7], vertices[6], vertices[2], vertices[3]],
            [vertices[0], vertices[4], vertices[7], vertices[3]],
            [vertices[1], vertices[5], vertices[6], vertices[2]],
            [vertices[4], vertices[5], vertices[6], vertices[7]],
            [vertices[0], vertices[1], vertices[2], vertices[3]]
        ]
        # 創建長方體的Poly3DCollection對象，設置透明度
        mesh = Poly3DCollection(faces, alpha=0.2, color='blue')
        # 添加長方體到3D子圖
        ax.add_collection3d(mesh)

        # 計算長方體內的魚數量和不同顏色的魚數量
        total_fish_count = sum(1 for x, y, z in zip(fish_x, fish_y, fish_z) if 
                            crit_x <= x < crit_x + small_cube_size and 
                            crit_y <= y < crit_y + small_cube_size and 
                            crit_z <= z < crit_z + small_cube_size)
        
        yellow_fish_count = sum(1 for x, y, z , color in zip(fish_x, fish_y, fish_z, fish_colors) if 
                            crit_x <= x < crit_x + small_cube_size and 
                            crit_y <= y < crit_y + small_cube_size and 
                            crit_z <= z < crit_z + small_cube_size and 
                            color == "yellow" )
        
        x = mark_fish * total_fish_count / yellow_fish_count
        save_list += x
        print("預測魚數量" , x)
        print("預測" , int(catch_count / 10 + 1 ) , "次平均:",save_list/(catch_count/10 + 1))
    
    elif(catch_count % 5 == 0):
        # 刪除長方體
        mesh.remove()
    
    catch_count =  catch_count + 1
    plt.pause(0.1)
plt.show()
