import pytrends
from pytrends.request import TrendReq
import matplotlib.pyplot as plt


def plot_minecraft_trend():
    # Set up pytrends
    pytrends = TrendReq(hl="en-US", tz=360)

    # Set up search parameters
    kw_list = ["Minecraft"]
    timeframe = "today 12-m"

    # Get the data
    pytrends.build_payload(kw_list, timeframe=timeframe)
    minecraft_trend = pytrends.interest_over_time()

    # Plot the data
    plt.plot(minecraft_trend.index, minecraft_trend["Minecraft"])
    plt.xlabel("Date")
    plt.ylabel("Search Interest")
    plt.title("Minecraft Search Trend Over 1 Year")
    plt.grid(True)
    plt.show()


# Call the function to generate the graph
plot_minecraft_trend()
