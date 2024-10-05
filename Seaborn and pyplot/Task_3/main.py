import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

info = pd.read_csv("dataset.csv")
info_1 = pd.DataFrame(info.value_counts())
info_2 = info[info['platform'] == 'PS3']
plt.figure(figsize=(8,6))
sns.set_style("darkgrid")
plotting_info = sns.barplot(info_2,y = 'user_count', x = 'year_of_release', hue='year_of_release',saturation=1)
plotting_info.legend(title='PS3',frameon=False)
sns.move_legend(plotting_info,loc = 0,bbox_to_anchor=(1,0.6))
figure_of_plotting = plotting_info.get_figure()
figure_of_plotting.savefig("pre_project.png",bbox_inches='tight',dpi=150)
