# Elle Pickard nds3ky 

import numpy as np
import matplotlib.pyplot as plt

def Fact(G, S, kd_1, kd_2):
    """Fractional receptor activation: (kd_2*G + kd_1*S) / (kd_1*kd_2 + kd_2*G + kd_1*S)"""
    return (kd_2 * G + kd_1 * S) / (kd_1 * kd_2 + kd_2 * G + kd_1 * S) 


kd_1 = 0.38                      # Semaglutide dissociation constant [nM]
kd_2 = 0.17                     # GLP1 dissociation constant [nM]   


G_fed = 0.040                # GLP1 (fed) concentration [nM]
G_fasted = 0.015             # GLP1 (fasted) concentration [nM]
S = np.logspace(-2, 4, 500)     # ligand concentration, 0.01 to 10,000 [nM]

#Calculating fractional receptor activation for fed vs. fasted states
Fact_fed = Fact(G_fed, S, kd_1, kd_2)
Fact_fasted = Fact(G_fasted, S, kd_1, kd_2)

#Plotting graph with two curves for fed and fasted states with semiglutide competition 
plt.figure(figsize=(8,5))
plt.semilogx(S, Fact_fed, label="Fed", lw=2)
plt.semilogx(S, Fact_fasted, label="Fasted", lw=2)
plt.axhline(0.5, ls="--", c="gray", lw=1)
plt.axvline(kd_2, ls="--", c="gray", lw=1)
plt.ylim(0,1)
plt.xlabel("Semaglutide Concentration (nM)")
plt.ylabel("Fractional Receptor Activation")
plt.title("GLP-1 Receptor Activation: Fed vs. Fasted")
plt.legend()
plt.grid(alpha=0.2)

plt.show()