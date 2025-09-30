import cv2
import numpy as np
import matplotlib.pyplot as plt

def inter_mean_threshold(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("ไม่พบไฟล์ภาพ")
        return
    
    T0 = np.mean(img)
    print(f"ค่าเฉลี่ยความสว่างของภาพ (T0): {T0}")

    T1 = 0
    interaction = 0
    while True:
        g1 = img[img >= T0]
        g0 = img[img <T0]

        mean_g1 = np.mean(g1) if g1.size > 0 else 0
        mean_g0 = np.mean(g0) if g0.size > 0 else 0

        T1 = (mean_g1 + mean_g0) / 2
        print(f"รอบที่ {interaction}: T เก่า={T0:.2f}, T ใหม่={T1:.2f}")

        if abs(T1 - T0) < 1:
            break
            
        T0 = T1
        interaction += 1

    print(f"\n ค่า Threshold ที่เหมาะสมที่สุด: {int(T1)}")
    return int(T1), img