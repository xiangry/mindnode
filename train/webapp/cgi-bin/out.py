#! --*-- coding: utf-8 --*--
__author__ = 'gaoxingsheng'


import  athletemodel
import  htemplate as yate
import glob

data_files = glob.glob('data/*.txt')
athletes = athletemodel.put_to_store(data_files)

all_text = ''

all_text += yate.start_response()
all_text += yate.include_header("Coach Kelly's List of Athletes")
all_text += yate.start_from("out.py")
all_text += yate.para("Select an athlete from the list to work with:")

for each_athlete in athletes:
    all_text += yate.radio_button("which_athlete", athletes[each_athlete].name)

all_text += yate.end_form("Select")

all_text += yate.include_footer({"Home": "/index.html"})


index = open("index.html", "wb")
index.write(all_text)
index.close()0