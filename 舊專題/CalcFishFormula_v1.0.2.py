import random

def simulate(markFishCount,totalFish,catchFish,countingTimes): #simulate(標記魚隻數,總隻數,抓魚隻數,估算次數)
    markFish = list(range(1 , markFishCount + 1)) # 500 隻做標記
    fish = list(range(501, totalFish + 1 )) 
    merge = markFish + fish # 共計 10000 隻魚
    count = 0 
    accumulator = 0 # 累加器
    while(count < countingTimes):
        choice = []
        isMark = 0
        random.shuffle(merge) # 讓魚隨機

        for i in range(catchFish):
            choice.append(random.choice(merge))
            
        for i in choice:
            if i in markFish :
                isMark = isMark + 1
        
        if isMark == 0:
            continue
        else:
            count = count + 1

        predict = len(markFish) * catchFish / isMark
        
        #print("第 ",count," 次預測:",predict)
        accumulator = accumulator + predict

    print("預測" , count , "次平均結果" , accumulator / count)
    print("誤差" , abs(10000 - accumulator / count) / 10000 * 100 , "%" )    

simulate(500,10000,2000,20)
