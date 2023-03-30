import plotly.graph_objs as go


def graphing():
    # Define the sensor names
    sensor_names = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8']

    # Define the x-axis values
    time = list(range(0, 105, 5))

    # Create a list of traces for each sensor
    traces = []
    for name in sensor_names:
        # Create a line trace for the sensor with y-values set to the sensor name
        trace = go.Scatter(x=time, y=[name]*len(time), name=name, mode='lines')
        traces.append(trace)

    # Create the layout for the graph with A4 paper size
    layout = go.Layout(title='Sensor Readings', xaxis=dict(title='Time (s)'), yaxis=dict(title='Sensor Names'), width=595, height=842)

    # Create the figure object
    fig = go.Figure(data=traces, layout=layout)

    # Display the graph
    fig.show()



    import matplotlib.pyplot as plt

    # define the data
    toa = [22.97388949, 23.59899775, 25.75168887, 27.87624017, 28.09409635, 31.33958326, 31.95876047, 32.39149445, 33.39636271]
    bearing = [-0.91137199, -0.94185888, -0.73733928, -0.60817156, -0.47725227, -0.17842146, -0.39988179, -0.24548724, -0.63939348]
    spl = [78.39910845, 72.10571761, 69.94141609, 60.10739709, 57.50451793, 40.6371623, 43.98275939, 39.8110488, 42.2365895]

    # create the scatter plot
    plt.scatter(toa, bearing, c=spl)

    # set axis labels and title
    plt.xlabel('Time of Arrival')
    plt.ylabel('2D Bearing Angles')
    plt.title('Time of Arrival vs 2D Bearing Angles with SPL Level')

    # add a colorbar
    plt.colorbar(label='SPL Level')

    # show the plot
    plt.show()



