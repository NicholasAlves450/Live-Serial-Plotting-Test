import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial

# Create a figure and axes
fig, ax = plt.subplots()

# Initialize data
x = []
y = []

# Serial connection setup
try:
    ser = serial.Serial('COM3', 9600, timeout=0.1)  # Open the serial port
except serial.SerialException as e:
    print(f"Error: Could not open serial port: {e}")
    exit()

# Number of points to display in the plot
N = 200

# Animation function
def animate(i):
    # Read a line from the serial port
    try:
        data = ser.readline().decode().strip()
        # Parse the data as a float
        y_value = float(data)
        
        # Update data lists
        x.append(i)
        y.append(y_value)

        # Limit data to the last N points
        x[:] = x[-N:]
        y[:] = y[-N:]

        # Clear the previous plot
        ax.clear()

        # Plot the new data
        
        ax.plot(x, y, label='Sensor Data')

        # Set labels, title, and legend
        plt.gca().set_ylim(bottom=0)
        ax.set_title("Live Sensor Data")
        ax.set_xlabel("Time (frames)")
        ax.set_ylabel("Value (cm)")
        ax.legend(loc='upper left')
    except ValueError:
        # Skip invalid data (e.g., if data is not a float)
        pass

# Create the animation
ani = animation.FuncAnimation(fig, animate, interval=10)  # Adjust interval for smoother updates

# Show the plot
plt.show()

# Ensure the serial port is closed on exit
ser.close()
