def mc_pi(n):  # Sampling n points to calculate pi.
    #import time
    import numpy as np
    #a = time.time()
    m = 0
    pi = [None] * n
    x = np.random.uniform(-1, 1, n)
    y = np.random.uniform(-1, 1, n)
    for i in range(0, n):
        if (x[i]**2 + y[i]**2) <= 1:
            m = m + 1
        pi[i] = 4.0 * m / (i + 1)
    #b = time.time() - a
    #print("Toal time: %.1fsec\n" % (b))
    return (pi[n - 1])


# use every core of CPU to parallel calculate pi, loop t times, every time sampling n points.
def pl_mc_pi(n, t):
    import time
    import sys
    import multiprocessing
    import numpy as np
    a = time.time()
    cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=cores)
    cnt = 0
    pi = [None] * t
    for y in pool.imap_unordered(mc_pi, [n] * t):
        pi[cnt] = y
        m = np.mean(pi[0:cnt + 1])
        cnt += 1
        sys.stdout.write('done %d/%d, current pi is %f\r' % (cnt, t, m))
    b = time.time() - a
    print("\nToal time: %.1fsec\n" % (b))
    return np.mean(pi)


def mc_pi_plot(n, tt):  # want to plot an animation to show the progress?
    import time
    import numpy as np
    import matplotlib.pyplot as plt
    %matplotlib osx
    plt.close()
    a = time.time()
    m = 0
    pi = [None] * n
    co = [None] * n
    x = np.random.uniform(-1, 1, n)
    y = np.random.uniform(-1, 1, n)
    plt.axis('scaled')
    plt.axis([-1, 1, -1, 1])
    for i in range(0, n):
        if (x[i]**2 + y[i]**2) <= 1:
            m = m + 1
            co[i] = 'r'
        else:
            co[i] = 'k'
        pi[i] = 4.0 * m / (i + 1)
        plt.scatter(x[i], y[i], s=0.75, marker='.', c=co[i], alpha=.5)
        if tt:
            plt.pause(tt)
    b = time.time() - a
    print("Toal time: %.1fsec\n" % (b))
    if tt:
        plt.show()
    return (pi[n - 1])
