import MetaTrader5 as mt5
import matplotlib.pyplot as plt


class ScatterFX():
    def __init__(self, pair1, pair2):
        self.pair1 = pair1
        self.pair2 = pair2
        self.fig, self.ax = plt.subplots()
        self.list1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


    def Initializer(self):
        mt5.initialize()

        symbol1 = self.pair1
        symbol2 = self.pair2

        first = mt5.symbol_info_tick(symbol1).bid
        second = mt5.symbol_info_tick(symbol2).bid
        mt5.shutdown()

        return first, second

    def AxisSetter(self, xaxis, yaxis):
        fig, ax = self.fig, self.ax
        ax.set_xlim((xaxis - 0.0005), (xaxis + 0.0005))
        ax.set_ylim((yaxis - 0.0005), (yaxis + 0.0005))
        ax.set_xlabel(self.pair1)
        ax.set_ylabel(self.pair2)
        ax.set_title('Real-time Scatter Plot')

    def ScatterPlot(self):
        mt5.initialize()

        symbol1 = self.pair1
        symbol2 = self.pair2

        scatter = self.ax.scatter([], [])
        # Update the plot in real-time
        for i in range(10000):
            # Update data for the x-axis and y-axis
            x = mt5.symbol_info_tick(symbol1).bid
            y = mt5.symbol_info_tick(symbol2).bid

            print(x)
            print(y)

            self.list1.pop(0)
            self.list2.pop(0)

            self.list1.append(x)
            self.list2.append(y)


            x_data = self.list1
            y_data = self.list2

            # Update the plot with new data
            scatter.set_offsets(list(zip(x_data, y_data)))

            # Pause for a short time to simulate real-time updating
            plt.pause(0.5)

        # Add labels and title
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Real-time Scatter Plot')

        # Display the plot
        plt.show()


