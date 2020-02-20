# Electric Fields of Circular Charge Distributions

This repo contains two examples of calculating electric fields by numerical integration. 

# Uniformly Charged Disk

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

# TODO: Planar Field of Charged Loop 