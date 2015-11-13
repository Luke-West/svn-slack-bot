#!/usr/bin/python
#Luke West (luke.west@elder-studios.co.uk)
#A bot to notify certain clients when changes are made to svn

#I would like to say thank you to Scott Vitale for the original working copy of this program and give
#him credit for some very good work.
#his email: svvitale@gmail.com

import os
import sys
import subprocess
import re
import json
import requests
import time

# svnlook location
LOOK="svnlook"

######################################################################
######################################################################
################### Edit below at your own ###########################
###################         risk           ###########################
######################################################################
######################################################################

def slack_bot( msg ):
  #A bot to post messages to slack regarding the current status of the deploy
  #The empty attachment here is used as a way of creating a space between messages. Remove/edit this according to your desired message layout

  url = '**Slack API here**'

  payload = {
     "text": msg,
     "channel": "#**slack room here**",
     "username": "svn-bot",
     "icon_url": "Desired bot image (can copy link straight from the web)",
     "attachments":[{
       "text": None
     }]
  }
  
  try:
    response = requests.post(url, data=json.dumps(payload))
    print("An update has been posted to Slack.")
  except:
    pass
  
def runLook( *args ):
  # check_output will except if it fails so we don't spam the room with 'run svnlook help for help' messages
  return subprocess.check_output( ' '.join([LOOK] + list(args)), shell=True, stderr=subprocess.STDOUT)

def getCommitInfo( repo, revision ):
  comment = runLook("log", repo, "-r", revision)
  author = runLook("author", repo, "-r", revision)
  files = runLook("changed", repo, "-r", revision)

  chatMsg = ("""
[%s] %s committed revision %s
%s
Changed Files:
%s
""" % (repo, author.rstrip(), revision, comment, files)).strip()
  
  return chatMsg

def GetRevision():
  #This will do 10 checks for new commits. The repository path needs setting here.
  times_to_execute = 10
  i = 0
  while i < times_to_execute:
    with open("revision_number.txt", "r+") as revision:
      current_revision = int(revision.readline())
    try:
      chatMsg = getCommitInfo('//path to repository/', str(current_revision + 1))
      print(chatMsg)
      with open("revision_number.txt", "w") as revision:
  	    revision.write(str(int(current_revision+1)))
  	    revision.close()
    except:
      print("There has been no new commit made.")
    i = i + 1
    time.sleep(5)
  exit()

if __name__ == "__main__":
  GetRevision()


