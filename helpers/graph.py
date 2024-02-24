# @formatter:off
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from datetime import datetime
from helpers import images
import numpy as np
import math
import io


def template_graph(x_axis, y_axis):
    mpl.rcParams['savefig.pad_inches'] = 0  # Remove 0.1in border around graph
    plt.figure(figsize=(6.4, 4.8))  # Set the size of the graph (in inches - width x height)
    ax = plt.axes()  # Initialize axis
    plt.autoscale(tight=True)  # Enable tight autoscaling
    plt.ylim(0, 100)  # Lock the Y axis between 2 values (not necessary)
    plt.grid(color='gray', linestyle='-', linewidth=0.5, alpha=0.5)  # Set up a light grey grid behind the data

    ax.plot(x_axis, y_axis, 'o-', label="Temperature (°C)")  # Plot the data. 'o-' is the line style. label is used in the legend
    # You can duplicate the line above to create multiple lines

    ax.legend()  # Create a legend using the label(s) defined above. Not necessary for one line graphs

    ax.spines['top'].set_visible(False)  # Hide the top spline
    ax.spines['right'].set_visible(False)  # Hide the right spline
    ax.spines['left'].set_color('white')  # Set colour of left spine
    ax.spines['bottom'].set_color('white')  # Set colour of bottom spine

    ax.tick_params(axis='x', colors='white')  # Set the colour of the ticks on the X axis
    ax.tick_params(axis='y', colors='white')  # Set the colour of the ticks on the Y axis

    plt.xticks(ticks=x_axis,
               labels=x_axis,
               rotation=45)  # Initialize the x ticks using the timestamps list. The 'labels' section is what is actually displayed, so is parsed here.

    plt.yticks(range(0, 101, 10))  # This sets the y ticks to clean intervals of 10

    ax.xaxis.set_major_locator(plt.MaxNLocator(12))  # Limit the maximum number of ticks on the X axis. This is very important for clean graphs
    # ax.yaxis.set_major_formatter(ticker.FuncFormatter(format_y_tick))  # You can specify a formatter function for the Y axis here

    img_bytes = io.BytesIO()  # Set up a BytesIO object to store the image in
    plt.savefig(img_bytes, format='png', transparent=True)  # Save the image. transparent=True is important for discord embeds
    img_bytes.seek(0)  # Idk what this does tbh but ChatGPT told me to put it here

    plt.clf()  # Clear the graph for some reason? ig it's already saved

    return img_bytes  # Return the image


def format_y_tick(value, pos):
    return f'{value}c'


