#!/usr/bin/env python
# coding: utf-8

# # Laboratorio 1. CNYT
# *Viernes 14 de agosto de 2020*
# 
# **Nombre:** Nicolas Piñeros

# ## Experimentos basicos en computación cuántica usando Qiskit

# ### 1. Quibits, inicialización y medición

# In[6]:


# Importaciones
from qiskit import QuantumCircuit #Clase para declarar circuitos
from qiskit import execute #Funcion para ejecutar circuitos cuanticos de manera simulada 
                            #o en computador cuantico real

from qiskit import Aer #Módulo donde podemos acceder al simulador qasm
from qiskit.visualization import plot_histogram # Función para graficar el output como diagrama de barras
get_ipython().run_line_magic('matplotlib', 'inline')
# Esta último llamado me permite usar la librería mat´plotlib en el Notebook


# **1.1. Experimento:** Cuando un qubit esta inicializado en |0> el resultado de la medición debe ser, en teoria, siempre |0>(con probabilidad del 100%). 1 shot simulado

# In[4]:


# Declarar y llenar mi circuito
circuito_11 = QuantumCircuit(1,1) # 1 alambre cuantico (qubits) un alambre clásico
circuito_11.measure(0,0) # 0 se refiere al índice


# In[7]:


# Dibujamos el circuito
circuito_11.draw(output='mpl')


# In[8]:


#Ejecuto la simulación
simulador = Aer.get_backend('qasm_simulator')
ejecucion = execute(circuito_11, backend=simulador, shots=1)
resultado = ejecucion.result()
conteos = resultado.get_counts()
print(conteos)


# In[9]:


plot_histogram(conteos)


# **1.2. Experimento:** Cuando un qubit esta inicializado en |0> el resultado de la medición debe ser, en teoria, siempre |0>(con probabilidad del 100%). 1000 shots simulado

# In[10]:


# Declarar y llenar mi circuito
circuito_12 = QuantumCircuit(1,1) # 1 alambre cuantico (qubits) un alambre clásico
circuito_12.measure(0,0) # 0 se refiere al índice


# In[11]:


circuito_12.draw(output='mpl')


# In[12]:


#Ejecuto la simulación
simulador = Aer.get_backend('qasm_simulator')
ejecucion = execute(circuito_12, backend=simulador, shots=1000)
resultado = ejecucion.result()
conteos = resultado.get_counts()
print(conteos)


# In[13]:


plot_histogram(conteos)


# **1.3. Experimento:** Cuando un qubit esta inicializado en $|0>\rangle$ el resultado de la medición debe ser, en teoria, siempre $|0>\rangle$(con probabilidad del 100%). 1000 shots en computador cuantico real

# In[14]:


from qiskit import IBMQ
IBMQ.load_account()


# In[17]:


#Ejecución en un computador cuantico real
proveedor = IBMQ.get_provider('ibm-q')
comp_cuantico = proveedor.get_backend('ibmq_burlington')
ejecucion = execute(circuito_12, backend=comp_cuantico,shots=1000)

from qiskit.tools.monitor import job_monitor

job_monitor(ejecucion)

resultado = ejecucion.result()
conteos = resultado.get_counts()
print(conteos)


# In[20]:


plot_histogram(conteos)


# **1.4. Experimento:** Cuando un qubit esta inicializado en $|1>\rangle$ el resultado de la medición debe ser, en teoria, siempre $|1>\rangle$(con probabilidad del 100%). 1000 shots en computador cuantico real

# In[28]:


circuito_14 = QuantumCircuit(1,1)
circuito_14.x(0)
circuito_14.measure(0,0)


# In[22]:


circuito_14.draw(output='mpl')


# **1.5. Experimento:** Cuando un qubit esta inicializado en $|1>\rangle$ el resultado de la medición debe ser, en teoria, siempre $|1>\rangle$(con probabilidad del 100%). 1000 shots en computador cuantico real

# In[30]:


circuito_15 = QuantumCircuit(1,1)
circuito_15.x(0)
circuito_15.measure(0,0)


# **1.7. Experimento:** Cuando un qubit está inicializado en una superposición de los estados $|0\rangle$ y $|1\rangle$ (se logra aplicando la compuerta **H** al estado $|0\rangle$) dada por:
# 
# $$|\psi\rangle = \frac{1}{\sqrt{2}} |0\rangle + \frac{1}{\sqrt{2}} |1\rangle$$
# 
# El resultado de la medición debe ser o $|0\rangle$ con probabilidad del 50% o $|1\rangle$ con probabilidad del 50%. 1 shot en un simulador.

# In[31]:


circuito_17 = QuantumCircuit(1,1)
circuito_17.h(0)
circuito_17.measure(0,0)


# In[32]:


#Dibujamos el circuito
circuito_17.draw(output='mpl')


# In[39]:


ejecucion = execute(circuito_17, backend=comp_cuantico,shots=1000)

from qiskit.tools.monitor import job_monitor

job_monitor(ejecucion)

resultado = ejecucion.result()
conteos = resultado.get_counts()
print(conteos)


# In[34]:


plot_histogram(conteos)


# # 2. Suma cuántica
# *El siguiente circuito nos permite calcular el resultado de la suma 1 + 1 usando un computador cuántico*

# In[36]:


circuito_suma = QuantumCircuit(4,2)
# inicializo num_1 = 1
circuito_suma
# inicializo num_2 = 1
circuito_suma.x(1)
#
circuito_suma.barrier()
#
circuito_suma.cx(0, 3)
circuito_suma.cx(1, 3)
circuito_suma.ccx(0, 1, 2)
#
circuito_suma.measure(2, 0)
circuito_suma.measure(3, 1)
#Dibujo el circuito
circuito_suma.draw(output = 'mpl')


# In[37]:


ejecucion = execute(circuito_suma, backend=comp_cuantico,shots=1000)

job_monitor(ejecucion)

resultado = ejecucion.result()
conteos = resultado.get_counts()
print(conteos)


# In[38]:


plot_histogram(conteos)


# In[ ]:




