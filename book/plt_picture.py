import matplotlib.pyplot as plt
import pandas as pd

stats = pd.read_csv("./stats2.csv")
plt.plot(stats.length, stats.unique, "bo")
plt.show()

plt.loglog(stats.length, stats.unique, "gs")
plt.show()

print(stats[stats.language == "English"])
print(stats[stats.language == "French"])

plt.figure(figsize=(10, 10))
subset = stats[stats.language == "English"]
plt.loglog(subset.length, subset.unique, "o", label="English", color="crimson")

subset = stats[stats.language == "French"]
plt.loglog(subset.length, subset.unique, "o", label="French",
           color="forestgreen")

subset = stats[stats.language == "German"]
plt.loglog(subset.length, subset.unique, "o", label="German", color="orange")

subset = stats[stats.language == "Portuguese"]
plt.loglog(subset.length, subset.unique, "o", label="Portuguese",
           color="blueviolet")
plt.legend()
plt.xlabel("Book length")
plt.ylabel("Number of unique words")
plt.savefig("lang_plot.pdf")
plt.show()
