import random

def simulate(x): #simulate(模擬次數)
    markFish = list(range(1, 501)) # 500 隻標記魚
    fish = list(range(501, 10001)) # 9500 隻魚
    merge = markFish + fish # 共計 10000 隻魚

    catchFish = 2000 # 定義一次要抓幾隻魚
    
    count = 0 # 計數器
    accumulator = 0 # 累加器

    while(count < x):
        # 初始化漁網和標記魚計數器
        choice = []
        isMark = 0

        random.shuffle(merge) # 讓魚隨機
        for i in range(catchFish):
            choice.append(random.choice(merge))
            if choice[i] in markFish :
                isMark = isMark + 1

        if isMark == 0: # 除錯
            continue
        else:
            count = count + 1

        predict = len(markFish) * catchFish / isMark # 帶入公式推測總魚隻數
        #print("第 ",count," 次預測:",predict)

        accumulator = accumulator + predict

    print("預測" , count , "次平均結果" , accumulator / count)
    print("誤差百分比:" , abs(10000 - accumulator / count) / 10000 * 100 , "% \t 誤差隻數:" , 10000 - accumulator / count)    

simulate(100)