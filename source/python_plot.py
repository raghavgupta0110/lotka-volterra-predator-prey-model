import pylab as py
from scipy.integrate import odeint


# parameters
# alpha, beta, delta and gamma are parameters of lotka-voltera model
alpha = 2/3
beta = 4/3
delta = 1.
gamma = 1.

x_initial = [1.6, 1.6]  # Initial Value of prey and predator
x_initial_iter = [[0.9, 0.9], [1.1, 1.1], [1.3, 1.3], [1.5, 1.5], [1.7, 1.7]]

with open('parameters.tex', 'w') as f:
    f.truncate()
    f.write(str("\ ".split()[0]) + "newcommand{\clp}{" + str(alpha) + "}\n")
    f.write(str("\ ".split()[0]) + "newcommand{\cet}{" + str(beta) + "}\n")
    f.write(str("\ ".split()[0]) + "newcommand{\del}{" + str(delta) + "}\n")
    f.write(str("\ ".split()[0]) + "newcommand{\gam}{" + str(gamma) + "}\n")
    f.write(str("\ ".split()[0]) + "newcommand{\init}{(" + str(x_initial[0]) +
            ", " + str(x_initial[1]) + ")}")


def lotka_volterra(X, t=0):
    """
    Return a list with two elements showing growth rate of prey
    and predator populations.

    X takes in list of [prey, predator] at time t.

    returns a two element list of rate of change of prey and predator.

    """

    return [alpha*X[0] - beta*X[0]*X[1], -delta*X[1] + gamma*X[0]*X[1]]


def solve_diff(x_init, t_start=0, t_end=20, t_num=300):
    """ Function for solving differntial equation.

    args:
    x_init = list of initial value of prey and predator.
    t_start  = Start value of time t.
    t_end    = End value of time t.
    t_num    = number of values in between t_start and t_end.
    """

    t = py.linspace(t_start, t_end, t_num)
    sol = odeint(lotka_volterra, x_init, t)
    prey = sol[:, 0]
    predator = sol[:, 1]
    return [prey, predator, t]


if __name__ == '__main__':
    [prey, predator, t] = solve_diff(x_initial)

# font name and size

    size_lab = 12           # font size of label.
    size_tit = 14           # font size of title.
    color_lab = 'black'     # label color.
    color_tit = 'black'     # title color.
    style_lab = 'serif'     # font style of label.
    style_tit = 'serif'     # font style of title.
    legend_size = 14.0      # legend font size.
    legend_style = 'serif'  # legend font style.

    f1 = py.figure()

    py.plot(t, prey, 'g', label='Prey', marker='D', markersize=2, linewidth=1)
    py.plot(t, predator, 'r', label='Predator', marker='D', markersize=2,
            linewidth=1)

    py.axis([0, 20, 0, 3])
    py.grid()
    py.legend(loc='best', prop={'size': legend_size, 'family': legend_style})
    py.xlabel('Time', fontsize=size_lab, color=color_lab, fontname=style_lab)
    py.ylabel('Population', fontsize=size_lab, color=color_lab,
              fontname=style_lab)
    py.title('Evolution of Prey and Predator populations', fontsize=size_tit,
             color=color_tit, fontname=style_tit)

    f1.savefig('prey_and_predator.png')

# Marker and linewidth

    m_l = [['D', 1, 1], ['D', 1, 1], ['D', 1, 1], ['D', 1, 1],
           ['D', 1, 1], ['D', 1, 1]]

# m_l is a list of list. The inner list consist of marker,
# markersize, and linewidth.

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
