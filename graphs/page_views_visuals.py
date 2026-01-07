# ------------------------------------------
# Web Analytics Visual Creation Script
# ------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Mock Data
np.random.seed(42)
page_views = np.random.normal(loc=8, scale=4, size=500)
stages = ["Landing", "Product View", "Add-to-Cart", "Checkout", "Purchase"]
values = [10000, 6000, 3000, 1500, 750]
device = ["Desktop", "Mobile"]
conversion = [4.5, 1.8]

# ------------------------------------------
# 1️⃣ Histogram: Page Views
# ------------------------------------------

plt.figure(figsize=(8,5))
plt.hist(page_views, bins=20)
p25, p75 = np.percentile(page_views, [25, 75])
plt.axvline(p25, linestyle='--', color='red', label="25th %tile")
plt.axvline(p75, linestyle='--', color='red', label="75th %tile")
plt.title("Page Views per User Distribution")
plt.xlabel("Page Views")
plt.ylabel("User Count")
plt.legend()
plt.tight_layout()
plt.savefig("visuals/page_views.png")
plt.show()

# ------------------------------------------
# 2️⃣ Conversion Funnel
# ------------------------------------------

plt.figure(figsize=(8,5))
plt.plot(stages, values, marker="o")
highest_dropoff_stage = values.index(max(np.diff(values, prepend=0), key=abs))
plt.axvline(highest_dropoff_stage, linestyle='--', color='red')
plt.title("Customer Journey Funnel")
plt.ylabel("Users")
plt.grid()
plt.tight_layout()
plt.savefig("visuals/funnel.png")
plt.show()

# ------------------------------------------
# 3️⃣ Device Conversion Comparison
# ------------------------------------------

plt.figure(figsize=(7,5))
sns.barplot(x=device, y=conversion)
c25, c75 = np.percentile(conversion, [25, 75])
plt.axhline(c25, linestyle='--', color='red')
plt.axhline(c75, linestyle='--', color='red')
plt.title("Conversion Rate by Device")
plt.ylabel("Conversion %")
plt.tight_layout()
plt.savefig("visuals/device_performance.png")
plt.show()

# ------------------------------------------



# =====================================================
# Google Colab Download Helper
# =====================================================
try:
    from google.colab import files
    for f in os.listdir("visuals"):
        files.download(f"visuals/{f}")
except:
    print("Download available only in Google Colab 🎓")

plt.show()


# needed this line to download file
files.download(file_name)

# This to prepare the file
file_name = "city_noise_responses_categories.png"
plt.savefig(file_name, dpi=300, bbox_inches="tight")
