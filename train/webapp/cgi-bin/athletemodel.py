#! --*-- coding: utf-8 --*--
__author__ = 'gaoxingsheng'

import pickle

import AthleteList
from AthleteList import sanitize

def get_coach_data(filename):
    # not shown here as it has not changed since the last chapter
    # return {'name': filename}

    try:
        with open(filename, "r") as athf:
            data = athf.read()
            print data
            data = data.replace('\n', '')
            data = data.split(',')
            data = [sanitize(each) for each in data]
    except IOError as ioerr:
        print("File error (get_coach_data):" + str(ioerr))

    name = filename.split('/')[1].split('.')[0]
    return {'name': name, 'data': data}


def put_to_store(files_list):
    all_athletes = {}

    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath['name']] = ath

    print all_athletes
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print('File error (put_to_store:) ' + str(ioerr))

    return all_athletes


def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File error (get_from_store):' + str(ioerr))

    return all_athletes


# the_files = ['james.txt', 'julie.txt', 'mikey.txt', 'sarah.txt']
# per_fix = "data"
# full_files = []
# for each in the_files:
#     full_files.append(per_fix + '/' + each)

# print full_files
# data = put_to_store(full_files)
# print data