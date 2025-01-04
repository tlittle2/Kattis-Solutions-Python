"""
Purpose: Create equivalent Autosys JIL file for job order from another job scheduler framework (CA7, airflow, etc)

Concept: 
1. Store each job name as a variable, and stores equivalent string value as the variable. Make them global
2. Add to master collection main, and pass the collection to calling methods
3. Create static structures to help determine certain values for the JIL file for particular jobs (what autosys box, what job dependencies)
    a. This should be make it easy to understand how certain parts of the JIL file get created for a particular job
4. Pass what is found in the data structure back to the calling method, and let calling method take care of generating the JIL parameter text
"""

prefix = "ora_d_c"
job1 = 'job1'
job2 = 'job2'
job3 = 'job3'
job4 = 'job4'

box1 = "opsd1"
box2 = "dly02"
box3 = "dly01"

def prefixAndJob(ip):
    return "{}_{}".format(prefix, ip)


def assignToBox(collection):
    d = {"{}".format(i): "" for i in collection}
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



def calendar(collection, ip): #using 1 exclude calendar for now, can be customized
    calendarMap = {"{}".format(i): "BOMC_p1" for i in collection}

    return calendarMap[ip]


def createDependencies(collection):
    d = {"{}".format(i): [] for i in collection}

    #job name : upstream dependencies
    d[job3] = [job1, job2]
    d[job4] = [job3]

    return d

def dependencies(collection, ip):
    adjacencyDict = createDependencies(collection)

    string = ""
    
    for k,v in adjacencyDict.items():
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
        dependencies(collection, i)
        print(dependencies(collection, i).replace("condition:  &", "condition:")) # remove & for first job in dependency condition
        print("exclude_calendar: {}".format(calendar(collection, i)))
        print("box_name: ora_d_b_{}".format(boxName(collection, i)))
        print("alarm_if_fail: true")
        print("alarm_if_terminated: true")
        print("\n")
   
        
if __name__ == "__main__": 
    main()
