import matplotlib as mpl
import matplotlib.pyplot as plt
import io

def graph(xdata, ydata):
    mpl.rcParams['savefig.pad_inches'] = 0

    ax = plt.axes((0, 0, 1, 1), frameon=False)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.autoscale(tight=True)

    # Plot the data.
    plt.plot(ydata)

    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png', transparent=True)
    img_bytes.seek(0)

    plt.clf()

    return img_bytes
