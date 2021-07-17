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

## chromedriver setup on ubuntu

First uninstall selenium and chromedriver

`pip3 uninstall selenium`

`pip3 uninstall chromedriver`

Install selenium from ubuntu repository(it will install chromedriver also).

`sudo apt -y install python3-selenium`

Optional install webdriver-manager

`pip3 install webdriver-manager`

## References

https://www.mt-megami.com/article/ubuntu-python3-selenium-googlechrome-scraping

**For changing windows**

https://stackoverflow.com/questions/66568508/selenium-switch-to-popup-window

**Loop**

https://qiita.com/rosuke/items/04d86316cbd733d4b6e8

https://www.it-swarm-ja.com/ja/python/python%E3%81%A7selenium%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%A6%E3%81%99%E3%81%B9%E3%81%A6%E3%81%AEhref%E3%83%AA%E3%83%B3%E3%82%AF%E3%82%92%E5%8F%96%E5%BE%97%E3%81%97%E3%81%BE%E3%81%99/822552195/

**window handling**

https://www.seleniumqref.com/api/python/window_get/Python_window_handles.html

**scrap url**

Scrap url using scarp_url.py  Source https://mmsankosho.com/nlp-1/

**About xpath**

https://qiita.com/rllllho/items/cb1187cec0fb17fc650a

https://www.octoparse.jp/blog/xpath-introduction/

**Work on errors**

https://stackoverflow.com/questions/61299653/attributeerror-webdriver-object-has-no-attribute-switch-to-window-handles

## Future studies

https://qiita.com/Azunyan1111/items/b161b998790b1db2ff7a

## Contributions

## Updates

## Memo

## Feature upgrades


## ToDo

~~Create anaconda env.~~ 7/13/2021

~~Check date and parse string just for "Year-and-Month"~~ 7/12/2021

~~Expamle 2021-07-22 --> 2021-07~~ 7/12/2021

~~Run on second and third Wednesday in cron.~~ 7/14/2021

~~use selenium to get dynamic URL.~~ 7/17/2017

## Licence
[MIT]

## Author

[linuxkay](https://github.com/linuxkay)
~                                        
