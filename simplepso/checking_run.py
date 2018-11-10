from pysb.core import *
from pysb.bng import *
from pysb.integrate import *
from pysb.simulator.bng import BngSimulator
import matplotlib.pyplot as plt
import numpy as np
from pysb.util import alias_model_components
from necroptosismodule import model


fstpso = [2326, 4800, 9000, 40000, 9000, 9000, 9000, 9000, 8030, 3900, 7226, 9000, 40000, 24000, 10000,
3.304257485026848768e-05,
9.791215971368776028e-03,
6.110068937548310437e-03,
4.319219461882335177e-05,
4.212644667502709987e-03,
1.164332269398710173e-05,
2.404257105292715788e-02,
3.311085510054400207e-05,
4.280399320119887552e-02,
2.645814637693955063e-05,
1.437707485722601597e-02,
2.303744002126363599e-01,
2.980688423948379739e-05,
4.879773212139151134e-02,
1.121503480627013705e-05,
1.866712857727401229e-03,
7.572177664736867708e-01,
1.591282730353343167e-05,
3.897146248650381478e-02,
3.076363174012029411e+00,
3.734859661130401243e+00,
3.216200470463125876e-06,
8.782429548444865440e-05,
2.906341314225960662e-02,
5.663104188870970508e-05,
2.110469405515222677e-02,
1.294086380531199176e-01,
3.127598126760888220e-01,
4.298489868360909627e-01,
2.332910188537793332e-06,
7.077504621536276526e-03,
6.294061533948092091e-01,
6.419313355304218094e-02,
8.584653667640911989e-04,
8.160445062706172072e-05,
4.354383618147421691e-06,
4.278903092658225660e+00
]

tspan = np.linspace(0, 480, 481)
sim2 = BngSimulator(model, tspan=tspan)
L4 = sim2.run(method='ode', param_values=fstpso)


plt.figure()
# # plt.plot(tspan/60, L3.observables['MLKLa_obs'],color = 'purple',label = 'MLKLp')
# plt.plot(tspan/60, sim_result1.observables['MLKLa_obs'],label = '100 ng/ml TNF')
# plt.plot(tspan/60, sim_result2.observables['MLKLa_obs'],label = '10 ng/ml TNF')
# plt.plot(tspan/60, sim_result3.observables['MLKLa_obs'],label = '1 ng/ml TNF')
# plt.plot(tspan/60, sim_result4.observables['MLKLa_obs'],label = '0.1 ng/ml TNF')
# # plt.plot(tspan/60, L3.observables['MLKL_obs'],color = 'red',label = 'MLKL')
plt.plot(tspan, L4.observables['MLKLa_obs'],color = 'red',label = 'MLKLp_cal')
# # plt.plot(tspan/60, simulation_result.observables['IKKa_obs'], color = 'r', label = 'IKKa_mat')
plt.xlabel("Time (in hr)", fontsize=15)
plt.ylabel("MLKLp [Molecules/Cell]", fontsize=15)
# plt.title('MLKLp Trajectories')
# plt.legend(loc ='best')x
plt.show()