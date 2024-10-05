# Working with `seaborn` library

## Now we will be learning about last library `seaborn` with a bit of `matplotlib.pyplot` library

These libraries will help us construct the bar chart like our target:<br>
![](project.png "project")
Starting with `seaborn` library: <br>

#### We are gonna use these functions:
`seaborn.barplot(data=None, *, x=None, y=None, hue=None, order=None, hue_order=None, estimator='mean', errorbar=('ci', 95), n_boot=1000, seed=None, units=None, weights=None, orient=None, color=None, palette=None, saturation=0.75, fill=True, hue_norm=None, width=0.8, dodge='auto', gap=0, log_scale=None, native_scale=False, formatter=None, legend='auto', capsize=0, err_kws=None, ci=<deprecated>, errcolor=<deprecated>, errwidth=<deprecated>, ax=None, **kwargs)` as you can see there are a lot of parameters for plotting bar chart in seaborn, but we will use only a few of them like:<br>
-`data` = *dataDataFrame, Series, dict, array, or list of arrays* which is dataset to plot <br>
-`x,y,hue` = names of variables in `data` which are the inputs for plotting long-form data<br>
-`saturation` = float for setting saturation of the plotting chart<br>
More on [seaborn manual](https://seaborn.pydata.org/index.html)<br>
<br>
`seaborn.set_style(style=None, rc=None)`
to set style where <br>
-`style` = *dict,or one of {darkgrid,whitegrid,dark,white,ticks}* for styling and <br> 
-`rc` = *dict,optional* for overriding the values in the present seaborn style dictionaries.<br>
<br>
Ex:<br>
`sns.set_style("whitegrid")`<br>
`sns.barplot(x=["A", "B", "C"], y=[1, 3, 2])`<br>
![](set_style_1_0.png)<br>
Or<br>
`sns.set_style("darkgrid")`<br>
`sns.barplot(x=["A", "B", "C"], y=[1, 3, 2])`<br>
![](set_style_2_0.png)<br>

`matplotlib.axes.Axes.legend(title, frameon, *args, **kwargs)`<br>
-`title` = *str* to name the title of legend<br>
-`frameon` = boolean, whether to have frame on the legend or not<br>
-[other arguments](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend)<br>
This is used to plot legends which describe the bars of our chart.<br>
Don't be scared of this function, as you can see we need `matplotlib.axes.Axes` type data for using `legend()` function and it can be succeeded by doing so<br>
`sns.set_style("darkgrid")`<br>
`plot = sns.barplot(x=["A", "B", "C"], y=[1, 3, 2],hue = ["A", "B", "C"])`<br>
`plot.legend(title="abc")`<br>
![](legend_1.png)
### Always remember to use `hue` parameter in sns.barplot() for the next showing function of `plot.legend()` to work<br>

`seaborn.move_legend(obj, loc, bbox_to_anchor, **kwargs)` to move legend<br>
-`obj` = *object with the plot* <br>
-`loc` = *string or int* from {'upper left' or 2, 'upper right' or 1, 'lower left' or 3, 'lower right' or 4, 'upper center' or 9, 'lower center' or 8, 'center left' or 6, 'center right' or 7, 'center' or 10, 'best' or 0}<br>
-`bbox_to_anchor` = *BboxBase, 2-tuple, or 4-tuple of floats* to allow arbitrary placement of the legend<br>
`**kwargs` can be seen in [manual](https://seaborn.pydata.org/generated/seaborn.move_legend.html#seaborn.move_legend)<br>

Ex:<br>
`sns.set_style("darkgrid")`<br>
`plot = sns.barplot(x=["A", "B", "C"], y=[1, 3, 2],hue = ["A", "B", "C"])`<br>
`plot.legend(title="abc")`<br>
`sns.move_legend(plot,loc=0,bbox_to_anchor=(1,0.8))`<br>
![](legend_2.png)
<br><br>
To create new figure, or activate an existing one we use this function, but we will not consider all parameters:<br>
`matplotlib.pyplot.figure(num=None, figsize=None, dpi=None, *, facecolor=None, edgecolor=None, frameon=True, FigureClass=<class 'matplotlib.figure.Figure'>, clear=False, **kwargs)` <br>
-`figsize`= *(float, float), default: rcParams["figure.figsize"] (default: [6.4, 4.8])* which are width, height in inches<br>
<br>
After creating a figure we shall save it, there are several ways to do so, but we gonna use<br>
`matplotlib.figure.Figure.savefig(fname, *, transparent=None, dpi='figure', format=None, metadata=None, bbox_inches=None, pad_inches=0.1,facecolor='auto', edgecolor='auto', backend=None,**kwargs)` for which we will fill only a few of parameters like:<br>
-`fname` = *str or path-like or binary file-like* filled like "savename.format" for the name and format of saving<br>
-`dpi` = *float or 'figure', default: rcParams["savefig.dpi"] (default: 'figure')* to set resolution in dots per inch.<br>
-`bbox_inches` = *str or Bbox, default: rcParams["savefig.bbox"] (default: None)* to bound box in inches,but if *'tight'*, try to figure out the tight bbox of the figure. <br>

Ex:<br>
`plt.figure(figsize=(12,6))`<br>
`plotting_data = sns.barplot(otherinfo,x='genre',y='count')`<br>
`figure_plot = plotting_data.get_figure()`<br>
`figure_plot.savefig("Task1.png",dpi=300,bbox_inches = 'tight')`<br>
![](Task1.png)
<br><br>
### Now, after learning and getting used to these functions, we may start testing ourselves by doing tasks on those functions.