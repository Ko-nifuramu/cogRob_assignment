import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from __init__ import MAX_TIME_STEP

def visu_lorenz_map(lorenz_map : np.ndarray, p:int, r = 28, b=8/3):
    '''
    lorenz_map.shape : (1, Max_time_step, 3)
    '''
    print('lorenz_map : {}'.format(lorenz_map.shape))
    print(f'p : {p}')
    
    lorenz_map.reshape(-1, 3)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    
    
    # ax.view_init(elev=20., azim=-35)
    ax.set_title(f"lorenz_map : param(p={p},r={r},b=8/3)")
    ax.set_xlabel("x", size = 14)
    ax.set_ylabel("y", size = 14)
    ax.set_zlabel("z", size = 14)
    ax.plot(lorenz_map[:,0], lorenz_map[:,1], lorenz_map[:,2])
    
    
    plt.savefig("image/lorenz/p_" + str(p)+"with_label"+".jpeg")

def visu_lorenz_init_sensitivity(two_data_logi_map : np.ndarray, iniPos1:float, iniPos2:float):
    
    lorenz_map1 = two_data_logi_map[0]
    lorenz_map2 = two_data_logi_map[1]
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    ax.set_title(f"sensitivity to initial conditions")
    ax.set_xlabel("x", size = 14)
    ax.set_ylabel("y", size = 14)
    ax.set_zlabel("z", size = 14)
    ax.plot(lorenz_map1[:,0], lorenz_map1[:,1], lorenz_map1[:,2], color='deepskyblue')
    ax.plot(lorenz_map2[:,0], lorenz_map2[:,1], lorenz_map2[:,2], color='palegreen')
    
    plt.legend(['initPos1(x,y,z) = {:.10f}'.format(iniPos1[0, 0, 0]), 'initPos2(x,y,z) = {:.10f}'.format(iniPos2[0, 0, 0])])
    plt.savefig("image/sensitivity_to_initialPos_lorenz")
    
    
def visu_lorenz_bifu_sensitivity(two_data_logi_map : np.ndarray, noise : float):
    
    lorenz_map1 = two_data_logi_map[0]
    lorenz_map2 = two_data_logi_map[1]
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    ax.set_title(f"sensitivity to bifurcation params")
    ax.set_xlabel("x", size = 14)
    ax.set_ylabel("y", size = 14)
    ax.set_zlabel("z", size = 14)
    ax.plot(lorenz_map1[:,0], lorenz_map1[:,1], lorenz_map1[:,2], color='deepskyblue')
    ax.plot(lorenz_map2[:,0], lorenz_map2[:,1], lorenz_map2[:,2], color='palegreen')
    
    plt.legend(['P(p,r,b) = ({:.10f}, {:.10f}, {:.10f}'.format(6, 28, 8/3), 'P(p,r,b) = {:.10f}, {:.10f}, {:.10f}'.format(6*(1+noise), 28,(8/3))])
    plt.savefig("image/sensitivity_to_bifu_lorenz")