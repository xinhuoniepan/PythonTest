
def openFile(filename):
    with open(filename) as f:
        sortfile = f.readline().strip().split(',')
        (name,time) = sortfile.pop(0),sortfile.pop(0)
        top3file = sorted(set([sanitize(each_time) for each_time in sortfile]))[0:3]
        print(name +'de cheng ji shi :' + str(top3file))

def sanitize(time_string):
    if '-' in time_string:
        spliter = '-'
    elif ':' in time_string:
        spliter = ':'
    else:
        return time_string
    (min,secs) = time_string.split(spliter)

    return(min + '.' + secs)

# def delete_samedata(topfile):
#     top3file = []
#     for item in topfile:
#         if item not in top3file:
#             top3file.append(item)
#     return top3file

openFile('james2.txt')
openFile('julie2.txt')
openFile('mikey2.txt')
openFile('sarah2.txt')


