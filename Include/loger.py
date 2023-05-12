import datetime
def log(data,status):
    x = datetime.datetime.now()
    runlog= open('../logs/runtime.txt',"a")
    runlog.write(str(data)+"-----"+str(x)+"\n")
    runlog.close()
    if status==True:
        print(data)