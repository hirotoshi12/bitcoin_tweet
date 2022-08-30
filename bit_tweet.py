import requests
import os
import ast
import tweepy
# import json

# twitterのAPIキー
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)

# 保存場所の定義
past_rate = 'rate.txt'

endPoint_path_new = 'https://api.coin.z.com/public/v1/ticker?symbol=BTC'

response_new = requests.get(endPoint_path_new)

response_dict = ast.literal_eval(response_new.text)

# 過去レートのファイルを確認する。
if os.path.exists(past_rate):
    # ファイル読み込み（読み取り）
    past_last = 0
    with open(past_rate, encoding='utf-8') as f:
        past_last = f.read()
        print('過去レート:' + past_last)
        
    print('最新レート:' + response_dict['data'][0]['last'])
    # 条件式
    if response_dict['data'][0]['last'] > past_last:
        print('上がりました')
        client.create_tweet(text="上がりました")
        
    elif response_dict['data'][0]['last'] ==  past_last:
        print('変わりませんでした')
        client.create_tweet(text="変わりませんでした")
    else:
        print('下がりました')
        client.create_tweet(text="下がりました")
    
f = open(past_rate, 'w', encoding='utf-8')
f.write(response_dict['data'][0]['last'])
f.close()
    
    