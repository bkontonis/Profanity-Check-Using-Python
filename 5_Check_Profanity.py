import urllib3
import json

def read_text():
    quotes = open("./5_movie_quotes.txt")
    contents_of_files = quotes.read()
    print(contents_of_files)
    contents_of_files = contents_of_files.replace('\n', ' ').replace('\r', '').replace('\t', '').replace(' ', '')
    quotes.close()
    check_profanity(contents_of_files)

def check_profanity(text_to_check):
    http = urllib3.PoolManager()
    connection = http.request("GET", "http://www.wdylike.appspot.com/?q="+text_to_check)
    output = json.loads(connection.data.decode('utf-8'))
    #print('\n\n'+str(output))
    if output==True:
        print("\n\nProfanity alert!!!")
    elif output==False:
        print("\n\nThis document has to curse words!")
    else:
        print("\n\nCould not scan document properly.")

read_text()

