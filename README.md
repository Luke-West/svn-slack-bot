# This project is no longer supported

I created this script years ago (in my days of being an apprentice). It's not updated anymore and if you choose to use it, 
you're on your own. It's a simple script and anyone of novice level or above should be able to work out how to use it.

-----------------

# Post messages to slack upon new commits to SVN Repository

This script is created to publish information to Slack when SVN commits occur. 

Required files/Application/services:
    * Subversion: http://subversion.tigris.org/
    * Working repository
    * Slack Domain and room

The user MUST edit the script file to add in
    * Slack API
    * Slack room name
    * a user name for display in Slack
    * location of svnlook command.
    * Edit revision_number.txt to latest revision if SVN repository isn't new to avoid a message being posted for every
      commit ever made.

I advice that you set this up with cron. When the program is run it will check for any new commits and then end. Set this up with cron to 
startup and run every 60 minutes or so and it will do all the work automatically.
