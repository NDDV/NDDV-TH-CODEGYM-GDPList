#%%
import pandas as pd
import matplotlib.pyplot as plt

# %%
df = pd.read_csv("GDPlist.csv")
df

# %%
df.info()

# %%
GDP_df= df["GDP (millions of US$)"]
GDP_df
#%%
plt.hist(GDP_df, bins = 200)
plt.title("GDP (millions of US$)")
plt.xlabel("GDP")
plt.ylabel("Số thứ tự các quốc gia")
# %%
df.Continent.value_counts()

# %%
continent_df = df.groupby(["Continent"])["GDP (millions of US$)"].sum()
continent_df

# %%
df=df.sort_values(["GDP (millions of US$)"], ascending = False)
df.head(10)

# %%
