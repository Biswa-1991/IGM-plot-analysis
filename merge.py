import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# ============================================================
# LIST OF .dat FILES
# ============================================================

files = [
    r"C:\Users\mohan\Desktop\CEVYUX\IGMPLOT\Cu\mol-igm.dat",
    r"C:\Users\mohan\Desktop\CEVYUX\IGMPLOT\Cu\NLI.dat",
    r"C:\Users\mohan\Desktop\CEVYUX\IGMPLOT\Cu\CUN.dat",
    r"C:\Users\mohan\Desktop\CEVYUX\IGMPLOT\Cu\agostic\Cu-igm.dat",
]

# ============================================================
# COLOR FOR EACH DATASET
# ============================================================

colors = [
    "red",
    "blue",
    "green",
    "pink",
]

# ============================================================
# LABELS
# ============================================================

labels = [
    "System 1",
    "System 2",
    "System 3",
    "System 4",
]

# ============================================================
# FIGURE
# ============================================================

fig, ax = plt.subplots(figsize=(10,7), dpi=300)

# ============================================================
# LOOP OVER FILES
# ============================================================

for file, color, label in zip(files, colors, labels):

    # Load data
    data = np.loadtxt(file, skiprows=1)

    # --------------------------------------------------------
    # According to:
    # u 1:3
    #
    # Column 1 = sign(lambda2)rho
    # Column 3 = delta g
    # --------------------------------------------------------

    x = data[:,0]
    y = data[:,2]

    # Scatter plot
    ax.scatter(
        x,
        y,
        s=8,
        c=color,
        alpha=0.7,
        linewidths=0,
        label=label
    )

# ============================================================
# AXIS LABELS
# ============================================================

ax.set_xlabel(
    r'sign($\lambda_2$)$\rho$ (a.u.)',
    fontsize=22
)

ax.set_ylabel(
    r'$\delta g$ (a.u.)',
    fontsize=22
)

# ============================================================
# AXIS LIMITS
# ============================================================

ax.set_xlim(-0.4, 0.2)
ax.set_ylim(0, 0.6)

# ============================================================
# TICKS
# ============================================================

ax.set_xticks(np.arange(-0.4, 0.21, 0.1))
ax.set_yticks(np.arange(0, 0.61, 0.05))

ax.tick_params(
    axis='both',
    which='major',
    direction='in',
    top=True,
    right=True,
    length=8,
    width=1.5,
    labelsize=18,
    pad=8
)

# ============================================================
# SPINE THICKNESS
# ============================================================

for spine in ax.spines.values():
    spine.set_linewidth(1.8)

# ============================================================
# LEGEND
# ============================================================

ax.legend(
    fontsize=16,
    frameon=False,
    loc='upper left'
)

# ============================================================
# LAYOUT
# ============================================================

plt.tight_layout()

# ============================================================
# SAVE
# ============================================================

plt.savefig(
    "Merged_IGM_plot.png",
    dpi=600,
    bbox_inches='tight'
)

# ============================================================
# SHOW
# ============================================================

plt.show()