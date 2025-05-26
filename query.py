# File: query_table.py

import logging
import yaml
import sys
from collections import Counter
import matplotlib.pyplot as plt

# Setup logging
logging.basicConfig(
  level=logging.INFO,
  format='%(asctime)s [%(levelname)s] %(message)s',
  handlers=[logging.StreamHandler()]
)

DATA_FILE = sys.argv[1]
OUTPUT_FILE = sys.argv[2]

# Load YAML
with open(DATA_FILE, 'r') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

# Counters
drug_counts = Counter()
procedure_counts = Counter()

# Output table
output_lines = ["participant_id\tdrug_1\tdrug_2\tprocedure_1\tprocedure_2"]

for entry in data:
  participant_id = entry.get("participant_id", "")
  drug1 = entry.get("d1.name", "")
  drug2 = entry.get("d2.name", "")
  proc1 = entry.get("p1.name", "")
  proc2 = entry.get("p2.name", "")

  drug_counts[drug1] += 1
  drug_counts[drug2] += 1
  procedure_counts[proc1] += 1
  procedure_counts[proc2] += 1

  output_lines.append(f"{participant_id}\t{drug1}\t{drug2}\t{proc1}\t{proc2}")

# Write to result file
with open(OUTPUT_FILE, 'w') as file:
  file.write("\n".join(output_lines))

# ---------- PLOTS ----------

# Drug Pie Chart
fig, ax = plt.subplots()
labels = list(drug_counts.keys())
sizes = list(drug_counts.values())
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
plt.title("Drug Distribution")
plt.tight_layout()
plt.savefig("drug_distribution_pie.png")

# Procedure Bar Chart
fig, ax = plt.subplots()
labels = list(procedure_counts.keys())
sizes = list(procedure_counts.values())
ax.bar(labels, sizes, color='orange')
ax.set_title("Procedure Distribution")
ax.set_xlabel("Procedure")
ax.set_ylabel("Count")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("procedure_distribution_bar.png")

logging.info(f"Result saved to {OUTPUT_FILE}")
logging.info("Plots saved: drug_distribution_pie.png, procedure_distribution_bar.png")