import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Parameters
a = [1.5, 1.5] # birth rate humans
b_h = [0.01, 0.2] # death rate humans
g = [0.01, 0.01]   # gamma capacity factor
c_i = [0.01, 0.5]  # immunization rate
c_z = [0.03, 0.02]   # zombification rate
b_z = [0.01, 0.01]  # death rate zombies



# System of differential equations base case
def model1(y, t, a, b_h, g, c_i, c_z,b_z):
    H, I, Z = y
    dHdt = H *a - H*( b_h + c_i + g * (H + I)+ c_z * Z )
    dIdt = c_i*H + I * (a- b_h - g * (H + I))
    dZdt = (c_z * H - b_z * (H + I)) * Z
    return [dHdt, dIdt, dZdt]

# System of differential equations immune have decreased birth rate
def model2(y, t, a, b_h, g, c_i, c_z,b_z):
    H, I, Z = y
    dHdt = H *a - H*( b_h + c_i + g * (H + I)+ c_z * Z )
    dIdt = c_i*H + I * (a*0.5- b_h - g * (H + I))
    dZdt = (c_z * H - b_z * (H + I)) * Z
    return [dHdt, dIdt, dZdt]

# System of differential equations for immune give birth to none immune
def model3(y, t, a, b_h, g, c_i, c_z,b_z):
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
scenarios = [0,1]

t = np.linspace(0, 10, 100)


for s in scenarios: # model 1
    solution = odeint(model1, y0, t, args= (a[s],b_h[s],g[s], c_i[s], c_z[s], b_z[s]))
    H.append( solution[:,0])
    I.append( solution[:,1])
    Z.append( solution[:,2])

for s in scenarios: #model 2
    solution = odeint(model2, y0, t, args= (a[s],b_h[s],g[s], c_i[s], c_z[s], b_z[s]))
    H.append( solution[:,0])
    I.append( solution[:,1])
    Z.append( solution[:,2])

for s in scenarios: # model 3
    solution = odeint(model3, y0, t, args= (a[s],b_h[s],g[s], c_i[s], c_z[s], b_z[s]))
    H.append( solution[:,0])
    I.append( solution[:,1])
    Z.append( solution[:,2])

#plots
plt.figure(figsize=(25, 10))

plt.subplot(3, 2, 1)
plt.plot(t, H[0], label='Humans (H)', color='blue')
plt.plot(t, I[0], label='Immune Humans (I)', color='red')
plt.plot(t, Z[0], label='Zombies (Z)', color='green')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.title('Base case 1')
plt.grid(True)


plt.subplot(3, 2, 2)
plt.plot(t, H[1], label='Humans (H)', color='blue')
plt.plot(t, I[1], label='Immune Humans (I)', color='red')
plt.plot(t, Z[1], label='Zombies (Z)', color='green')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.title('Base case 2')
plt.grid(True)
##############################################scenario 2
plt.subplot(3, 2, 3)
plt.plot(t, H[2], label='Humans (H)', color='blue')
plt.plot(t, I[2], label='Immune Humans (I)', color='red')
plt.plot(t, Z[2], label='Zombies (Z)', color='green')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.title('decreased birth rate 1')
plt.grid(True)

plt.subplot(3, 2, 4)
plt.plot(t, H[3], label='Humans (H)', color='blue')
plt.plot(t, I[3], label='Immune Humans (I)', color='red')
plt.plot(t, Z[3], label='Zombies (Z)', color='green')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.title('decreased birth rate 2')
plt.grid(True)


##############################################scenario 2
plt.subplot(3, 2, 5)
plt.plot(t, H[4], label='Humans (H)', color='blue')
plt.plot(t, I[4], label='Immune Humans (I)', color='red')
plt.plot(t, Z[4], label='Zombies (Z)', color='green')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.title('no immune births 1')
plt.grid(True)

plt.subplot(3, 2, 6)
plt.plot(t, H[5], label='Humans (H)', color='blue')
plt.plot(t, I[5], label='Immune Humans (I)', color='red')
plt.plot(t, Z[5], label='Zombies (Z)', color='green')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.title('no immune births 2')
plt.grid(True)


plt.tight_layout()
plt.show()