#Purpose: Create equivalent Autosys JIL file for job order from another job scheduler framework (CA7, airflow, etc)

prefix = "ora_d_c"
job1 = 'job1'
job2 = 'job2'
job3 = 'job3'


def createDependencies(collection):
    d = {"{}".format(i): "" for i in collection}
    
    d[job1] = [job2, job3]
    d[job2] = [job3]

    return d

def dependencies(collection, ip):
    adjacencyList = createDependencies(collection)

    string = ""

    for k,v in adjacencyList.items():
        if ip == k:
            if len(v) > 0:
                for i in range(len(v)):
                    string += " & s({}_{},0)".format(prefix, v[i])

                return "condition: {}".format(string)
            else:
                return ""


def main():
    collection = [job1, job2, job3]

    for i in collection:
        print("/*********************{}_{}*********************/".format(prefix,i))
        print("insert_job: {}_{}".format(prefix,i))
        print(dependencies(collection, i).replace("condition:  &", "condition:"))
        print("\n")
   
        
if __name__ == "__main__": 
    main()
