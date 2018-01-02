import pickle
from Athlete import AthleteList

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return(AthleteList(templ.pop(0),templ.pop(0),templ))
    except IOError as ioerr:
        print("file error:" + str(ioerr))
        return(None)
def put_to_store(files_lists):
    all_athletes = {}
    for each_file in files_lists:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open("athletes.pickle",'wb') as athf:
            pickle.dump(all_athletes,athf)
    except IOError as ioerr:
        print('file error(put_to_store)' + str(ioerr))
    return(all_athletes)
def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle','rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('file err(get_from_store)' + str(ioerr))
    return (all_athletes)

filelists = ['julie.txt','james.txt']
put_to_store(filelists)
lists = get_from_store()

for each_itme in lists:
    print(lists[each_itme])
