import pylab as py
from scipy.integrate import odeint

alpha = 2/3
beta = 4/3
delta = 1.
gamma = 1.              # a, b, c and d are parameters of lotka-voltera model
x_initial = [1.6, 1.6]  # Initial Value of prey and predator
x_initial_iter = [[0.9, 0.9], [1.1, 1.1], [1.3, 1.3], [1.5, 1.5], [1.7, 1.7]]


def lotka_volterra(X, t=0):
    """ Return a list with two elements showing growth rate of prey
    and predator populations.
    """

    return [alpha*X[0] - beta*X[0]*X[1], -delta*X[1] + gamma*X[0]*X[1]]


def solve_diff(x_init, t_start=0, t_end=20, t_num=300):
    """ Function for solving differntial equation with arguments
    x_init, t_start, t_end and t_num.
    """

    t = py.linspace(t_start, t_end, t_num)
    sol = odeint(lotka_volterra, x_init, t)
    prey = sol[:, 0]
    predator = sol[:, 1]
    return [prey, predator, t]

[prey, predator, t] = solve_diff(x_initial)

size_lab = 12
size_tit = 14
color_lab = 'black'
color_tit = 'black'
style_lab = 'serif'
style_tit = 'serif'
legend_size = 14.0

f1 = py.figure()

py.plot(t, prey, 'g', label='Prey', marker='D', markersize=2, linewidth=1)
py.plot(t, predator, 'r', label='Predator', marker='D', markersize=2,
        linewidth=1)

py.axis([0, 20, 0, 3])
py.grid()
py.legend(loc='best', prop={'size': legend_size, 'family': 'serif'})
py.xlabel('Time', fontsize=size_lab, color=color_lab, fontname=style_lab)
py.ylabel('Population', fontsize=size_lab, color=color_lab, fontname=style_lab)
py.title('Evolution of Prey and Predator populations', fontsize=size_tit,
         color=color_tit, fontname=style_tit)

f1.savefig('prey_and_predator.png')


m_l = [['D', 1, 1], ['D', 1, 1], ['D', 1, 1], ['D', 1, 1],
       ['D', 1, 1], ['D', 1, 1]]
f2 = py.figure()
for i in range(0, 5):

    [prey, predator, t] = solve_diff(x_initial_iter[i])
    py.plot(prey, predator, label=x_initial_iter[i], marker=m_l[i][0],
            markersize=m_l[i][1], linewidth=m_l[i][2])

py.axis([0, 3.5, 0, 2.0])
py.grid()
py.legend(loc='best', prop={'size': legend_size})
py.xlabel('Number of Prey', fontsize=size_lab, color=color_lab,
          fontname=style_lab)
py.ylabel('Number of Predator', fontsize=size_lab, color=color_lab,
          fontname=style_lab)
py.title('Phase Space Plot', fontsize=size_tit, color=color_tit,
         fontname=style_lab)

f2.savefig('phase_space_plot.png')
