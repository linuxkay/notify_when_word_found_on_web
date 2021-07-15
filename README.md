# notify_when_word_found_on_web

## Overview

Notify when specific word found on web

## Category

Python Script

## Description

## Demo in Animation

## Requirements

## Install

python3.x

pip install requests smtblib BeautifulSoup4

anaconda setup

## install python3.5 with the name wordbot
conda create -n wordbot python=3.5

conda infor -e // check newly created environment.

## activate wordbot

conda activate wordbot

## add repository for more search/install

conda config --append channels conda-forge

## Install package independently.
conda install BeautifulSoup4

## pip and anaconda setup

use requirements.txt for pip.

use myenv.yaml for Anaconda.

Run following command for setup using myenv.yaml.

`conda env create -f=myenv.yaml`

Export installed package on conda by

`conda env export > myenv.yaml`

For pip export,

`conda list -e > requirements.txt`

## Usage

Test run in regular environment

`conda activte wordbot`

Find out python path on anaconda`

`which python`

Exit conda env

`conda deactivate`

Run wordbot

`home/pi/berryconda3/envs/wordbot/bin/python3 /home/pi/Workspace/word_notification_v1.py`

Running in cron

Log stored at /var/tmp/wordbot.log

Run on second Wednesday at 9AM

`0 9 8-14 * *  [ $(date "+\%w") -eq 3 ] && /home/pi/berryconda3/envs/wordbot/bin/python3 /home/pi/Workspace/word_notification_v1.py > /var/tmp/wordbot.log 2>&1`

Run on second Thursday at 9AM

`0 9 8-14 * *  [ $(date "+\%w") -eq 4 ] && /home/pi/berryconda3/envs/wordbot/bin/python3 /home/pi/Workspace/word_notification_v1.py > /var/tmp/wordbot.log 2>&1`

Run on thrid Wednesday at 9 AM

`0 9 15-21 * *  [ $(date "+\%w") -eq 3 ] && /home/pi/berryconda3/envs/wordbot/bin/python3 /home/pi/Workspace/word_notification_v1.py > /var/tmp/wordbot.log 2>&1`

Run on third Thursday at 9AM

`0 9 15-21 * *  [ $(date "+\%w") -eq 4 ] && /home/pi/berryconda3/envs/wordbot/bin/python3 /home/pi/Workspace/word_notification_v1.py > /var/tmp/wordbot.log 2>&1`

Ideally set timer on systemctl.

## Contributions

## Updates

## Memo

## Feature upgrades

Scrap url using scarp_url.py  Source https://mmsankosho.com/nlp-1/

use selenium to get dynamic URL.

## ToDo

~~Create anaconda env.~~ 7/13/2021

~~Check date and parse string just for "Year-and-Month"~~ 7/12/2021

~~Expamle 2021-07-22 --> 2021-07~~ 7/12/2021

~~Run on second and third Wednesday in cron.~~ 7/14/2021

## Licence
[MIT]

## Author

[linuxkay](https://github.com/linuxkay)
~                                        
