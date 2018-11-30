# -*- coding: UTF-8 -*-
import twitter
import datetime
import googlemaps
from googlemaps import geocoding

# ----------------------------------------------------------
# --------          HW 12: Twitter Search          ---------
# --------          Plus Geolocation Data          ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after having completed this
# program
# ----------------------------------------------------------
# Name: Noah
# Time spent on this program: 6 hours
# Collaborators and sources:
#   (List any collaborators or sources here.)
# ----------------------------------------------------------



# ----------------------------------------------------------
# Fill in the following variables
# ----------------------------------------------------------
consumer_key = 'YIFZJADPOVpyMTgllZOXHqY2r'
consumer_secret = 'izNseptlneuPDf22kpImDzRiRNm5FoTC3JaVnF62wnEn1EUrA4'
geocode_api_key = 'AIzaSyBmtHKmSh0cqarpAHbKJsE8GtxyfyZlLrY'

test_screen_name = 'colgateuniv'
test_address = '1600 Amphitheatre Parkway, Mountain View, CA'




# ----------------------------------------------------------
# Main Function for Testing
# ----------------------------------------------------------
def main():
    '''main function to call other functions'''
    screen_name = 'colgateuniv'
    lat = '42.8166'
    long = '-75.5402'
 
  
    twitter_api = get_twitter_api()
    tweets = twitter_api.GetUserTimeline(screen_name=screen_name)
    tweet = tweets[0]
    user = 'colgateuniv'
    
    gmaps_client = googlemaps.Client(geocode_api_key)

   
    api = googlemaps.Client(geocode_api_key)

        
    search(twitter_api)

# ----------------------------------------------------------
# Write Your Code Here
# ----------------------------------------------------------

def tweet_to_string( status, location=False ):
    ''' updated version of the code written in Lecture 25 '''
    try:
        #gets user date and tweet
        user = status.user.screen_name
        date = tweet_date(status.created_at)
        tweet = status.text.replace("\n"," ")
        #slices up to make long string
        s = 'Tweet from @' + user + date + ': "' + tweet + '"'
        if location: # optionally append location name
            s += ' (' + status.place['full_name'] + ')'
        return s
    except twitter.error.TwitterError as e:
        print('Error in status_to_string: ' + e + '\n')
        return False
    
def user_to_string(user):
    '''takes a user and changes it to a string'''
    #gets username
    try:
        username = user.screen_name
    #gets user id
        user_id = user.name
    #makes long string
        final = "'" + str("@" + username + " (" + user_id + ") " + '"' + user.description + '"') + "'"
    except titter.error.TwitterError:
        final = "User not found."
    return final

def get_user(api, screenname):
    '''takes api and name and retrieves userip'''
    #gets userip
    userip = api.GetUser(screen_name=screenname)
    
    return userip

def get_tweets_by_user(api, name):
    '''takes api and name and retrieves recent tweets'''
    
    #gets five recent tweets from user
    try:
        tweets = api.GetUserTimeline(screen_name=name)
        recent = tweets[0:10]
    
        tweet = []
        for i in recent:
            try:
                print(i.text)
            #just appends the text of the 5
                tweet.append(i.text)
            except UnicodeEncodeError:
                print("Error. Unable to print some characters.")
    except twitter.error.TwitterError:
        tweet = "User not found."
    return tweet

def get_tweets_by_keyword(api, word):
    '''takes api and keyword and returns tweets with keyword'''

        
    status = api.GetSearch(word)
    tweets = []
    #goes through 20 status
    for i in status[0:20]:
        try:
            #checks if the text can be printed
            print(i.text)
            #if so appends it
            tweets.append(i.text)
        except UnicodeEncodeError:
            #if not prints error and keeps going
            print("Error. Unable to print some characters.")
                

    return tweets

