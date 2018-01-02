class AthleteList(list):
    def __init__(self,a_name,a_dob=None,a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return(sorted(set([self.sanitize(t) for t in self]))[0:3])


    def sanitize(self,time_string):
        if '-' in time_string:
            splitter='-'
        elif ':' in time_string:
            splitter=':'
        else:
            return(time_string)

        return (time_string.replace(splitter,'.'))

# def get_coach_data(filename):
#     try:
#         with open(filename) as f:
#             data = f.readline()
#         templ = data.strip().split(',')
#         return(AthleteList(templ.pop(0),templ.pop(0),templ))
#     except IOError as ioerr:
#         print("file error:" + str(ioerr))
#         return(None)
#
# julie = get_coach_data("julie.txt")
# julie.append("1.23")
# julie.extend(["1.33"])
# print(julie.name  + " chengji : " + str(julie.top3()))
