#Check on TFT data and update the mysql database

#~~~~~Libraries~~~~~
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import json
import urllib.request
#~~~~~~~~~~~~~~~~~~~    

#~~~~~Global Variable~~~~~
API_KEY = '?api_key=RGAPI-65c978e9-fc20-47df-9621-0a34c2826471'
USER_NAME = 'DotsXL'
#~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~Functions~~~~~
#Establish connection with MySQL database
def mysql_server_connect():
    try:
        connection = mysql.connector.connect(host='localhost',
                             database='sql_match_history',
                             user='shayshu',
                             password='datalog')

        return connection
    except mysql.connector.Error as error :
        print("Failed to connect to database {}".format(error))

#Close connection with MySQL database
def mysql_server_close(connection):
    try:
        connection.close()
    except mysql.connector.Error as error :
        print("Failed to close database connection {}".format(error))

#Return the match history
def mysql_get_match_history(ID):
    
    try:
        connection = mysql_server_connect()
        cursor  = connection.cursor()
        sql_query = """select * from match_history"""
        cursor.execute(sql_query, (ID))
        records = cursor.fetchall()

        #Print out each row from the database
        for row in records:
            print(row[0])
            print(row[1])
            print(row[2])

        return records

    except mysql.connector.Error as error :
        print("Failed to read {}".format(error))

def check_new_entry(match_id):
    try:
        connection = mysql_server_connect()
        cursor  = connection.cursor()
        sql_query = """select * from match_history where Match_History_ID = %s"""
        cursor.execute(sql_query, (match_id))
        records = cursor.fetchall()

        #Print out each row from the database
        for row in records:
            print(row[0])
            print(row[1])
            print(row[2])

        return records

    except mysql.connector.Error as error :
        print("Failed to read {}".format(error))

#Make a requrest to riot api and get the puuid from an:
#API key, and summoner name, 
def get_puuid(key, summonerName):
    url_request = 'https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-name/' +  summonerName + key
    responseJson = requests.get(url_request).json()
    puuid = responseJson['puuid']

    return puuid

#Get the number of matches and their respective ids
def get_match_ids(key, puuid):
    url_request = 'https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/' + puuid + '/ids' + key
    responseJson = requests.get(url_request).json()
    match_ids = responseJson

    return match_ids

#Get the match data for a given match id
def get_match_data(key, match_id):
    url_request = 'https://americas.api.riotgames.com//tft/match/v1/matches/' + match_id + key
    responseJson = requests.get(url_request).json()

    return responseJson
    
#~~~~~~~~~~~~~~~~~~~

