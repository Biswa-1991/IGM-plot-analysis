import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# ============================================================
# FILE PATH
# ============================================================

filename = r"C:\Users\mohan\Desktop\CEVYUX\IGMPLOT\Cu\agostic\Cu-igm.dat"

# ============================================================
# LOAD DATA
# ============================================================

# Skip header line
data = np.loadtxt(filename, skiprows=1)

# ------------------------------------------------------------
# According to:
# plot "mol-igm.dat" u 1:3:5
#
# Column 1 = sign(lambda2)rho
# Column 3 = delta g
# Column 5 = qg descriptor
# ------------------------------------------------------------

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
    cmap='jet',      # Similar to gnuplot rgbformulae 22,13,-31
    s=8,             # Point size
    alpha=0.95,
    linewidths=0,
    vmin=1,
    vmax=4
)

# ============================================================
# AXIS LABELS
# ============================================================

ax.set_xlabel(
    r'sign($\lambda_2$)$\rho$ (a.u.)',
    fontsize=20
)

ax.set_ylabel(
    r'$\delta g$ (a.u.)',
    fontsize=20
)

# ============================================================
# AXIS LIMITS
# ============================================================

# Adjusted to match your uploaded figure

ax.set_xlim(-0.4, 0.2)
ax.set_ylim(0, 1)

# ============================================================
# TICKS
# ============================================================

ax.tick_params(
    axis='both',
    which='major',
    direction='in',
    top=True,
    right=True,
    length=6,
    width=1.3,
    labelsize=14
)

# Major tick spacing

ax.xaxis.set_major_locator(MultipleLocator(0.1))
ax.yaxis.set_major_locator(MultipleLocator(0.1))

# ============================================================
# SPINE THICKNESS
# ============================================================

for spine in ax.spines.values():
    spine.set_linewidth(1.5)

# ============================================================
# COLORBAR
# ============================================================

cbar = plt.colorbar(sc, ax=ax, pad=0.02)

cbar.set_label(
    r'$q_g$',
    fontsize=18
)

cbar.ax.tick_params(
    direction='in',
    length=5,
    width=1.2,
    labelsize=12
)

# ============================================================
# OPTIONAL GRID
# ============================================================

# Uncomment if needed
# ax.grid(alpha=0.2)

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