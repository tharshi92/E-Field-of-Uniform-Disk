# Electric Fields of Circular Charge Distributions

This repo contains two examples of calculating electric fields by numerical integration. 

# Axial Field Uniformly Charged Disk

We're interested in the axial electric field of a charged disk lying in the x-y plane. The disk has a radius R and is centred at the origin. To calculate the electric field we first construct the contribution to the field at a position z by a disk element dQ at a radius r < R. Note that any planar contributions to the field are cancelled out by another charge element 180 degrees away from dQ. This implies that the electric field is only song the z-axis. Now we have

<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;dE_z&space;=&space;\frac{dQ}{4&space;\pi&space;\epsilon_0&space;d^2}&space;\sin\alpha" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;dE_z&space;=&space;\frac{dQ}{4&space;\pi&space;\epsilon_0&space;d^2}&space;\sin\alpha" title="dE_z = \frac{dQ}{4 \pi \epsilon_0 d^2} \sin\alpha" /></a>

where

<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;d^2&space;=&space;z^2&space;&plus;&space;r^2,&space;\,\,\,&space;\sin\alpha&space;=&space;\frac{z}{d}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;d^2&space;=&space;z^2&space;&plus;&space;r^2,&space;\,\,\,&space;\sin\alpha&space;=&space;\frac{z}{d}" title="d^2 = z^2 + r^2, \,\,\, \sin\alpha = \frac{z}{d}" /></a>

If we assume the disk has a charge Q smeared over the surface then we have

<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;dE_z&space;=&space;\frac{Q&space;z&space;r}{4&space;\pi^2&space;\epsilon_0&space;R^2&space;(z^2&space;&plus;&space;r^2)^{3/2}}&space;dr&space;d\theta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;dE_z&space;=&space;\frac{Q&space;z&space;r}{4&space;\pi^2&space;\epsilon_0&space;R^2&space;(z^2&space;&plus;&space;r^2)^{3/2}}&space;dr&space;d\theta" title="dE_z = \frac{Q z r}{4 \pi^2 \epsilon_0 R^2 (z^2 + r^2)^{3/2}} dr d\theta" /></a>

in polar co-ordinates. Integrating this across the angular domain we have

<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;E_z&space;=&space;\frac{Q}{2&space;\pi&space;\epsilon_0&space;R^2}&space;\int^R_{0}&space;\frac{zr}{(z^2&space;&plus;&space;r^2)^{3/2}}&space;dr" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;E_z&space;=&space;\frac{Q}{2&space;\pi&space;\epsilon_0&space;R^2}&space;\int^R_{0}&space;\frac{zr}{(z^2&space;&plus;&space;r^2)^{3/2}}&space;dr" title="E_z = \frac{Q}{2 \pi \epsilon_0 R^2} \int^R_{0} \frac{zr}{(z^2 + r^2)^{3/2}} dr" /></a>

To integrate this on python we will first make it dimensionless:

<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\eta_z&space;=&space;\int^1_{0}&space;\frac{uv}{(v^2&space;&plus;&space;u^2)^{3/2}}&space;du" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;\eta_z&space;=&space;\int^1_{0}&space;\frac{uv}{(v^2&space;&plus;&space;u^2)^{3/2}}&space;du" title="\eta_z = \int^1_{0} \frac{uv}{(v^2 + u^2)^{3/2}} du" /></a>

where

<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\eta_z&space;=&space;\frac{2&space;\pi&space;\epsilon_0&space;R^2&space;E_z}{Q},&space;\,&space;\,&space;\,&space;u&space;=&space;\frac{r}{R},&space;\,&space;\,&space;\,&space;v&space;=&space;\frac{z}{R}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;\eta_z&space;=&space;\frac{2&space;\pi&space;\epsilon_0&space;R^2&space;E_z}{Q},&space;\,&space;\,&space;\,&space;u&space;=&space;\frac{r}{R},&space;\,&space;\,&space;\,&space;v&space;=&space;\frac{z}{R}" title="\eta_z = \frac{2 \pi \epsilon_0 R^2 E_z}{Q}, \, \, \, u = \frac{r}{R}, \, \, \, v = \frac{z}{R}" /></a>

This integral can be done analytically, and the resulting function agrees with the numerical simulation.

# Planar Field of Charged Loop

The goal is to calculate the planar electric field of a charged loop lying in the x-y plane. The loop has a radius R and is centred at the origin. To calculate the electric field we first construct the azimuthal contribution to the field at a position (r, theta) by a loop element dQ at (R, alpha):

