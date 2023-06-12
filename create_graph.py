import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def comparison_graph():
    # First dataset
    angles1 = [90, 121, 37, 58, 178, 165, 25]
    times1 = [2, 4, 7, 10, 12, 13, 13.5]
    bar_values1 = [86, 117, 75, 45, 125, 111, 51]

    # Second dataset
    angles2 = [45, 85, 62, 31, 99, 110, 75]
    times2 = [3, 6, 8, 11, 12.5, 14, 14.5]
    bar_values2 = [60, 95, 80, 40, 115, 105, 70]

    # Convert angles to radians
    angles_radians1 = np.radians(angles1)
    angles_radians2 = np.radians(angles2)

    # Create the figure and subplots
    fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=True)

    # Set aspect ratio to equal for the angle graph subplot
    ax1.set_aspect('equal')

    # Plot the arcs and arrows for the first dataset in the angle graph subplot
    for angle, x, y in zip(angles_radians1, times1, np.zeros_like(times1)):
        arc = patches.Arc((x, y), 0.2, 0.2, 0, 0, np.degrees(angle))
        ax1.add_patch(arc)
        ax1.annotate("", xy=(x + np.cos(angle), y + np.sin(angle)), xytext=(x, y),
                     arrowprops=dict(arrowstyle="->"))
        ax1.text(x + 0.5* np.cos(angle), y + 0.5 * np.sin(angle),
                 f"{int(np.degrees(angle))}°", ha='center', va='center')

    # Create vertical dashed lines on the angle graph subplot for the first dataset
    for t in times1:
        ax1.axvline(x=t, linestyle='dashed', color='gray')

    # Plot the bar chart for the first dataset in the second subplot
    ax2.bar(times1, bar_values1, width=0.2, align='center', color='blue')

    # Create vertical dashed lines on the bar chart subplot for the first dataset
    for t in times1:
        ax2.axvline(x=t, linestyle='dashed', color='gray')
        ax2.text(t , bar_values1[times1.index(t)] + 1.2, f"{int(bar_values1[times1.index(t)])}", ha='center', va='center')

    # Plot the arcs and arrows for the second dataset in the angle graph subplot
    for angle, x, y in zip(angles_radians2, times2, np.zeros_like(times2)):
        arc = patches.Arc((x, y), 0.2, 0.2, 0, 0, np.degrees(angle))
        ax1.add_patch(arc)
        ax1.annotate("", xy=(x + np.cos(angle), y + np.sin(angle)), xytext=(x, y),
                     arrowprops=dict(arrowstyle="->", color='green'))
        ax1.text(x + 0.5 * np.cos(angle), y + 0.5 * np.sin(angle),
                 f"{int(np.degrees(angle))}°", ha='center', va='center', color='green')

    # Create vertical dashed lines on the angle graph subplot for the second dataset
    for t in times2:
        ax1.axvline(x=t, linestyle='dashed', color='gray')
        ax2.text(t , bar_values2[times2.index(t)] + 1.2, f"{int(bar_values2[times2.index(t)])}", ha='center', va='center')

    # Plot the bar chart for the second dataset in the second subplot
    ax2.bar(times2, bar_values2, width=0.2, align='center', color='green')

    # Create vertical dashed lines on the bar chart subplot for the second dataset
    for t in times2:
        ax2.axvline(x=t, linestyle='dashed', color='gray')

    # Set labels and title for the angle graph subplot
    ax1.set_ylabel('Y')
    ax1.set_title('Angles in Degrees (°)', pad = 20)

    # Set labels and title for the bar chart subplot
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Value')
    ax2.set_title('SPL Sound Pressure Level (dB)', pad = 20)

    # Adjust the spacing between subplots
    plt.subplots_adjust(hspace=0.3)

    # Display the graph
    plt.show()


