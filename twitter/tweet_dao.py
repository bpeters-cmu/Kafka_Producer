from .models import TweetModel


def insert_tweet(status):

    tweet = TweetModel(tweet_id=status.id, user_name=status.user.name, tweet_text=status.text,
                       user_location=status.user.location, verified_user=status.user.verified)
    tweet.save()
