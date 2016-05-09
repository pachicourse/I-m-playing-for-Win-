# coding: Shift_JIS

import re
import json
import codecs
import string
from twitter import *
from datetime import datetime
from datetime import timedelta
from subprocess import Popen, PIPE

#監視周期
INTERVAL = timedelta(seconds=3600);

#data.txtから起動時につぶやきたいゲームのタスク名を取得
def gamelist():
    gamenames = [];
    data = open("./data.txt");
    for s in data:
        s = s.replace("\n", "");
        gamenames.append(s);
    return gamenames;

def main():
    #jsonをロードしてtwitterに接続
    with open("secret.json") as f:
        secretjson = json.load(f);
    t = Twitter(auth=OAuth(secretjson["access_token"], secretjson["access_token_secret"], secretjson["consumer_key"], secretjson["consumer_secret"]));
    
    cmd = "tasklist";
    previous = datetime.now();
    games = gamelist();
    hour = [-1] * len(games);
    first = True; #起動時に実行する用
    
    while True:
        if datetime.now() - previous > INTERVAL or first:
            first = False;
            previous = datetime.now();
            #print("done");
            for i in range(0, len(games)):
                check = False;
                p1 = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE);
                for line in p1.stdout.readlines():
                    if re.search(games[i], line.decode("shift-jis")) and not check :
                        hour[i] = hour[i] + 1;
                        tweet = "I'm playing " + games[i] + " (" + str(hour[i]) + "時間目)";
                        #print(tweet);
                        check = True;
                        t.statuses.update(status=tweet);
                if not check :
                    hour[i] = -1;


if __name__ == "__main__":
    main();
