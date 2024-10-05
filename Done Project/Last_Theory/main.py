import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

info = pd.read_csv("dataset.csv")

info_1=pd.DataFrame(info[['platform','genre']].value_counts())
info_1 = info_1.reset_index(drop=False)
info_1.rename({0:'count'},axis='columns',inplace=True)

PS4 = info_1[info_1['platform'] == 'PS4']
PS4= PS4.sort_values(by='genre')

XOne = info_1[info_1['platform'] == 'XOne']
XOne= XOne.sort_values(by='genre')

PC = info_1[info_1['platform'] == 'PC']
PC= PC.sort_values(by='genre')

WiiU = info_1[info_1['platform'] == 'WiiU']
WiiU= WiiU.sort_values(by='genre')

info_new=pd.concat([PS4,XOne,PC,WiiU])



sns.set_style("darkgrid")
plt.figure(figsize=(10,6))

plotting = sns.barplot(data=info_new,x='platform',y='count',hue='genre',saturation=0.9)
sns.set_style("whitegrid")
plotting.legend(frameon=False,title='genre')
sns.move_legend(plotting,loc=0,bbox_to_anchor=(1,0.8))
figure= plotting.get_figure()
figure.savefig('project_done.png',bbox_inches='tight',dpi=300)