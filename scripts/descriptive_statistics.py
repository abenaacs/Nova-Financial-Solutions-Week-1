import pandas as pd
import matplotlib.pyplot as plt


def headline_length_analysis(data):
    """Analyze and visualize headline length statistics."""
    data["headline_length"] = data["headline"].apply(len)
    print("\nHeadline Length Statistics:")
    print(data["headline_length"].describe())

    plt.figure(figsize=(10, 6))
    data["headline_length"].hist(bins=30, color="skyblue", edgecolor="black")
    plt.title("Distribution of Headline Lengths")
    plt.xlabel("Headline Length")
    plt.ylabel("Frequency")
    plt.show()


def articles_per_publisher(data):
    """Analyze and visualize the number of articles per publisher."""
    publisher_counts = data["publisher"].value_counts()
    print("\nTop 10 Publishers:\n", publisher_counts.head(10))

    plt.figure(figsize=(10, 6))
    publisher_counts.head(10).plot(kind="bar", color="orange", edgecolor="black")
    plt.title("Top 10 Publishers by Article Count")
    plt.xlabel("Publisher")
    plt.ylabel("Number of Articles")
    plt.xticks(rotation=45)
    plt.show()


def publication_date_trends(data):
    """Visualize publication trends over time."""
    daily_counts = data["date"].dt.date.value_counts().sort_index()

    # Identify significant spikes (e.g., 3 standard deviations above the mean)
    mean_count = daily_counts.mean()
    std_dev = daily_counts.std()
    spike_threshold = mean_count + 3 * std_dev
    spikes = daily_counts[daily_counts > spike_threshold]

    plt.figure(figsize=(14, 7))
    daily_counts.plot(kind="line", color="green", label="Daily Article Counts")
    plt.scatter(spikes.index, spikes.values, color="red", label="Significant Spikes")
    plt.title("Publication Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Articles")
    plt.legend()
    plt.show()

    print("\nSignificant Spikes in Publication Frequency:")
    print(spikes)
