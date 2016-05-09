# coding: Shift_JIS

import re
import json
import codecs
import string
from twitter import *
from datetime import datetime
from datetime import timedelta
from subprocess import Popen, PIPE

#�Ď�����
INTERVAL = timedelta(seconds=3600);

#data.txt����N�����ɂԂ₫�����Q�[���̃^�X�N�����擾
def gamelist():
    gamenames = [];
    data = open("./data.txt");
    for s in data:
        s = s.replace("\n", "");
        gamenames.append(s);
    return gamenames;

def main():
    #json�����[�h����twitter�ɐڑ�
    with open("secret.json") as f:
        secretjson = json.load(f);
    t = Twitter(auth=OAuth(secretjson["access_token"], secretjson["access_token_secret"], secretjson["consumer_key"], secretjson["consumer_secret"]));
    
    cmd = "tasklist";
    previous = datetime.now();
    games = gamelist();
    hour = [-1] * len(games);
    first = True; #�N�����Ɏ��s����p
    
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
                        tweet = "I'm playing " + games[i] + " (" + str(hour[i]) + "���Ԗ�)";
                        #print(tweet);
                        check = True;
                        t.statuses.update(status=tweet);
                if not check :
                    hour[i] = -1;


if __name__ == "__main__":
    main();
