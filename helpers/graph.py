import matplotlib.pyplot as plt
import io

def graph(title: str, data: list[float]):
    x_values = list(range(1, len(data) + 1))
    plt.plot(x_values, data)

    plt.xlabel('Data Points')
    plt.ylabel('Values')

    plt.title(title)

    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)

    plt.clf()

    return img_bytes
