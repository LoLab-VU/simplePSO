try:
    import matplotlib

    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    plot = True
except ImportError:
    plot = False
    pass

import numpy as np
from necro_uncal_new_updated import model
# from pysb.integrate import Solver
import scipy.interpolate
from pysb.integrate import *
from simplepso.pso import PSO
import collections

# new_start =  np.load('optimizer_best_5000_all_new_2.npy')

start = np.array([-1.00225162,-3.55869791,-1.90399644, -1.65646416 ,-2.70609458,-3.8963345   ,
                  -2.3801572 ,-3.37514841,-3.34759048, -3.00399653 ,-3.0848272 ,-1.26296845  ,
                  -2.96167494,-3.22252192,-7.2842393 , -5.35432838 ,-1.2263877 ,-2.85525137  ,
                  -2.57487899, 0.48436482,-0.96044932, -5.92950153 ,-1.24823338,-4.37561893  ,
                  -3.82638097,-2.20471678,-0.40339438, -0.06527514 ,-3.28278697,-6.27342939  ,
                  -2.03870477, 0.41308922,-2.27304972,  1.81173972 ,-2.76739579,-6.00313583  ,
                   1.1912514 ,-4.25131413,-2.52552199, -3.56185531])

start2  = np.array([-8.09429697e-01 ,-9.37396748e-01 ,-2.49838416e+00 ,-1.56891444e+00 ,
  -1.97564501e+00, -2.91681464e+00, -1.21498551e-02, -8.97901635e-01,
  -1.26688508e+00, -2.76750743e+00, -2.96540419e+00, -6.79323586e-01,
   1.54624474e+00, -8.74796683e-01, -1.52321549e+00, -2.64133597e+00,
  -8.59453166e-01, -1.58466625e+00, -2.01465273e-01, -1.26856454e+00,
   4.19045597e+00, -1.92619073e+00,  3.23216049e+00,  1.03054444e-01,
   9.16643850e-01,  3.42070231e+00,  2.00386980e+00, -6.01837900e-01,
   1.11276134e+00, -1.69859445e+00,  3.67665123e+00, -1.78697586e+00,
   1.28108171e+00,  1.45648689e+00,  1.59245102e+00, -3.71949116e+00,
  -4.43194729e+00, -2.44828585e+00,  4.08330419e-01,  2.94010281e-01])

start3 = np.array([-1.18283093 ,-0.26728024 ,-2.2313471  ,-1.58341688 ,-1.98251115,-3.793315  ,
          -0.48793422 ,-0.67476851 , 0.04134961 ,-3.60958836 ,-5.39195483,-1.57560256,   
          -0.05445229 ,-1.21873346 ,-1.90764296 ,-4.26275975 ,-1.00705933,-1.86825905,   
          -1.48580697 ,-1.86968071 , 3.70861183 ,-2.93769572 , 4.88173226, 0.13688775,   
          -0.10593204 , 3.60321618 ,-0.03406283 ,-1.02863234 , 2.8962784 ,-2.05488278,   
           2.99330352 ,-2.89483663 , 0.99400913 , 0.91455076 ,-0.84541177,-3.3345754 ,
          -3.25684876 ,-1.76577659 ,-0.32568681 , 1.48462079])

model.enable_synth_deg()
obs_names = ['MLKLa_obs']
mlkl_obs = 'MLKLa_obs'


# Defining a few helper functions to use
def normalize(trajectories):
    """Rescale a matrix of model trajectories to 0-1"""
    ymin = trajectories.min(0)
    ymax = trajectories.max(0)
    return (trajectories - ymin) / (ymax - ymin)


def extract_records(recarray, names):
    """Convert a record-type array and list of names into a float array"""
    return np.vstack([recarray[name] for name in names]).T
t = np.array([0, 30, 90, 270, 480,600, 720, 840, 960])

# t = np.linspace(0, 720, 13)
solver1 = ScipyOdeSimulator(model, tspan=t)

y100 = np.array([0, 0.00885691708746097,0.0161886154261265,0.0373005242261882,
                  0.2798939020159581, 0.510, .8097294067, 0.95,0.98])
y10 = np.array([0, 0.0106013664572332,0.00519576571714913,0.02967443048221,0.050022163974868,
                0.088128107774737, 0.17, 0.30055140114867, 0.47])

sd100 = np.array([0., 0., 0., 0., 0.10, 0.25, 0.5, 0.75, 1.])
sd10 = np.array([0., 0., 0., 0., 0.10, 0.25, 0.5, 0.75, 1.])

