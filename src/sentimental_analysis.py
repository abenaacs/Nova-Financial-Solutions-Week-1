from textblob import TextBlob


def add_sentiment_analysis(analyst_ratings_df, text_column="headline"):
    """
    Perform sentiment analysis on the comments in analyst ratings.

    Args:
        analyst_ratings_df (pd.DataFrame): DataFrame containing analyst ratings.
        text_column (str): Column name containing textual comments.

    Returns:
        pd.DataFrame: Updated DataFrame with sentiment polarity scores.
    """
    if text_column in analyst_ratings_df.columns:
        analyst_ratings_df["Sentiment_Polarity"] = analyst_ratings_df[
            text_column
        ].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
        print("Sentiment analysis added successfully.")
    else:
        print(f"Column '{text_column}' not found in the analyst ratings data.")
    return analyst_ratings_df
