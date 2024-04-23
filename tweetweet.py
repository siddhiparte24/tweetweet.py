# pip install tweepy
import tweepy

# config.py : where I keep my keys as constants
import tweet

def about_me(client: tweepy.Client) -> None:
    """Print information about the client's user."""
    # The `public_metrics` addition will give me my followers count, among other things
    me = client.get_me(user_fields=["public_metrics"])
    print(f"My name: {me.data.name}")
    print(f"My handle: @{me.data.username}")
    print(f"My followers count: {me.data.public_metrics['followers_count']}")

if __name__ == "__main__":
    client = tweepy.Client(
        bearer_token=tweet.BEARER_TOKEN,
        consumer_key=tweet.API_KEY,
        consumer_secret=tweet.API_SECRET,
        access_token=tweet.ACCESS_TOKEN,
        access_token_secret=tweet.ACCESS_SECRET,
    )
    print("=== About Me ===")
    about_me(client)