def get_trending_topics(api):
    '''takes api and returns trending topcs'''
    #gets trending topics
    trending = api.GetTrendsCurrent()
    trends = []
   
    for i in trending[0:20]:
        #checked if each could be printed before appending
        try:
            #returns just topics
            print(i.name)
            q = i.name
            trends.append(q)
        except UnicodeEncodeError:
            print("Couldn't print the text.")
            
    return trends

def get_trending_tweets(api):
    '''takes api and returns dictionary with trending topics as keys and tweets as values'''
    #gets trending topics
    trends = get_trending_topics(api)
    #creates dictionary with topcs as keys
    d = {}
    
    for i in range(0,10):
        try:
            #checked if each could be printed before appending
            print(get_tweets_by_keyword(api, trends[i])[1:3])
            d[trends[i]] = get_tweets_by_keyword(api, trends[i])[1:3]
        except UnicodeEncodeError:
            print("Couldn't print the text.")

    return d

def get_trending_users(api):
    '''takes api and returns dictionary with trending topics as keys and users as values'''
    #gets trending topics
    trends = get_trending_topics(api)

    #creates dictionary with trending topcs as keys and users that have posted about them as values
    d = {}
    for i in range(0,10):
        status = api.GetSearch(trends[i])
        
        tweets = []
        for t in status[0:4]:
            #checked if each could be printed before appending
            try:
                print(t.user.screen_name)
                tweets.append(t.user.screen_name)
            except UnicodeEncodeError:
                print("Couldn't print the text.")
        d[trends[i]] = tweets
    return d




# ----------------------------------------------------------
# New Location Functions

def get_addr_from_cood(client, lat, long):
    '''gets address from coordinates'''
    #gets address info from reverse geocode
    loca = client.reverse_geocode([lat, long])
    #gets just the address
    final = loca[0]['formatted_address']
    return print(final)

def get_cood_from_addr(client, address):
    '''gets coordinates from address'''
    #address info from address
    latlong = client.geocode(address)
    #finds the lat long
    part = latlong[0]['geometry']['location']
    final = [part['lat'],part['lng']]
    return print(final)

def get_place_name_from_cood(client, lat, long):
    '''gets name of place from coordinates'''
    #gets adress info from lat long
    loca = client.reverse_geocode([lat, long])
    address = loca[0]['formatted_address']
    #gts address
    #gets name from address
    latlong = client.places(address)
    final = latlong['results'][0]['name']
    return print(final)

def get_place_name_from_addr(client, address):
    '''gets name of place from address'''
    latlong = client.places(address)
    final = latlong['results'][0]['name']
    return print(final)

def get_tweet_place_name(api, tweet):
    '''gets place name from tweet'''
    
    

    
    return tweet.user.location

def get_tweets_near_location(api, lat, long, radius):
    
    return None





# ----------------------------------------------------------
# Search Function

def search(twitter_api):
    ''' primary function to be written '''
    done = False
    #create while loop
    while not done:
        #print options
        print("Search by:\n1. User\n2. Keyword\n3. Trending Topic")
        choice = input("Which way would you like to search by? ")
        print()
        if choice == '1':
            try:
                #input username and finds tweet by users
                user = input("Enter username: ")
                print()
                tweeter = get_tweets_by_user(twitter_api, user)
                print()
                location = input("Would you like to see the time of the most recent tweet? Y or N? ")
                if location == 'Y' or location == 'y':
                    print()
                    tweets = twitter_api.GetUserTimeline(screen_name=user)
                    
                    print(tweets[0].created_at)
            except UnicodeEncodeError:
                print("Can't print the text.")
        if choice == '2':
            try:
                #inputs keyword and searches tweets with keyword
                keyword = input("Enter a keyword: ")
                print()
                get_tweets_by_keyword(twitter_api, keyword)
                print()
                search = input("Would you like to see recent users who have tweeted this keyword? Y or N? ")
                if search == 'Y' or search == 'y':
                    status = twitter_api.GetSearch(keyword)
                    people = []
                    print()
                    for i in status[0:10]:
                        people.append(i.user.screen_name)
                    print(people)
            except UnicodeEncodeError:
                print("Can't print the text.")
        if choice == '3':
            try:
                search_by_trending(twitter_api)
            except UnicodeEncodeError:
                print("Can't print the text.")
        #checks if they want to search again
        print()
        option = input("Would you like to search again? (y/n) ")
        if option == 'n':
            done = True
            print()
            #if not while loop ends and prints goodbye
            print("Goodbye")
        print()
    return ''





