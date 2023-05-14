import numpy as np
from __init__ import MAX_TIME_STEP, BIFU_TIME_STEP
from visualize_util.visualize_lor import visu_lorenz_map, visu_lorenz_init_sensitivity

def simulate_continuous_system():
    #attractor transfer(bifurcation)
    # p = [13, 14, 15, 20, 23, 23.5, 23.5, 24.3, 24.4, 24.5, 24.6, 24.7, 24.8, 26, 27, 28]
    p = [i/1000 for i in range(5190, 5210, 1)]
    lorenz_map = np.zeros((len(p),int(MAX_TIME_STEP), 3))
    x0 = 0.4
    
    for i in range(len(p)):
        lorenz_map[i,0,0] = x0
        lorenz_map[i,0,1] = x0
        lorenz_map[i,0,2] = x0
        for j in range(0, int(MAX_TIME_STEP-1)):
            lorenz_next = F_lorenz_system(lorenz_map[i,j,:],p=p[i])
            lorenz_map[i, j+1, :] = lorenz_next.reshape(1,1,3)
            
    
        visu_lorenz_map(lorenz_map[i], p[i])
    
    #sesitivity to initial params
    initial_point1 = np.ones((1,1,3))/2
    initial_point2 = initial_point1 + np.ones((1,1,3))/pow(10, 5)
    
    lorenz_iniPosi_compare = np.zeros((2, int(MAX_TIME_STEP), 3))
    lorenz_iniPosi_compare[0,0, :]=initial_point1
    lorenz_iniPosi_compare[1,0, :]=initial_point2
    
    for i in range(1, int(MAX_TIME_STEP)):
        lorenz_iniPosi_compare[0, i, :] = F_lorenz_system(lorenz_iniPosi_compare[0, i-1, :], p=6)
        lorenz_iniPosi_compare[1, i, :] = F_lorenz_system(lorenz_iniPosi_compare[1, i-1, :], p=6)
    
    visu_lorenz_init_sensitivity(lorenz_iniPosi_compare, initial_point1, initial_point2)


def F_lorenz_system(point_pre : np.ndarray, p, dt = 1e-3, r=28, b=8/3)->np.ndarray:
    '''
    point_pre.shape : (1, 3)
    data -> 1, xyz,->3
    '''
    point_pre.reshape(3,1)
    dx = (-p*point_pre[0]+p*point_pre[1])*dt
    dy = (-point_pre[0]*point_pre[2] + r*point_pre[0] -point_pre[1])*dt
    dz = (point_pre[0]*point_pre[1] - b*point_pre[2])*dt
    
    point_next = np.array([point_pre[0]+dx, 
                            point_pre[1]+dy,
                            point_pre[2]+dz])
    
    return point_next.reshape(1,3)

simulate_continuous_system()