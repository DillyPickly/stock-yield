from datetime import date

import pandas as pd
from bokeh.io import show
from bokeh.layouts import layout
from bokeh.models import (Button, CustomJS, DateRangeSlider,
                          DatetimeTickFormatter, NumeralTickFormatter)
from bokeh.plotting import figure, show

# Import Data
djia_uri  = 'processed_data/djia_historical.csv'
yield_uri = 'processed_data/yield_historical.csv'

djia_df  = pd.read_csv(djia_uri, sep=',',header=0,index_col=0)
yield_df = pd.read_csv(yield_uri,sep=',',header=0,index_col=0)

x = pd.to_datetime(djia_df.index)
y = djia_df['adj_close']


# create new plot
fig = figure(
    title="datetime axis example",
    x_axis_type="datetime",
    sizing_mode="stretch_width",
    max_width=500,
    plot_height=250,
    output_backend='webgl'
)

# add renderers
# p.circle(x,y, size=8)
fig.line(x,y, color="navy", line_width=1)

# # format axes ticks
# p.yaxis[0].formatter = NumeralTickFormatter(format="$0.00")
# p.xaxis[0].formatter = DatetimeTickFormatter(months="%b %Y")

# add Date range slider
date_range_slider = DateRangeSlider(value=(date(2016, 1, 1), date(2016, 12, 31)),
                                    start=date(2015, 1, 1), end=date(2017, 12, 31))

# button_update = CustomJS(args=dict(button=button), code="""

#     if (button.label == "Play") {
#         button.label = "Pause";
#     } else if (button.label == "Pause") {
#         button.label = "Play";
#     }

# """)

date_range_slider.js_on_change("value", date_range_slider_update)

# add Play button
button = Button(label="Play", default_size=150 , button_type="default")

button_update = CustomJS(args=dict(button=button), code="""

    if (button.label == "Play") {
        button.label = "Pause";
    } else if (button.label == "Pause") {
        button.label = "Play";
    }

    

""")

button.js_on_click(button_update)




# create layout
layout = layout(
    [
        [button, date_range_slider],
        [fig],
    ],
    # sizing_mode="stretch_width",
    # margin=(10,50,10,50),


)

show(layout)
