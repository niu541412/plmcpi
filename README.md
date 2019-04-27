# plmcpi
parallel calculate the value of pi with Monte Carlo method, just for fun and practice.

## Usage:
- mc_pi(n), Sampling n points to calculate pi.
```python
mc_pi(1000)
```
- pl_mc_pi(n, t), use every core of CPU to parallel calculate pi, loop t times, every time sampling n points.
```python
pl_mc_pi(1000, 1000) 
```

- mc_pi_plot(n, tt), want to plot an animation to show the progress?
```python
mc_pi_plot(1000, 0.001)
```
