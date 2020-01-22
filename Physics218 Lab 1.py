#!/usr/bin/env python
# coding: utf-8

# In[68]:


import numpy as np


# $\alpha = \frac {\Delta L} {L*\Delta T}$

# $\delta Q = Q \sqrt{(m\frac{\delta A}{A})^2 + (n\frac{\delta B}{B})^2 + (o\frac{\delta C}{C})^2}$

# $\Delta T = T_f - T_i$

# $\delta Q = \sqrt{(\delta A)^2 + (\delta B)^2}$

# In[69]:


def thermo (deltaL,L,deltaT):
    alpha = deltaL/(L*deltaT)
    return alpha

deltaL = .00125 
L = 1.05
deltaT = 69.1 

alpha = thermo(deltaL,L,deltaT)
print("Alpha = ",alpha,"Degrees C^-1")


# In[70]:


### RULE 3 ###

def Qerror3(Aerror3,Berror3):
    qe3 = ((Aerror3**2)+(Berror3**2))**(1/2)
    return qe3

Aerror3 = .3
Berror3 = .1

Q_Error_3 = Qerror3(Aerror3,Berror3)
print("Error in Delta T = ",Q_Error_3,"Degrees C") 


# In[71]:


### RULE 4 ###

def Qerror4(Q,Aerror4,A4,Berror4,B4,Cerror4,C4,m,n,o):
    qe4 = Q*(((((m*(Aerror4/A4))**2)+(n*(Berror4/B4))**2)+(o*(Cerror4/C4))**2)**(1/2))
    return qe4

Q = 1.7228309558266145e-05
A4 = .00125
B4 = 1.05
C4 = 69.1
Aerror4 = .00001
Berror4 = .001 
Cerror4 = 0.31622776601683794
m = 1
n = -1
o = -1

Q_Error_4 = Qerror4(Q,Aerror4,A4,Berror4,B4,Cerror4,C4,m,n,o)
print("Error in Alpha = ",Q_Error_4,"Degrees C^-1")


# In[ ]:




