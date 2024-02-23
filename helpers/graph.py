import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from datetime import datetime
import io

def format_y_tick(value, pos):
    return f'{value}c'

def weather_graph(timestamps, temperature, humidity, dewpoint, rainfall):
    mpl.rcParams['savefig.pad_inches'] = 0
    ax = plt.axes(frameon=False)
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