data = collections.OrderedDict([('t100', y100), ('t10', y10)])
ydata_norm = y100
rate_params = model.parameters_rules()
# print(len(rate_params))
param_values = np.array([p.value for p in model.parameters])
# print(len(param_values))
rate_mask = np.array([p in rate_params for p in model.parameters])
# print(len(rate_mask))
# quit()
original_values = np.array([p.value for p in model.parameters])
# We search in log10 space for the parameters
log10_original_values = np.log10(original_values[rate_mask])

# We will use a best guess starting position for the model, up or down 1 order of magnitude
#start_position = log10_original_values #+ np.random.uniform(-3., 3., size=np.shape(log10_original_values)) #[-1.5, 1.3,
                                          #-.75]  # np.random.uniform(-1.5, 1.5, size=np.shape(log10_original_values))
# Defining some functions to help plot the output of the parameters
def display(parameter_2):
    # Y = np.copy(parameter_1)
    # param_values[rate_mask] = 10 ** Y
    # solver.run(param_values)
    # ysim_array_1 = extract_records(solver.yobs, obs_names)
    # ysim_norm_1 = normalize(ysim_array_1)
    Y = np.copy(parameter_2)
    param_values[rate_mask] = 10 ** Y
    # rate_params = 10 ** Y

    t10_params = np.copy(param_values)
    t10_params[0] = 233
    ko_pars = [param_values, t10_params]

    result = solver1.run(param_values=ko_pars) #, num_processors=10)

    ysim_array11 = result.observables[0]['MLKLa_obs']
    ysim_array22 = result.observables[1]['MLKLa_obs']

    # ysim_array = extract_records(solver.yobs, obs_names)
    ysim_norm11 = normalize(ysim_array11)
    ysim_norm22 = normalize(ysim_array22)


    mlkl_100 = np.array([0.001, 0.05, 0.05, 0.05, 0.05, 0.2, 0.05, 0.05, 0.05])
    mlkl_10= np.array([0.001, 0.05,0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05])


    var_data = collections.OrderedDict([('t100_var', mlkl_100), ('a20_var', mlkl_10)])

    ysim = collections.OrderedDict([('t100_sim', ysim_norm11), ('t10_sim', ysim_norm22)])

    # solver1.run(param_values)
    # ysim_array_2 = solver.yobs['MLKLa_obs']
    # ysim_norm_2 = normalize(ysim_array_2)
    # ['red', 'green', 'black', 'purple', 'orange']
    # param_values[rate_mask] = 10 ** log10_original_values
    # solver.run(param_values)
    # ysim_array_3 = solver.yobs['MLKLa_obs']
    # ysim_norm_3 = normalize(ysim_array_3)

    # colors = [cmap(i) for i in np.linspace(0, 1, 5)]

    # c = ['red', 'green', 'black','purple', 'cyan']
    # d = ['red', 'green', 'black','purple', 'cyan']
    # # colors = ['red', 'green', 'black', 'purple', 'orange']
    # for i,j,k,l,m in zip(data, ysim,c, d, var_data):
    #     plt.figure()
    #     # plt.plot(t, ysim_norm_3[:, 0], '-^', linewidth=5, label='Ideal P')
    #     # plt.plot(t, ysim_norm_3[:, 1], '-^', linewidth=5, label='Ideal C')
    #     # plt.plot(t, ysim_norm_1[:, 0], '->', label='Starting P')
    #     # plt.plot(t, ysim_norm_1[:, 1], '->', label='Starting C')
    #     # plt.plot(t/60, data[i], color = 'purple',label='Noisy Mlklp{}'.format(i))
    #     plt.plot(t / 60, wty,'--', color='black', label='Ctrl Mlklp')
    #     # plt.errorbar(t/60,data[i] , yerr=var_data[m],fmt='o', capsize=5, label='Noisy Mlklp{}'.format(i))
    #     plt.fill_between(t/60, data[i] - var_data[m], data[i] + var_data[m], facecolor='purple', label = '{}'.format(m), interpolate=True, alpha=.3)
    #
    #     # plt.plot(t, norm_noisy_data_C, label='Noisy C')
    #     plt.plot(t/60, ysim[j],color = 'black',label='Best fit Mlklp {}'.format(j))
    #     # plt.plot(t, ysim_norm_2[:, 1], 'o', label='Best fit C')
    #     plt.legend(loc=0)
    #     plt.ylabel('molecules/cell')
    #     plt.xlabel('time (hrs)')
    #     plt.tight_layout()
    #     plt.savefig('necroptosis_kds_all_75_5000_start2l.png', format='png')
    # plt.show()
    # plt.close()

