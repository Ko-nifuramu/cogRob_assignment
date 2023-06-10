import matplotlib.pyplot as plt
import numpy as np
from __init__ import MAX_TIME_STEP

def visu_logi_map(logi_map : np.ndarray, a:int):
    print(f'a : {a}')
    linear = np.zeros((int(MAX_TIME_STEP), 2))
    logi = np.zeros((int(MAX_TIME_STEP), 2))
    for i in range(int(MAX_TIME_STEP)):
        linear[i,0] = i/MAX_TIME_STEP
        linear[i,1] = i/MAX_TIME_STEP
        logi[i,0] = i/MAX_TIME_STEP
        logi[i,1] = a*logi[i,0]*(1-logi[i,0])
    
    fig = plt.figure()
    plt.plot(logi_map[:, 0], logi_map[:, 1])
    plt.xlim(0, 1)
    plt.plot(linear[:,0], linear[:,1], color='k')
    plt.plot(logi[:,0], logi[:,1], color='k')
    plt.title(f"logistic_map : a = {a}")
    plt.savefig("image/logi/a_" + str(a)+".jpeg")


def visu_logi_iniPos_sensitivity(two_data_logi_map : np.ndarray, initPos1:float, initPos2:float):
    plt.figure()
    plt.xlim(0, two_data_logi_map.shape[1])
    plt.plot(two_data_logi_map[0, :], color='deepskyblue')
    plt.plot(two_data_logi_map[1, :], color='palegreen')
    plt.legend(['initPos1={:.10f}'.format(initPos1), 'initPos2={:.10f}'.format(initPos2)], loc="upper left")
    plt.savefig("image/sensitivity_to_iniPos_logi")


def visu_logi_bifu_sensitivity(two_data_logi_map : np.ndarray, a1:float, a2:float):
    plt.figure()
    plt.xlim(0, two_data_logi_map.shape[1])
    plt.plot(two_data_logi_map[0, :], color='deepskyblue')
    plt.plot(two_data_logi_map[1, :], color='palegreen')
    plt.legend(['a1={:.10f}'.format(a1), 'a2={:.10f}'.format(a2)], loc="upper left")
    plt.savefig("image/sensitivity_to_bifu_params_logi")