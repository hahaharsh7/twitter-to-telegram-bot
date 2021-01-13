import time 
import requests
def telegram_bot_sendtext(bot_token, bot_chatID, bot_message):
        send_text = 'https://api.telegram.org/bot'+bot_token+'/sendMessage?chat_id='+bot_chatID+'&parse_mode=HTML&text='+bot_message
        response = requests.get(send_text)

array = []      
import pandas as pd
while True:
    try:
        import tweepy
        import datetime
        auth = {'consumer_key': '',
                'consumer_secret':'',
                'access_token_key':'',
                'access_token_secret': ''
            }
        class TweetMiner(object):
                result_limit    =   20    
                data =   []
                api =   False
                def __init__(self, keys_dict=auth, api=api, result_limit = 20):

                    self.twitter_keys = keys_dict

                    auth = tweepy.OAuthHandler(keys_dict['consumer_key'], keys_dict['consumer_secret'])
                    auth.set_access_token(keys_dict['access_token_key'], keys_dict['access_token_secret'])

                    self.api = tweepy.API(auth)
                    self.twitter_keys = keys_dict

                    self.result_limit = result_limit
                def mine_user_tweets(self, user="buyucoin",mine_rewteets=False,max_pages=5):
                        data           =  []
                        last_tweet_id  =  False
                        page           =  1

                        while page <= max_pages:
                            if last_tweet_id:
                                statuses   =   self.api.user_timeline(screen_name=user,
                                                                     count=self.result_limit,
                                                                     max_id=last_tweet_id - 1,
                                                                     tweet_mode = 'extended',
                                                                     include_retweets=True
                                                                    )        
                            else:
                                statuses   =   self.api.user_timeline(screen_name=user,
                                                                        count=self.result_limit,
                                                                        tweet_mode = 'extended',
                                                                        include_retweets=True)

                            for item in statuses:
                                mined = {
                                        #'tweet_id':        item.id,
                                        #'name':            item.user.name,
                                        'screen_name':     item.user.screen_name,
                                        #'retweet_count':   item.retweet_count,
                                        'text':            item.full_text,
                                        'mined_at':        datetime.datetime.now(),
                                        'created_at':      item.created_at,
                                        #'favourite_count': item.favorite_count,
                                        #'hashtags':        item.entities['hashtags'],
                                        #'status_count':    item.user.statuses_count,
                                        #'location':        item.place,
                                        #'source_device':   item.source
                                    }

                                try:
                                    mined['retweet_text'] = item.retweeted_status.full_text
                                except:
                                    mined['retweet_text'] = 'None'
                                try:
                                    mined['quote_text'] = item.quoted_status.full_text
                                    mined['quote_screen_name'] = status.quoted_status.user.screen_name
                                except:
                                    mined['quote_text'] = 'None'
                                    mined['quote_screen_name'] = 'None'

                                last_tweet_id = item.id
                                data.append(mined)

                            page += 1

                        return data

        Tweet = TweetMiner(result_limit = 10)
        uk_tweets = Tweet.mine_user_tweets(user='buyucoin', max_pages=1)    
        tweets_df = pd.DataFrame(uk_tweets)
        tweets_df = tweets_df[tweets_df['created_at'].astype(str).str.contains(str("2021-01-13"))]
        tweets_df['date'] = tweets_df.created_at.dt.strftime('%Y-%m-%d')
        tweets_df = tweets_df[['screen_name', 'date','text']].reset_index(drop=True)
        tweets_df = tweets_df.apply(pd.to_numeric, errors='ignore')
        for i in tweets_df['text']:
            if i in array:
                break
            else:
                array.insert(0,i)
                k = array[0].replace("#","")
                telegram_bot_sendtext('','',k)
                break

        time.sleep(5000)
        
    except:
        pass