# ----------------------------------------------------------
# Write Any Helper Functions Here
# ----------------------------------------------------------

def tweet_date( date_str ):
    try:
        date = datetime.datetime.strptime(date_str,
                                          '%a %b %d %H:%M:%S %z %Y')
        return date.strftime(' at %I:%M %p on %a %d, %Y')
    except Exception as e:
        print('Error in get_tweet_data: ' + e)
        return ''

def search_by_trending(api):
    try:
        #prints out the trending topcs
        print("These are the trending topcs.")
        print()
        thing = get_trending_topics(api)
        print()
        #asks which they would like to search by
        number = int(input("Which topic would you like to search by? (0-10) "))
        one = thing[number]
        print()
        #searches with the topic as keyword
        get_tweets_by_keyword(api, one)
    except UnicodeEncodeError:
        print("Can't print the text.")
    return ""




# ----------------------------------------------------------
# Provided Functions: Do Not Change
# ----------------------------------------------------------

def get_twitter_api(consumer_key=consumer_key, consumer_secret=consumer_secret):
    ''' creates an Api object using the consumer_key and consumer_secret
        defined above
    '''
    try:
        return twitter.Api(consumer_key=consumer_key,
                           consumer_secret=consumer_secret,
                           application_only_auth=True,
                           sleep_on_rate_limit=True)
    except twitter.error.TwitterError as e:
        print('Error in get_api: ' + e)
        return False

def test_twitter_connection(consumer_key=consumer_key,
                            consumer_secret=consumer_secret,
                            screen_name=test_screen_name ):
    ''' simple test to verify program is connected to twitter properly '''
    try:
        api = get_twitter_api()    
        timeline = api.GetUserTimeline(screen_name=screen_name)
        most_recent_tweet = timeline[0]
        print(most_recent_tweet.text)
    except twitter.error.TwitterError as e:
        print('Error in test_connection: ' + e)
        return False


def get_gmaps_client(geocode_api_key=geocode_api_key):
    ''' get google maps client with given api key '''
    return googlemaps.Client(key=geocode_api_key)

def test_gmaps_connection(geocode_api_key=geocode_api_key,
                          address=test_address):
    ''' test connection to google maps library '''
    gmaps_client = googlemaps.Client(key=geocode_api_key)
    geocode_result = gmaps_client.geocode(address)
    print_result(geocode_result)

def print_result(result):
    '''print each dictionary in the result list returned from gmaps '''
    for D in result:
        print_dict(D, 0)

def print_dict(D, tabs):
    '''print items in a dictionary indented with dotted lines between'''
    indent = '    ' * tabs
    for k,v in D.items():
        if tabs == 0:
            print('----------------------------------')
        if type(v) == dict:
            print(indent + str(k) + ': ')
            print_dict(v, tabs+1)
        elif type(v) == list:
            print(indent + str(k) + ': ')
            print_list(v, tabs+1)
        else:
            print(indent + str(k) + ' = ' + str(v))
    if tabs == 0:
        print('----------------------------------')
            
def print_list(L, tabs):
    '''print items in a list indented with dotted lines between'''
    indent = '    ' * tabs
    for i in range(len(L)):
        if type(L[i]) == list:
            print_list(L[i], tabs+1)
        elif type(L[i]) == dict:
            print_dict(L[i], tabs)
        else:
            print(indent + str(L[i]))
        if i < len(L)-1:
            print(indent + '..............' + '....' * (5 - tabs))