# Here we define the cost function. We pass it the parameter vector, unlog it, and pass it to the solver.
# We choose a chi square cost function, but you can provide any metric of you choosing
# It must return a tuple
def obj_function(parameter_2):
    Y = np.copy(parameter_2)
    param_values[rate_mask] = 10 ** Y
    # rate_params = 10 ** Y

    t10_params = np.copy(param_values)
    t10_params[0] = 233
    ko_pars = [param_values, t10_params]

    result = solver1.run(param_values=ko_pars) #,num_processors =50)
    # solver2.run(param_values=a20_params)
    # solver3.run(param_values=tradd_params)
    # solver4.run(param_values=fadd_params)
    # solver5.run(param_values=c8_params)

    # list = [y1, y2, y3, y4, y5]
    # for i in list:
    ysim_array1 = result.observables[0]['MLKLa_obs']
    ysim_array2 = result.observables[1]['MLKLa_obs']

    # ysim_array = extract_records(solver.yobs, obs_names)
    ysim_norm1 = normalize(ysim_array1)
    ysim_norm2 = normalize(ysim_array2)

    # mlkl_var = np.var(y)
    mlkl_100 = np.array([0.001, 0.05, 0.05, 0.05, 0.05, 0.2, 0.05, 0.05, 0.05])
    mlkl_10= np.array([0.001, 0.05,0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05])

    e1 = np.sum((ydata_norm - ysim_norm1) ** 2 / (mlkl_100))
    e2 = np.sum((y10 - ysim_norm2) ** 2 / (mlkl_10))

    error = e1 + e2
    return error,



# def run_example():
#     best_pars = np.zeros((10000, len(model.parameters)))
#     counter = 0
#     for i in range(10000):
#     # Here we initialize the class
#     # We must proivde the cost function and a starting value
#         optimizer = PSO(cost_function=obj_function, start=start, verbose=True)
#         # We also must set bounds. This can be a single scalar or an array of len(start_position)
#         optimizer.set_bounds(parameter_range=3)
#         optimizer.set_speed(speed_min=-.25, speed_max=.25)
#         optimizer.run(num_particles=100, num_iterations=1000)
#         fitness, positions = optimizer.return_ranked_populations()  # at end of PSO for all # particles, rank by cost function value
#         hist_all = optimizer.all_history
#         fit_all = optimizer.all_fitness
#         np.save('position_pso', positions)  # param vectors for 1000 particles
#         np.save('values_cost_pso', fitness)  # cost function for each iteration of 1000 particles
#         np.save('his_all_pso', hist_all)
#         np.save('fit_all_pso', fit_all)
#         # print(fitness)
#         Y = np.copy(optimizer.best)
#         param_values[rate_mask] = 10 ** Y
#         # print(param_values)
#         if optimizer.values.min() < 5.0:
#             best_pars[counter, :] = param_values
#             print(best_pars[0:10, :])
#             counter += 1
#         print(i, counter)
#         print(optimizer.best) # what it takes here is the best set of parameter
#         np.save('necro_tnf100_10_optimizer_best_10000_%s' % i, optimizer.best)

def run_example2():
    counter = 0
    # print('run_example')
    # Here we initial the class
    # We must proivde the cost function and a starting value
    optimizer = PSO(cost_function=obj_function,start = log10_original_values, verbose=True)
    # We also must set bounds. This can be a single scalar or an array of len(start_position)
    optimizer.set_bounds(parameter_range=3)
    optimizer.set_speed(speed_min=-.25, speed_max=.25)
    optimizer.run(num_particles=100, num_iterations=500)
    print(optimizer.best)
    counter += 1
    print(counter)
    np.save('necro_optimizer_best_100_500_5_5',optimizer.best)
    # print('whatever')
#     if plot:
#          display(optimizer.best)

if '__main__' == __name__:
    run_example2()

# def run_example():
#     best_pars = np.zeros((10000, len(model.parameters)))
#
#     counter = 0
#     for i in range(10000):
#          pso = PSO(save_sampled=False, verbose=False, num_proc=8)
#          pso.set_cost_function(obj_function)
#          pso.set_start_position(log10_original_values)
#          pso.set_bounds(2)
#          pso.set_speed(-.25, .25)
#          pso.run(1000, 500)
#          # np.save('/home/ildefog/ParticleSwarmOptimization/simplepso/examples/pso_vals', pso.values) #cost function for PSO runs
#          # ranked_values = PSO.return_ranked_populations() #at end of PSO for all # particles, rank by cost function value
#          #
#          # np.save('/home/ildefog/ParticleSwarmOptimization/simplepso/examples', )
#
#          Y=np.copy(pso.best)
#          param_values[rate_mask] = 10 ** Y
#          print(param_values)
#          if pso.values.min() < 10.0:
#             best_pars[counter,:] = param_values
#             print(best_pars[0:10,:])
#             counter += 1
#          print (i, counter)
#
#     np.save('/home/ildefog/ParticleSwarmOptimization/simplepso/examples', best_pars)
#
# def run_example():
#     pso = PSO(verbose=True, save_sampled=True)
#     pso.set_cost_function(obj_function)
#     pso.set_start_position(log10_original_values)
#     pso.set_bounds(lower=2, upper=2)
#     pso.set_speed(-.25, .25)
#     pso.run(25, 5)
#     fitness,positions = pso.return_ranked_populations()  # at end of PSO for all # particles, rank by cost function value
#     hist_all = pso.all_history
#     fit_all = pso.all_fitness
#     # print('fitness, particles')
#     # print(fitness)
#     # print('position rank')
#     # print(positions)
#     # print('all history')
#     # print(hist_all)
#     # print('fit all iterations')
#     # print(fit_all)
#     if plot:
#         display(pso.best)
#     display(pso.best)
#     np.save('position_pso', positions) # param vectors for 1000 particles
#     np.save('values_cost_pso', fitness) #cost function for each iteration of 1000 particles
#     np.save('his_all_pso', hist_all)
#     np.save('fit_all_pso', fit_all)
#
#
# if __name__ == '__main__':
#     run_example()

#
# def run_example():
#     # print('run_example')
#     # Here we initial the class
#     # We must proivde the cost function and a starting value
#     optimizer = PSO(cost_function=obj_function,start = new_start, verbose=True)
#     # We also must set bounds. This can be a single scalar or an array of len(start_position)
#     optimizer.set_bounds(parameter_range=2)
#     optimizer.set_speed(speed_min=-.25, speed_max=.25)
#     optimizer.run(num_particles=50, num_iterations=500)
#     print(optimizer.best)
#     np.save('optimizer_best_50_500_mar11',optimizer.best)
# #     # print('whatever')
# #     if plot:
# # 	 display(optimizer.best)
# #     #
# #     #     print("Original values {0}".format(log10_original_values ** 10))
# #     #     print("Starting values {0}".format(start_position ** 10))
# #     #     print("Best PSO values {0}".format(optimizer.best ** 10))
# #     #     fig = plt.figure()
# #     #     fig.add_subplot(221)
# #     #     plt.scatter(log10_original_values[0], log10_original_values[1], marker='>', color='b', label='ideal')
# #     #     plt.scatter(start_position[0], start_position[1], marker='^', color='r', label='start')
# #     #     plt.scatter(optimizer.history[:, 0], optimizer.history[:, 1], c=optimizer.values, cmap=plt.cm.coolwarm)
# #     #
# #     #     fig.add_subplot(223)
# #     #     plt.scatter(log10_original_values[0], log10_original_values[2], marker='>', color='b', label='ideal')
# #     #     plt.scatter(start_position[0], start_position[2], marker='^', color='r', label='start')
# #     #     plt.scatter(optimizer.history[:, 0], optimizer.history[:, 2], c=optimizer.values, cmap=plt.cm.coolwarm)
# #     #
# #     #     fig.add_subplot(222)
# #     #     plt.scatter(log10_original_values[1], log10_original_values[2], marker='>', color='b', label='ideal')
# #     #     plt.scatter(start_position[1], start_position[2], marker='^', color='r', label='start')
# #     #     plt.scatter(optimizer.history[:, 1], optimizer.history[:, 2], c=optimizer.values, cmap=plt.cm.coolwarm)
# #     #
# #     #     fig.add_subplot(224)
# #     #     plt.legend(loc=0)
# #     #     plt.colorbar()
# #     #     plt.tight_layout()
# #     #     plt.savefig('population_necro.png')
# #     #     plt.show()
# #
# #
# if '__main__' == __name__:
#     run_example()
