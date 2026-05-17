import re
import math
import pandas as pd
from collections import defaultdict

# ============================================================
# USER INPUT
# ============================================================

# Gaussian output or log file
filename = r"C:\Users\mohan\Desktop\CEVYUX\CEVYUX-Cu.log"

# ============================================================
# PERIODIC TABLE
# ============================================================

atomic_symbols = {
    1:'H', 2:'He',
    3:'Li', 4:'Be', 5:'B', 6:'C', 7:'N', 8:'O', 9:'F', 10:'Ne',
    11:'Na', 12:'Mg', 13:'Al', 14:'Si', 15:'P', 16:'S', 17:'Cl', 18:'Ar',
    19:'K', 20:'Ca', 21:'Sc', 22:'Ti', 23:'V', 24:'Cr', 25:'Mn',
    26:'Fe', 27:'Co', 28:'Ni', 29:'Cu', 30:'Zn', 31:'Ga', 32:'Ge',
    33:'As', 34:'Se', 35:'Br', 36:'Kr', 47:'Ag', 79:'Au'
}

# ============================================================
# EXTRACT FINAL COORDINATES
# ============================================================

with open(filename, 'r') as f:
    lines = f.readlines()

# Find all Standard orientation sections
indices = []
for i, line in enumerate(lines):
    if 'Standard orientation:' in line:
        indices.append(i)

if not indices:
    raise ValueError('No Standard orientation section found!')

# Use the LAST geometry (optimized structure)
start = indices[-1]

coords = []

for i in range(start + 5, len(lines)):
    line = lines[i]

    if '-----' in line:
        break

    parts = line.split()

    if len(parts) >= 6:
        center_number = int(parts[0])
        atomic_number = int(parts[1])

        x = float(parts[3])
        y = float(parts[4])
        z = float(parts[5])

        symbol = atomic_symbols.get(atomic_number, str(atomic_number))

        coords.append({
            'atom_index': center_number,
            'symbol': symbol,
            'x': x,
            'y': y,
            'z': z
        })

print(f"Total atoms extracted: {len(coords)}")

# ============================================================
# CALCULATE ALL DISTANCES
# ============================================================

all_distances = []

for i in range(len(coords)):
    for j in range(i + 1, len(coords)):

        atom1 = coords[i]
        atom2 = coords[j]

        dx = atom1['x'] - atom2['x']
        dy = atom1['y'] - atom2['y']
        dz = atom1['z'] - atom2['z']

        dist = math.sqrt(dx**2 + dy**2 + dz**2)

        pair_type = '-'.join(sorted([atom1['symbol'], atom2['symbol']]))

        all_distances.append({
            'Pair Type': pair_type,
            'Atom 1': f"{atom1['symbol']}{atom1['atom_index']}",
            'Atom 2': f"{atom2['symbol']}{atom2['atom_index']}",
            'Distance (Å)': round(dist, 4)
        })

# ============================================================
# SORT DISTANCES
# ============================================================

all_distances = sorted(all_distances, key=lambda x: (x['Pair Type'], x['Distance (Å)']))

# ============================================================
# CREATE DATAFRAME
# ============================================================

df = pd.DataFrame(all_distances)

# ============================================================
# SAVE COMPLETE TABLE
# ============================================================

output_excel = 'All_Interatomic_Distances.xlsx'
output_csv = 'All_Interatomic_Distances.csv'

df.to_excel(output_excel, index=False)
df.to_csv(output_csv, index=False)

print(f"\nSaved complete distance table:")
print(output_excel)
print(output_csv)

# ============================================================
# PRINT GROUPED SUMMARY
# ============================================================

print("\n============================================================")
print("DISTANCE SUMMARY BY ATOM TYPE")
print("============================================================")

pair_groups = defaultdict(list)

for item in all_distances:
    pair_groups[item['Pair Type']].append(item)

for pair in sorted(pair_groups.keys()):

    print(f"\n{pair}")
    print('-' * 60)

    for entry in pair_groups[pair][:20]:
        print(f"{entry['Atom 1']:>6s}  -  {entry['Atom 2']:<6s}  =  {entry['Distance (Å)']:>8.4f} Å")

# ============================================================
# OPTIONAL: SAVE INDIVIDUAL FILES FOR EACH PAIR TYPE
# ============================================================

for pair in pair_groups:

    pair_df = pd.DataFrame(pair_groups[pair])

    safe_name = pair.replace('-', '_')

    pair_df.to_csv(f'{safe_name}_distances.csv', index=False)

print("\nIndividual pair-distance files also saved.")
