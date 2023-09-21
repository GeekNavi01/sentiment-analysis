# Import the libraries
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap
from bokeh.models import HoverTool

# create_bokeh_plot function
def create_bokeh_plot(review_counts):
    categories = list(review_counts.keys())
    counts = list(review_counts.values())

    source = ColumnDataSource(data=dict(categories=categories, counts=counts))

    p = figure(x_range=categories, plot_height=350, title="Review Categories", toolbar_location=None, tools="")

    # Add hover tool
    hover = HoverTool()
    hover.tooltips = [("Category", "@categories"), ("Count", "@counts")]
    p.add_tools(hover)

    p.vbar(x='categories', top='counts', width=0.5, source=source, line_color="white",
           fill_color=factor_cmap('categories', palette=['#FF5733', '#3399FF', '#33FF57', '#FF33A1'], factors=categories))

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.y_range.end = max(counts) + 5
    p.title.text_font_size = "16pt"
    p.xaxis.major_label_orientation = 1.2
    p.yaxis.axis_label = "Number of Reviews"

    return p
