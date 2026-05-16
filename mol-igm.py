import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib import rcParams

# ============================================================
# GLOBAL FONT SETTINGS
# ============================================================

rcParams['font.family'] = 'Times New Roman'
rcParams['mathtext.fontset'] = 'custom'
rcParams['mathtext.rm'] = 'Times New Roman'
rcParams['mathtext.it'] = 'Times New Roman:italic'
rcParams['mathtext.bf'] = 'Times New Roman:bold'

# ============================================================
# FILE PATH
# ============================================================

filename = r"C:\Users\mohan\Desktop\CEVYUX\IGMPLOT\Cu\total.dat"

# ============================================================
# LOAD DATA
# ============================================================

data = np.loadtxt(filename, skiprows=1)

x = data[:, 0]
y = data[:, 2]
qg = data[:, 4]

# ============================================================
# CREATE FIGURE
# ============================================================

fig, ax = plt.subplots(figsize=(10, 7), dpi=300)

# ============================================================
# SCATTER PLOT
# ============================================================

sc = ax.scatter(
    x,
    y,
    c=qg,
    cmap='jet',
    s=8,
    alpha=0.95,
    linewidths=0,
    vmin=1,
    vmax=4
)

# ============================================================
# AXIS LABELS
# ============================================================

ax.set_xlabel(
    r'$\mathbf{sign}(\boldsymbol{\lambda_2})\boldsymbol{\rho}\ \mathbf{(a.u.)}$',
    fontsize=24,
    fontweight='bold'
)

ax.set_ylabel(
    r'$\boldsymbol{\delta g}\ \mathbf{(a.u.)}$',
    fontsize=24,
    fontweight='bold'
)

# ============================================================
# AXIS LIMITS
# ============================================================

ax.set_xlim(-0.4, 0.2)
ax.set_ylim(0, 0.8)

# ============================================================
# TICKS
# ============================================================

ax.tick_params(
    axis='both',
    which='major',
    direction='out',
    top=False,
    right=False,
    bottom=True,
    left=True,
    length=6,
    width=3,
    labelsize=20
)

ax.xaxis.set_major_locator(MultipleLocator(0.1))
ax.yaxis.set_major_locator(MultipleLocator(0.2))

# Bold tick labels
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontweight('bold')
    label.set_fontname('Times New Roman')

# ============================================================
# SPINE THICKNESS
# ============================================================

for spine in ax.spines.values():
    spine.set_linewidth(3.0)

# ============================================================
# COLORBAR
# ============================================================

cbar = plt.colorbar(sc, ax=ax, pad=0.02)

cbar.set_label(
    r'$\boldsymbol{q_g}$',
    fontsize=20,
    fontweight='bold'
)

cbar.ax.tick_params(
    direction='out',
    length=5,
    width=3,
    labelsize=20,
)

# Bold colorbar ticks
for label in cbar.ax.get_yticklabels():
    label.set_fontweight('bold')
    label.set_fontname('Times New Roman')

# ============================================================
# LAYOUT
# ============================================================

plt.tight_layout()

# ============================================================
# SAVE FIGURE
# ============================================================

plt.savefig(
    "IGM_qg_plot.png",
    dpi=600,
    bbox_inches='tight'
)

# ============================================================
# SHOW PLOT
# ============================================================

plt.show()