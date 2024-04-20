import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Comic Sans MS'

# set the style of the axes and the text color
plt.rcParams['axes.edgecolor']='#333F4B'
plt.rcParams['axes.linewidth']=0.8
plt.rcParams['xtick.color']='#333F4B'
plt.rcParams['ytick.color']='#333F4B'
plt.rcParams['text.color']='#333F4B'


data = {
       'Brain': 68,
       'Ears, Nose, Teeth, and Throat': 5, 
       'Eyes': 23,
       'Bowel': 6,
       'Breast': 25,
       'Heart and Blood Vessels': 22, 
       'Kidneys and Urinary Tract': 4,
       'Liver': 9, 
       'Lungs': 53,
       'Bones': 9, 
       'Joints': 5, 
       'Female Reproductive Organs': 11,
       'Male Reproductive Organs': 7,
       'Lymph Nodes': 6,
       'Skin': 4,
       'Multi Organs Datasets' : 23
}

df = pd.DataFrame.from_dict(data, orient='index', columns=['number'])
# df = df.sort_values(by='number')
df = df. iloc[::-1]

print(f"Number of Dataset: {df['number'].sum()}")
# print(f"Maximum Number: {df['number'].max()}")

fig, ax = plt.subplots(figsize=(8,4.2))

range_y=list(range(1,len(df.index)+1))

plt.hlines(y=range_y, xmin=0, xmax=df['number'], color='#0080ff', alpha=0.2, linewidth=5)
plt.plot(df['number'], range_y, "o", markersize=5, color='#0080ff', alpha=0.6)
    
# set labels
ax.set_xlabel('Number', fontsize=15, fontweight='black', color = '#333F4B')
ax.set_ylabel('')

# set axis
ax.tick_params(axis='both', which='major', labelsize=12)
plt.yticks(range_y, df.index)
plt.xticks(np.arange(0, np.ceil(df['number'].max()*1.1), step=10))
ax.set_xlim(0,np.ceil(df['number'].max()*1.1))

# add an horizonal label for the y axis 
fig.text(0.18, 0.92, f"Number of Datasets Listed: {df['number'].sum()}" , fontsize=15, fontweight='black', color = '#333F4B')

# change the style of the axis spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_bounds((1, len(range_y)))
ax.spines['left'].set_position(('outward', 8))
ax.spines['bottom'].set_position(('outward', 5))

plt.savefig('src/numberOfDatasets.png', dpi=300, bbox_inches='tight')
#plt.show()