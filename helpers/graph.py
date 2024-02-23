import matplotlib as mpl
import matplotlib.pyplot as plt
import io


def weather_graph(timestamps, ydata):
    mpl.rcParams['savefig.pad_inches'] = 0
    ax = plt.axes()
    plt.autoscale(tight=True)
    plt.ylim(min(ydata) - 1, max(ydata) + 1)

    ax.plot(timestamps, ydata)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('white')  # Set color of left spine
    ax.spines['bottom'].set_color('white')  # Set color of bottom spine

    # Show only ticks on the left and bottom spines
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')

    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    ax.yaxis.set_major_formatter(ticker.FuncFormatter(format_y_tick))

    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png', transparent=True)
    img_bytes.seek(0)

    plt.clf()

    return img_bytes
