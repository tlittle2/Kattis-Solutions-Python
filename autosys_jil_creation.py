#Purpose: Create equivalent Autosys JIL file for job order from another job scheduler framework (CA7, airflow, etc)

prefix = "ora_d_c"
job1 = 'job1'
job2 = 'job2'
job3 = 'job3'
job4 = 'job4'

box1 = "qrsopsd1"
box2 = "qrsdly02"
box3 = "qrsdly01"

def prefixAndJob(ip): return "{}_{}".format(prefix, ip)


def assignToBox(collection):
    d = {"{}".format(i): [] for i in collection}
    d[job1] = box1
    d[job2] = box1
    
    d[job3] = box2
    d[job4] = box3
    
    return d


def boxName(collection, ip):
    boxMap = assignToBox(collection)

    if ip in boxMap.keys():
        return boxMap[ip]
    else:
        return ""



def calendar(collection, ip): #using exclude calendar for now, can be customized
    calendarMap = {"{}".format(i): "BOMC_p1" for i in collection}

    return calendarMap[ip]


def createDependencies(collection):
    d = {"{}".format(i): [] for i in collection}

    #job name : upstream dependencies
    d[job3] = [job1, job2]
    d[job4] = [job3]

    return d

def dependencies(collection, ip):
    adjacencyList = createDependencies(collection)

    string = ""

    for k,v in adjacencyList.items():
        if ip == k:
            if len(v) > 0:
                for i in range(len(v)):
                    string += " & s({},0)".format(prefixAndJob(v[i]))

                return "condition: {}".format(string)
            else:
                return ""


def main():
    collection = [job1, job2, job3, job4]

    for i in collection:
        print("/*********************{}*********************/".format(prefixAndJob(i)))
        print("insert_job: {}".format(prefixAndJob(i)))
        print(dependencies(collection, i).replace("condition:  &", "condition:")) # move & for first job in dependency condition
        print("exclude_calendar: {}".format(calendar(collection, i)))
        print("box_name: ora_d_b_{}".format(boxName(collection, i)))
        print("alarm_if_fail: true")
        print("alarm_if_terminated: true")
        print("\n")
   
        
if __name__ == "__main__": 
    main()