def hourly_weather_graph(timestamps, temperature, apparent_temperature, dewpoint, humidity, precipitation, rainfall, showers, snowfall):
    # Temperature graph
    mpl.rcParams['savefig.pad_inches'] = 0  # Remove 0.1in border around graph
    plt.figure(figsize=(6.4, 2))

    temp_range = max(max(temperature), max(apparent_temperature), max(dewpoint)) - min(min(temperature), min(apparent_temperature), min(dewpoint))
    temp_increment = math.ceil(temp_range / 4)

    temp_ax = plt.axes()  # Temperature axis
    plt.autoscale(tight=True)  # Enable tight autoscaling
    plt.ylim(math.floor(min(min(temperature), min(apparent_temperature), min(dewpoint)) / temp_increment) * temp_increment, math.ceil(max(max(temperature), max(apparent_temperature), max(dewpoint)) / temp_increment) * temp_increment)
    plt.grid(color='gray', linestyle='-', linewidth=0.5, alpha=0.5)  # Set up a light grey grid behind the data

    temp_ax.plot(timestamps, temperature, 'o-', label="Temperature")
    temp_ax.plot(timestamps, apparent_temperature, 'o-', label="Feels like")
    temp_ax.plot(timestamps, dewpoint, 'o-', label="Dew point")
    temp_ax.legend()

    temp_ax.spines['top'].set_visible(False)
    temp_ax.spines['right'].set_visible(False)
    temp_ax.spines['left'].set_color('white')  # Set color of left spine
    temp_ax.spines['bottom'].set_color('white')  # Set color of bottom spine

    temp_ax.tick_params(axis='x', colors='white')
    temp_ax.tick_params(axis='y', colors='white')

    plt.xticks(ticks=timestamps, labels=[datetime.strptime(ts, "%Y-%m-%dT%H:%M").strftime("%H:%M") for index, ts in enumerate(timestamps)], rotation=45)
    plt.yticks(range(math.floor(min(min(temperature), min(apparent_temperature), min(dewpoint)) / temp_increment) * temp_increment, math.ceil(max(max(temperature), max(apparent_temperature), max(dewpoint)) / temp_increment) * temp_increment + 1, temp_increment))
    temp_ax.xaxis.set_major_locator(plt.MaxNLocator(12))

    plt.tight_layout()

    temp_graph = io.BytesIO()
    plt.savefig(temp_graph, format='png', transparent=True)
    temp_graph.seek(0)

    plt.clf()

    # Humidity graph
    humidity_range = max(humidity) - min(humidity)
    humidity_increment = math.ceil(humidity_range / 4)

    humid_ax = plt.axes()  # Temperature axis
    plt.autoscale(tight=True)  # Enable tight autoscaling
    plt.ylim(math.floor(min(humidity) / humidity_increment) * humidity_increment, math.ceil(max(humidity) / humidity_increment) * humidity_increment)
    plt.grid(color='gray', linestyle='-', linewidth=0.5, alpha=0.5)  # Set up a light grey grid behind the data

    humid_ax.plot(timestamps, humidity, 'o-', label="Humidity")
    humid_ax.legend()

    humid_ax.spines['top'].set_visible(False)
    humid_ax.spines['right'].set_visible(False)
    humid_ax.spines['left'].set_color('white')  # Set color of left spine
    humid_ax.spines['bottom'].set_color('white')  # Set color of bottom spine

    humid_ax.tick_params(axis='x', colors='white')
    humid_ax.tick_params(axis='y', colors='white')

    plt.xticks(ticks=timestamps, labels=[datetime.strptime(ts, "%Y-%m-%dT%H:%M").strftime("%H:%M") for index, ts in enumerate(timestamps)], rotation=45)
    plt.yticks(range(math.floor(min(humidity) / humidity_increment) * humidity_increment, math.ceil(max(humidity) / humidity_increment) * humidity_increment + 1, humidity_increment))
    humid_ax.xaxis.set_major_locator(plt.MaxNLocator(12))

    plt.tight_layout()

    humidity_graph = io.BytesIO()
    plt.savefig(humidity_graph, format='png', transparent=True)
    humidity_graph.seek(0)

    plt.clf()

    # Precipitation graph
    precip_range = max(precipitation) * 1.1
    precip_increment = math.ceil(precip_range / 4) if math.ceil(precip_range / 4) else 1

    plt.figure(figsize=(6.4, 2))
    plt.autoscale(tight=True)  # Enable tight autoscaling
    plt.ylim(0, max(math.ceil(max(precipitation) / precip_increment) * precip_increment * 1.1, 1))

    plt.bar(timestamps, snowfall, label='Snowfall', color='white')
    plt.bar(timestamps, showers, bottom=snowfall, label='Showers', color='#97d1cd')
    plt.bar(timestamps, rainfall, bottom=np.array(showers) + np.array(snowfall), label='Rainfall', color='#6b6787')

    for hour, precip in zip(timestamps, precipitation):
        plt.text(hour, precip, str(precip) if precip > 0 else '0', ha='center', va='bottom', color='white', fontsize='8')

    plt.legend()

    ax = plt.gca()

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('white')  # Set color of left spine
    ax.spines['bottom'].set_color('white')  # Set color of bottom spine

    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    plt.xticks(ticks=timestamps, labels=[datetime.strptime(ts, "%Y-%m-%dT%H:%M").strftime("%H:%M") for index, ts in enumerate(timestamps)], rotation=45)
    plt.yticks(range(0, math.ceil(max(precipitation) / precip_increment) * precip_increment + 1, precip_increment))
    humid_ax.xaxis.set_major_locator(plt.MaxNLocator(12))

    plt.tight_layout()

    precipitation_graph = io.BytesIO()
    plt.savefig(precipitation_graph, format='png', transparent=True)
    precipitation_graph.seek(0)

    return temp_graph, humidity_graph, precipitation_graph


def weather_graph_backup(timestamps, temperature, humidity, dewpoint, rainfall):
    mpl.rcParams['savefig.pad_inches'] = 0
    ax = plt.axes()
    plt.autoscale(tight=True)
    plt.ylim(0, 100)
    plt.grid(color='gray', linestyle='-', linewidth=0.5, alpha=0.5)

    ax.plot(timestamps, temperature, 'o-', label="Temperature (°C)")
    ax.plot(timestamps, humidity, 'o-', label="Humidity (%)")
    ax.plot(timestamps, dewpoint, 'o-', label="Dew point (°C)")
    ax.plot(timestamps, rainfall, 'o-', label="Rainfall (mm)")

    ax.legend()

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('white')  # Set color of left spine
    ax.spines['bottom'].set_color('white')  # Set color of bottom spine

    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    plt.xticks(ticks=timestamps, labels=[datetime.strptime(ts, "%Y-%m-%dT%H:%M").strftime("%H:%M") for index, ts in enumerate(timestamps)], rotation=45)
    plt.yticks(range(0, 101, 10))

    ax.xaxis.set_major_locator(plt.MaxNLocator(12))
    # ax.yaxis.set_major_formatter(ticker.FuncFormatter(format_y_tick))

    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png', transparent=True)
    img_bytes.seek(0)

    plt.clf()

    return img_bytes
