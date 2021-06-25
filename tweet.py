import tweepy
import credentials

auth = tweepy.OAuthHandler(credentials.api_key, credentials.api_secret_key)

auth.set_access_token(credentials.access_token,
                      credentials.access_token_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
    media_obj = api.media_upload("/Users/IvanZhao/Documents/GitHub/daniel-craig-bot/image.jpeg")
    print("Media Sucessfully Uploaded")
    status = api.update_status(media_ids=[media_obj.media_id])
    print("Tweet sucessfully posted!")
except:
    print("Error during authentication")
