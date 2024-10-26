import os
import json
from datetime import datetime, timezone

json_directory = "tweets"

tweet_count = 0
tweets_with_photos = 0
photo_count = 0
tweets_with_videos = 0

def count_media_in_tweet(tweet):
  global tweets_with_photos, photo_count, tweets_with_videos
  media_entities = tweet.get('entities', {}).get('media', [])
  extended_media_entities = tweet.get('extended_entities', {}).get('media', [])
  
  all_media = media_entities + extended_media_entities
  has_photo = False
  has_video = False
  
  for media in all_media:
    media_type = media.get('type')
    if media_type == 'photo':
      photo_count += 1
      has_photo = True
    elif media_type == 'video':
      has_video = True
  
  if has_photo:
    tweets_with_photos += 1
  if has_video:
    tweets_with_videos += 1

def process_json_files(directory):
  global tweet_count
  for filename in os.listdir(directory):
    if filename.endswith(".json"):
      filepath = os.path.join(directory, filename)
      with open(filepath, 'r', encoding='utf-8') as file:
        try:
          json_data = json.load(file)
          if isinstance(json_data, list):
            for tweet in json_data:
              tweet_count += 1
              count_media_in_tweet(tweet)
          elif isinstance(json_data, dict):
              tweet_count += 1
              count_media_in_tweet(json_data)
        except json.JSONDecodeError:
          print(f"Error reading JSON from {filename}")

def save_results_to_file(output_file):
  timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
  
  with open(output_file, 'w') as f:
    f.write(f"## Statistics\n")
    f.write(f"- Last updated: [{timestamp}](https://github.com/yetweets/vault/commits/main/)\n")
    f.write(f"- Total number of tweets: {tweet_count}\n")
    f.write(f"- Number of tweets with photo(s): {tweets_with_photos}\n")
    f.write(f"- Total number of photos in tweets: {photo_count}\n")
    f.write(f"- Number of tweets with video(s): {tweets_with_videos}\n")

def main():
  process_json_files(json_directory)
  save_results_to_file("statistics_output.txt")

if __name__ == "__main__":
  main()