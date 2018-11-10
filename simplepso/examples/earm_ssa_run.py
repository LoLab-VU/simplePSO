import matplotlib.pyplot as plt
import numpy as np
plt.switch_backend('agg')
from pysb.simulator import BngSimulator
from pysb.simulator import ScipyOdeSimulator
from pysb.simulator import StochKitSimulator
from earm_ssa import model
TRAIL = model.monomers['L']

import datetime
now = datetime.datetime.now()

# Definitions
NUM_SSA_RUNS = 10 #How many times SSA will be ran

#Length of simulation
tspan = np.linspace(0, 360, 361)

#turn off graphs showing up
plt.ioff()

#Set Path to save files needed
path = r'\Users\geenaildefonso\Projects\ParticleSwarmOptimization' #path for diablo

#RUN THROUGH EACH AMOUNT OF TRAIL:
TRAIL_LOOP = [('1000 ng/ml TRAIL', 740853), ('250 ng/ml TRAIL', 18521), ('40 ng/ml TRAIL', 3000), ('10 ng/ml TRAIL', 740)]
for trail_title, dose in TRAIL_LOOP:

    #RUN STOCHASTIC SIMULATION ALGORITHM (SSA)
    ssa_sim = StochKitSimulator(model, tspan=tspan, verbose=True)
    ssa_sim_res = ssa_sim.run(algorithm = 'ssa', initials={TRAIL(bf=None): dose}, n_runs=NUM_SSA_RUNS)
   # ssa_sim_res.save(path + 'SSA_data_%dTNF' % dose)
    df = ssa_sim_res.dataframe #pandas dataframe organizes data

    #FOR EACH OBSERVABLE AVERAGE THE SSA RUNS AT EACH TIME POINT
    avg = df.groupby(level='time').mean()

    #RUN ODE SIMULATION
    ode_sim = ScipyOdeSimulator(model, tspan=tspan)
    ode_sim_res = ode_sim.run(initials={TRAIL(bf=None): dose})

    # PLOT STOCHASTIC SIMULATION ALGORITHM (SSA) WITH AVG SSA (YELLOW) AND ODE (BLACK)
    # Array: [(Observable name, number to start y axis at, number to end y axis at)]
    # obs_y_range = [('CI_k63_obs', 0, 520), ('CII_obs', 0, 410), ('MLKLa_obs', 0, 10300)]
    #
    # for obs, y1, y2 in obs_y_range:
    #     plt.figure()
    #     plt.title(trail_title)
    #     plt.ylim(y1, y2)
    #     for _, run in df.groupby('simulation'):
    #             plt.plot(tspan / 60, run.loc[:, obs])
    #     plt.plot(tspan / 60, avg.loc[:, obs], 'gold', linewidth=3)
    #     plt.plot(tspan / 60, ode_sim_res.observables[obs], 'black', linewidth=3, linestyle='dashed')
    #     plt.xlabel("Time (in hr)", fontsize=15)
    #     plt.ylabel("Molecules/Cell", fontsize=15)
    #     plt.title('%s Trajectories' % obs, fontsize=18)
    #     name = 'uncal_run5_%d_SSA_%s_' % (dose, obs)
    #     ssa_name = name + str(now.strftime('%Y-%m-%d_%H%M.png'))
    #     plt.savefig(ssa_name, bbox_inches='tight')

    obs_y_range = [('mBid'), ('aSmac'), ('cPARP')]

    for obs in obs_y_range:
        plt.figure()
        plt.title(trail_title)
        # plt.ylim(y1, y2)
        for _, run in df.groupby('simulation'):
                plt.plot(tspan / 60, run.loc[:, obs])
        plt.plot(tspan / 60, avg.loc[:, obs], 'gold', linewidth=3)
        plt.plot(tspan / 60, ode_sim_res.observables[obs], 'black', linewidth=3, linestyle='dashed')
        plt.xlabel("Time (in hr)", fontsize=15)
        plt.ylabel("Molecules/Cell", fontsize=15)
        plt.title('%s Trajectories' % obs, fontsize=18)
        name = 'uncal_runtrail_%d_SSA_%s_' % (dose, obs)
        ssa_name = name + str(now.strftime('%Y-%m-%d_%H%M.png'))
        plt.savefig(ssa_name, bbox_inches='tight')