<a href="https://www.codecogs.com/eqnedit.php?latex=dE_{\theta}&space;=&space;\frac{Q}{8&space;\pi^2&space;\epsilon_0&space;R^2}&space;\frac{\sin(\theta&space;-&space;\alpha)}{[1&space;&plus;&space;u^2&space;-&space;2&space;u&space;\cos(\theta&space;-&space;\alpha)]^{3/2}}&space;d\alpha&space;\,&space;\,&space;\,&space;\,&space;\,&space;\,&space;,&space;\,&space;\,&space;\,&space;u&space;=&space;\frac{r}{R}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?dE_{\theta}&space;=&space;\frac{Q}{8&space;\pi^2&space;\epsilon_0&space;R^2}&space;\frac{\sin(\theta&space;-&space;\alpha)}{[1&space;&plus;&space;u^2&space;-&space;2&space;u&space;\cos(\theta&space;-&space;\alpha)]^{3/2}}&space;d\alpha&space;\,&space;\,&space;\,&space;\,&space;\,&space;\,&space;,&space;\,&space;\,&space;\,&space;u&space;=&space;\frac{r}{R}" title="dE_{\theta} = \frac{Q}{8 \pi^2 \epsilon_0 R^2} \frac{\sin(\theta - \alpha)}{[1 + u^2 - 2 u \cos(\theta - \alpha)]^{3/2}} d\alpha \, \, \, \, \, \, , \, \, \, u = \frac{r}{R}" /></a>

It is worth to note that this is an integral of a periodic function with odd symmetry. As a result, the integral vanishes over any interval with length <a href="https://www.codecogs.com/eqnedit.php?latex=2&space;\pi" target="_blank"><img src="https://latex.codecogs.com/gif.latex?2&space;\pi" title="2 \pi" /></a>. Now we can construct the radial contribution to the field at a position (r, theta) by dQ:

<a href="https://www.codecogs.com/eqnedit.php?latex=dE_{r}&space;=&space;\frac{Q}{8&space;\pi^2&space;\epsilon_0&space;R^2}&space;\frac{\sqrt{u^2&space;-&space;2&space;u&space;\cos(\theta&space;-&space;\alpha)&space;&plus;&space;\cos^2(\theta&space;-&space;\alpha)}}{[1&space;&plus;&space;u^2&space;-&space;2&space;u&space;\cos(\theta&space;-&space;\alpha)]^{3/2}}&space;d\alpha" target="_blank"><img src="https://latex.codecogs.com/gif.latex?dE_{r}&space;=&space;\frac{Q}{8&space;\pi^2&space;\epsilon_0&space;R^2}&space;\frac{\sqrt{u^2&space;-&space;2&space;u&space;\cos(\theta&space;-&space;\alpha)&space;&plus;&space;\cos^2(\theta&space;-&space;\alpha)}}{[1&space;&plus;&space;u^2&space;-&space;2&space;u&space;\cos(\theta&space;-&space;\alpha)]^{3/2}}&space;d\alpha" title="dE_{r} = \frac{Q}{8 \pi^2 \epsilon_0 R^2} \frac{\sqrt{u^2 - 2 u \cos(\theta - \alpha) + \cos^2(\theta - \alpha)}}{[1 + u^2 - 2 u \cos(\theta - \alpha)]^{3/2}} d\alpha" /></a>

This is an elliptic integral that cannot be expressed as a combination of simple functions. We will now simplfy and remove units:

<a href="https://www.codecogs.com/eqnedit.php?latex=d\eta_{r}&space;=&space;\frac{u&space;-&space;\cos(\theta&space;-&space;\alpha)}{[1&space;&plus;&space;u^2&space;-&space;2&space;u&space;\cos(\theta&space;-&space;\alpha)]^{3/2}}&space;d\alpha&space;\,&space;\,&space;\,&space;\,&space;,&space;\,&space;\,&space;\,&space;\,&space;\textrm{where}&space;\,&space;\,&space;\,&space;\,&space;d\eta_r&space;=&space;\frac{8&space;\pi^2&space;\epsilon_0&space;R^2&space;dE_r}{Q}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?d\eta_{r}&space;=&space;\frac{u&space;-&space;\cos(\theta&space;-&space;\alpha)}{[1&space;&plus;&space;u^2&space;-&space;2&space;u&space;\cos(\theta&space;-&space;\alpha)]^{3/2}}&space;d\alpha&space;\,&space;\,&space;\,&space;\,&space;,&space;\,&space;\,&space;\,&space;\,&space;\textrm{where}&space;\,&space;\,&space;\,&space;\,&space;d\eta_r&space;=&space;\frac{8&space;\pi^2&space;\epsilon_0&space;R^2&space;dE_r}{Q}" title="d\eta_{r} = \frac{u - \cos(\theta - \alpha)}{[1 + u^2 - 2 u \cos(\theta - \alpha)]^{3/2}} d\alpha \, \, \, \, , \, \, \, \, \textrm{where} \, \, \, \, d\eta_r = \frac{8 \pi^2 \epsilon_0 R^2 dE_r}{Q}" /></a>

This expression will be numerically integrated to obtain the field. Note that the results agree with physical intuition.



