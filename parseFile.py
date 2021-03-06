import yaml
import csv
import os
import sys
import traceback
import logging

class iplMatch:
    # This is Match class.
    iMatchCount = 0
    iMatchID = 0
    strSourceFileName = 0
    def __init__(self, strFileName):
        #print strFileName
        self.strSourceFileName = strFileName
        stream =  file(strFileName, 'r')
        yamlMatchData = yaml.safe_load(stream)
        self.strMatchVenue = yamlMatchData['info']['venue']
        self.strMatchCity = yamlMatchData['info']['city']
        self.strMatchDate = str(yamlMatchData['info']['dates'][0])
        self.strHomeTeam = yamlMatchData['info']['teams'][0]
        self.strAwayTeam = yamlMatchData['info']['teams'][1]
        #if (yamlMatchData['info']['outcome']['result']):   
        self.strWinner = yamlMatchData['info']['outcome']['winner']
        self.strTossWinner = yamlMatchData['info']['toss']['winner']
        self.strTossDecision = yamlMatchData['info']['toss']['decision']
        self.strWinType = yamlMatchData['info']['outcome']['by']
        self.strMoM = yamlMatchData['info']['player_of_match'][0]


    def displayMatchDetails(self):
        print "Match : ", self.strHomeTeam, " _vs_ ", self.strAwayTeam
        print "" \
              "Venue : ", self.strMatchVenue, ",", self.strMatchCity
        print "" \
              "On : ", self.strMatchDate
        print "" \
              "Toss Won by : ", self.strTossWinner, " Decided to ", self.strTossDecision
        print "" \
              "Won by ", self.strWinner, " by ", self.strWinType.keys()[0], " : ", self.strWinType.values()[0]
        print "" \
              "Man of the Match : ", self.strMoM
        #print self.strSourceFileName

    def reset(self):
        self.strMatchVenue = 0
        self.strMatchCity = 0
        self.strMatchDate = 0
        self.strHomeTeam = 0
        self.strAwayTeam = 0
        self.strWinner = 0
        self.strTossWinner = 0
        self.strTossDecision = 0
        self.strWinType = 0
        self.strMoM = 0

    def toArray(self):
        data = '|'.join([self.strHomeTeam, self.strAwayTeam, self.strMatchVenue, self.strMatchCity, self.strMatchDate, self.strTossWinner, self.strTossDecision, self.strWinner,self.strWinType.keys()[0], str(self.strWinType.values()[0]) ,"\n"])
        return data

if(sys.argv[1] == 'DIR'):
    path = sys.argv[2]
    fd = open('document.csv','wb')
    for files in os.listdir(path):
        current_file = os.path.join(path, files)
        try:
            iplMatchData = iplMatch(current_file)
            data = iplMatchData.toArray()
            fd.write(data)
        except KeyError:
            print ("Failed" + current_file)
            pass
        iplMatchData.reset()
else:
    strAbsFilePath = sys.argv[2]
    iplMatchData = iplMatch(strAbsFilePath)
    data = iplMatchData.toArray()
    print data

fd.close()
