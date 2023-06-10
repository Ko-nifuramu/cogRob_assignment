from src.continuous_system import simulate_continuous_system
from src.discrete_system import simulate_discrete_system

def main():
    '''
    simulate_discrete_system(), simulate_cintinuous_system()
    every function does
    
    ・attractor change with bifu_param
    ・sensitivity to bifurcation params
    ・sensitivity to initial conditions
    
    these three simulations.
    
    シミュレーション結果は、全てimageのフォルダに格納されます
    '''
    simulate_discrete_system()
    simulate_continuous_system()

if __name__ == "main":
    main()