import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Parameters
a =     [1.5, 1.5, 1.5, 1.5 ] # birth rate humans
b_h =   [0.2, 0.2, 0.2, 0.2 ] # death rate humans
g =     [0.01, 0.01, 0.01, 0.01]   # gamma capacity factor
c_i =   [0.5,  2, 0.5, 0.5]  # immunization rate
c_z =   [0.02, 0.02, 0.01, 0.02]   # zombification rate
b_z =   [0.01, 0.01, 0.01, 0.015] # death rate zombies





# System of differential equations for immune give birth to none immune
def model(y, t, a, b_h, g, c_i, c_z,b_z):
    H, I, Z = y
    dHdt = (H+I) *a - H*( b_h + c_i + g * (H + I)+ c_z * Z )
    dIdt = c_i*H + I * (- b_h - g * (H + I))
    dZdt = (c_z * H - b_z * (H + I)) * Z
    return [dHdt, dIdt, dZdt]

# Initial conditions
H0 = 100
I0 = 0
Z0 = 1
y0 = [H0, I0, Z0]
 
H=[]
I=[]
Z=[]
scenarios = [0,1,2,3]

t = np.linspace(0, 40, 100)



for s in scenarios: 
    solution = odeint(model, y0, t, args= (a[s],b_h[s],g[s], c_i[s], c_z[s], b_z[s]))
    H.append( solution[:,0])
    I.append( solution[:,1])
    Z.append( solution[:,2])

#equi solutions
solution = odeint(model, [1,1,150], t, args= (a[0],b_h[0],g[0], c_i[0], c_z[0], b_z[0]))
He = []
Ie= []
Ze = []
He.append( solution[:,0])
Ie.append( solution[:,1])
Ze.append( solution[:,2])

#increased immunization
solution2 = odeint(model, [1,1,100], t, args= (a[1],b_h[1],g[1], c_i[1], c_z[1], b_z[1]))
He.append( solution2[:,0])
Ie.append( solution2[:,1])
Ze.append( solution2[:,2])

#increased zombiefication 
solution3 = odeint(model, [1,1,100], t, args= (a[2],b_h[2],g[2], c_i[2], c_z[2], b_z[2]))
He.append( solution3[:,0])
Ie.append( solution3[:,1])
Ze.append( solution3[:,2])

#increased kill rate 
solution3 = odeint(model, [1,1,100], t, args= (a[3],b_h[3],g[3], c_i[3], c_z[3], b_z[3]))
He.append( solution3[:,0])
Ie.append( solution3[:,1])
Ze.append( solution3[:,2])

# equilibirum solution at 15,15,100

#plots
plt.figure(figsize=(15, 10))

plt.subplot(4, 2, 1)
plt.plot(t, H[0], label='Humans (H)', color='blue')
plt.plot(t, I[0], label='Immune Humans (I)', color='red')
plt.plot(t, Z[0], label='Zombies (Z)', color='green')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.title('Base case')
plt.grid(True)

plt.subplot(4, 2, 2)
plt.plot(t, He[0], label='Humans (H)', color='blue')
plt.plot(t, Ie[0], label='Immune Humans (I)', color='red')
plt.plot(t, Ze[0], label='Zombies (Z)', color='green')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.title('extreme case')
plt.grid(True)

# increased immunization

plt.subplot(4, 2, 3)
plt.plot(t, H[1], label='Humans (H)', color='blue')
plt.plot(t, I[1], label='Immune Humans (I)', color='red')
plt.plot(t, Z[1], label='Zombies (Z)', color='green')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.title('increased immunization: 2')
plt.grid(True)

plt.subplot(4, 2, 4)
plt.plot(t, He[1], label='Humans (H)', color='blue')
plt.plot(t, Ie[1], label='Immune Humans (I)', color='red')
plt.plot(t, Ze[1], label='Zombies (Z)', color='green')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.title('increased immunization:2')
plt.grid(True)


# increased zombiefication
plt.subplot(4, 2, 5)
plt.plot(t, H[2], label='Humans (H)', color='blue')
plt.plot(t, I[2], label='Immune Humans (I)', color='red')
plt.plot(t, Z[2], label='Zombies (Z)', color='green')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.title('decreased zombification: 0.01')
plt.grid(True)

plt.subplot(4, 2, 6)
plt.plot(t, He[2], label='Humans (H)', color='blue')
plt.plot(t, Ie[2], label='Immune Humans (I)', color='red')
plt.plot(t, Ze[2], label='Zombies (Z)', color='green')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.title('decreased zombification: 0.01')
plt.grid(True)


# increased kill rate
plt.subplot(4, 2, 7)
plt.plot(t, H[3], label='Humans (H)', color='blue')
plt.plot(t, I[3], label='Immune Humans (I)', color='red')
plt.plot(t, Z[3], label='Zombies (Z)', color='green')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.title('increased zombie kill rate: 0.015')
plt.grid(True)

plt.subplot(4, 2, 8)
plt.plot(t, He[3], label='Humans (H)', color='blue')
plt.plot(t, Ie[3], label='Immune Humans (I)', color='red')
plt.plot(t, Ze[3], label='Zombies (Z)', color='green')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.title('increased zombie kill rate: 0.015')
plt.grid(True)


plt.tight_layout()
plt.show()