#!/usr/bin/env python
# coding: utf-8

# # Cirq Notebook on Quantum Programming

# ## We are now starting to load the cirq libraries

# In[6]:


pip install --upgrade pip


# In[1]:


### In the below cell we are installing the cirq library, its a software library for writing, manipulating, and optimizing quantum circuits and then running them against quantum computers and simulators.


# In[1]:


pip install cirq


# In[4]:


import cirq


# In[3]:


print(cirq.google.Foxtail)


# In[1]:


## Basic Level Circuit


# ### The most Basic level program considering all the factors will be something which will have a certain amount of qubits, logic gates and output. Import cirq and define Grid QuBits

# In[5]:


length = 3
qubits = [cirq.GridQubit(i,j) for  i in range(length) for j in range(length)]
print(qubits)


# ## Quantum Logic Gates

# ### CNOT Gate and measurement

# In[21]:


### Define the CNOT Gate
qubit = cirq.GridQubit(0, 0)

#create a circuit
circuit = cirq.Circuit([
    cirq.X(qubit),
    cirq.measure(qubit, key = 'm') #measurement
]
)

print("Circuit:")
print(circuit)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=20)
print("Results:")
print(result)


# *Preparing the Bell State, in the below section we are going to be creating a ciruit which will be initializing a two qubit system into the Bell State*

# In[32]:


### Script for preparing the Bell state
qreg = [cirq.LineQubit (x) for x in range (2)]
circ = cirq.Circuit()

# add the Bell State preparation Circuit
circ.append([cirq.H(qreg[0]), cirq.CNOT(qreg[0], qreg[1])])
             
# display the circuit
print("Circuit:")
print(circ)

# add measurements             
circ.append(cirq.measure(*qreg, key="z"))

#simulate the circuits
sim = cirq.Simulator()
res = sim.run(circ, repetitions = 50)
             
# display the outcomes
print ("\nMeasurements:")
print (res.histogram(key="z"))


# In[8]:


### Script for preparing the X Gate
import cirq
qreg = [cirq.LineQubit (x) for x in range (2)]
circ = cirq.Circuit()

# add the Bell State preparation Circuit
circ.append([cirq.X(qreg[0])])
             
# display the circuit
print("Circuit:")
print(circ)

# add measurements             
circ.append(cirq.measure(*qreg, key="z"))

#simulate the circuits
sim = cirq.Simulator()
res = sim.run(circ, repetitions = 50)
             
# display the outcomes
print ("\nMeasurements:")
print (res.histogram(key="z"))


# Circuits can be constructed in many different ways, by default  cirq will attempt to slide your operation into the earliest possible moment when you insert it.

# In[2]:


import cirq
circuit = cirq.Circuit()
# You can create a circuit by appending to it
circuit.append(cirq.H(q) for q in cirq.LineQubit.range(4))
#All the gates are put into the same Moment since none overlap
print(circuit)


# In[6]:


### Creating a circuit directly
print(cirq.Circuit(cirq.SWAP(q, q+1) for q in cirq.LineQubit.range(3)))


# In[8]:


# Creates each gate in a separate moment.
print(cirq.Circuit(cirq.Moment([cirq.H(q)]) for q in cirq.LineQubit.range(3)))


# In[ ]:




