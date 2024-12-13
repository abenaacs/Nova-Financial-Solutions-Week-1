import matplotlib.pyplot as plt


def time_series_analysis(data):
    """Analyze and visualize publication frequency by hour of the day."""
    hourly_counts = data["date"].dt.hour.value_counts().sort_index()

    # Identify the peak publication hour
    peak_hour = hourly_counts.idxmax()
    print(
        f"\nPeak Publication Hour: {peak_hour}:00 with {hourly_counts[peak_hour]} articles"
    )

    plt.figure(figsize=(10, 6))
    hourly_counts.plot(kind="bar", color="purple", edgecolor="black")
    plt.title("Publication Frequency by Hour")
    plt.xlabel("Hour of Day")
    plt.ylabel("Number of Articles")
    plt.axvline(peak_hour, color="red", linestyle="--", label="Peak Hour")
    plt.legend()
    plt.show()
