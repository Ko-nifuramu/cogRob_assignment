import numpy as np
from src.util.visualize_util.visualize_logi import visu_logi_map, visu_logi_bifu_sensitivity
from __init__ import MAX_TIME_STEP, BIFU_TIME_STEP


def simulate_discrete_system():
    #attractor transfer
    a = [1.0, 2.7, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0]
    logi_map = np.zeros((len(a),int(2*MAX_TIME_STEP), 2))
    x0 = 0.5
    
    for i in range(len(a)):
        logi_map[i,0,0] = x0
        logi_map[i,0,1] = 0
        for j in range(0, int(MAX_TIME_STEP-1)):
            logi_next = F_logistic_map(logi_map[i,j,0],a[i])
            logi_map[i, 2*j+1, 0] = logi_map[i,2*j,0]
            logi_map[i, 2*j+1, 1] = logi_next
            logi_map[i, 2*j+2, 0] = logi_next
            logi_map[i, 2*j+2, 1] = logi_next
    
        visu_logi_map(logi_map[i], a[i])
    
    #sesitivity to bifu params
    a1 = 3.91
    a2 = 3.9100000001
    logi_bifu_compare = np.zeros((2, BIFU_TIME_STEP))
    logi_bifu_compare[0, 0] = x0
    logi_bifu_compare[1, 0] = x0
    
    for i in range(1, BIFU_TIME_STEP):
        logi_bifu_compare[0, i] = F_logistic_map(logi_bifu_compare[0, i-1], a1)
        logi_bifu_compare[1, i] = F_logistic_map(logi_bifu_compare[1, i-1], a2)
    
    visu_logi_bifu_sensitivity(logi_bifu_compare, a1, a2)


def F_logistic_map(x_pre : float, a_ele : float)->float:
    x_next = a_ele*(x_pre)*(1-x_pre)
    return x_next


simulate_discrete_system()