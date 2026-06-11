from dash import html, dcc


def layout():
	### layout
	# Image
	img = html.Img(
		src="assets/graph.png",
		alt="Project Analytics Photo",
		title="Project Image",
		style=dict(
			height="120px",
			width="120px",
			borderRadius="50%",
			border="1px solid black")
	)

	# header
	header = html.H1(
		children="Automobile Sales Statistics",
		style=dict(
			margin="4px auto",
			padding="4px 4px",
			display="block",
			backgroundColor="rgba(0, 0, 0, 0.1)",
			border="1px solid rgb(0, 0, 0)",
			borderRadius="8px",
			fontSize="24px",
			fontWeight="800")
	)

	# secondary header
	s_header = html.H5(
		children="Statistics of Recession and Non-recession",
		style=dict(
			margin="4px auto",
			padding="4px 4px",
			width="350px",
			height="30px",
			display="block",
			border="1px dashed rgb(0, 0, 0)",
			borderRadius="35%",
			fontSize="18px",
			fontWeight="600")
	)

	# line
	line = html.Hr(
		style=dict(borderTop="3px double black", 
				   opacity="0.6",
				   width="1200px",
				   color="blue")
	)

	## header wrap
	header_wrap=html.Div([
		img,
		html.Div(children=
			[header, s_header, line],
		style=dict(display="flex",
				   flexDirection="column",
				   alignItems="flex-start",
				   justifyContent="right",
			        fontFamily="serif")
					),
		img
	],
		style=dict(
			margin="0 10px",
			display="flex",
			flexDirection="row",
			alignItems="flex-start",
			justifyContent="space-between",
			gap="20px",
			textAlign="center")
	)

	## items
	# radio
	recession_radio = html.Div([
		html.H5(
			children="Recession period:",
			style=dict(
				margin="4px 4px",
				display="block",
				fontFamily="serif",
				fontSize="12px",
				fontWeight="400")
				),

		dcc.RadioItems(
			options=[dict(label="All", value="All"), dict(label="Yes", value="Yes"), dict(label="No", value="No")],
			value=None,
			inline=True,
			persistence=True,
			persistence_type="memory",
			id="recession_radio",
			style=dict(
				backgroundColor="rgba(0, 0, 0, 0.05)")
						)
	])

	# dropdown
	year_dropdown = html.Div([
		html.H5(
			children="Select year:",
			style=dict(
				margin="4px 4px",
				display="block",
				fontFamily="serif",
				fontSize="12px",
				fontWeight="400")
				),

		dcc.Dropdown(
			options=[] ,
			value=None,
			placeholder="Select",
			clearable=True,
			persistence=True,
			persistence_type="memory",
			disabled=False,
			id="year_dropdown",
			style=dict(
				backgrounColor="rgba(0, 0, 0, 0.95", fontSize=14)
					)
		])

	button = html.Button(
		children="Reset!",
		n_clicks=0,
		disabled=True,
		id="submit",
		style=dict(height="35px", display="block", transition= "0.3s")
	)

	## items wrap
	items = html.Div([
		html.Div(children=[recession_radio, year_dropdown, button],
						style=dict(
							gap="10px",
							display="flex",
							flexDirection="row",
							alignItems="flex-end",
							justifyContent="left")
				 ),
		html.H5(children=[],
			  id="selected",
			  style=dict(fontWeight=400,
						 textAlign="center")
				 ),
		html.H5(children=[],
			  id="filter",
			  style=dict(fontWeight=400,
						 fontSize=12,
						 textAlign="right")
				 )
		],
			    style=dict(display="grid",
						   gridTemplateColumns="1fr 1fr 1fr",
						   alignItems="flex-end",
						   marginBottom=20,
					         marginLeft=10,
					         marginRight=10)
		)

	## graphs
	graphs = html.Div(children=[dcc.Graph(id="plot1"),
					    dcc.Graph(id="plot2"),
					    dcc.Graph(id="plot3"),
					    dcc.Graph(id="plot4")],
					  id="plots"
						  )


	return html.Div(children=[header_wrap, items, graphs])