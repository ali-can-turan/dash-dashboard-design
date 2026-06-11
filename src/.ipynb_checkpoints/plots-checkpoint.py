import plotly.express as px
# helper function for graphs
def style_fig(fig):
	fig.update_layout(title_font=dict(size=14),
					  xaxis_title_font=dict(size=12),
					  yaxis_title_font=dict(size=12),
					  font=dict(size=10),
					  margin=dict(l=20, r=20, t=20, b=20),
					  template="seaborn")
	return fig

def fig_plotter(rec_year):
	# plot1
	plot1_df = rec_year.groupby("Month")["Automobile Sales"].mean().reset_index()
	plot1 = px.line(data_frame=plot1_df,
				x="Month",
				y="Automobile Sales",
				text="Automobile Sales", 
				labels={"Automobile Sales":"Sales"}, 
				title="Monthly Automobile Sales",
				markers="o")
	plot1.update_traces(textposition="top center",
					marker=dict(color="orange"),
					texttemplate="%{text:.0f}",
					cliponaxis=False)

	# plot2
	plot2_df = rec_year.groupby("Vehicle Type")["Advertising Expenditure"].sum().reset_index()
	plot2 = px.bar(data_frame=plot2_df,
			   x="Vehicle Type",
			   y="Advertising Expenditure",
			   text="Advertising Expenditure",
			   color="Advertising Expenditure",
			   # labels={"Advertising Expenditure":"Expenditure", "Vehicle Type": "Vehicle"},
			   title="Advertising Expenditure by Vehicle Type")
	plot2.update_traces(texttemplate="%{text:.0f}"),

	# plot3
	plot3 = px.scatter(data_frame=rec_year,
				   x="Price",
				   y="Automobile Sales",
				   color="Price",
				   labels={"Automobile Sales":"Sales"},
				   title="Automobile Sales by Price",
				   size="Automobile Sales",
				   marginal_y="violin")

	# plot4
	plot4_df = rec_year.groupby("City")["Advertising Expenditure"].mean().reset_index()
	plot4 = px.pie(data_frame=plot4_df,
			   names="City",
			   values="Advertising Expenditure",
			   hole=0.6,
			   # labels={"Advertising_Expenditure": "Expenditure"},
			   title="Advertising Expenditure by City")

	return style_fig(plot1), style_fig(plot2), style_fig(plot3), style_fig(plot4)

