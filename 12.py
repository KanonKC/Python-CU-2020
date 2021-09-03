# with open('tweet_info_mini.csv') as f:
#     content = f.readlines()
#     data = [i.strip().split(",") for i in content]
#     print(data)

# def top_K_tweeters(tweets, K):
#     tupDat = [tuple(i) for i in data]
#     print(tupDat)

# top_K_tweeters(1,1)

# Prog-12: Tweeter Data Analytics
# Fill in your ID & Name
# ...
# Declare that you do this by yourself

import datetime

def to_epoch(date_time):
    d = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
    return d.timestamp()

def read_tweets(filename):
    f = open(filename)
    tweets = [tuple(line.strip().split(',')) 
              for line in f.readlines()]
    f.close()
    return tweets

def prt(x):
    print('\n'.join(str(e) for e in x))
    print('-----------------')

def test(filename, K, S):
    tweets = read_tweets(filename)
    print(filename, 'K=', K, 'S=', S)
    prt( top_K_tweeters(tweets, K) )
    prt( top_K_tweeters_in_S_seconds(tweets, K, S) )
    prt( top_K_common_tweet_pairs(tweets, K) )
    prt( top_K_common_tweet_triples(tweets, K) )

def main():
    test('tweet_info_mini.csv', 5, 3)
    test('tweet_info.csv', 10, 24*60*60)
#----------------------------------

def top_K_tweeters(tweets, K):

    return [] 
#---------------------------------
def top_K_tweeters_in_S_seconds(tweets, K, S):

    return [] 
#---------------------------------
def top_K_common_tweet_pairs(tweets, K):

    return [] 
#---------------------------------
def top_K_common_tweet_triples(tweets, K):

    return [] 

#----------------------------------
main()
