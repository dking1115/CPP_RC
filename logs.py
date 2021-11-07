import time
def write(path,data):
    try:
        log=open(path,'a')
        log.write("\n%s"%(str(data)))
        log.close()
    except:
        print('log write error')
def read_last(path):
    try:
        log=open(path,'r')
        last=""
        for line in log:
            pass
            last = line
        log.close()
        return last
    except:
        error='log read error'
        print(error)
def error_log(folder,error):
    print(error)
    write("%s/logs/Error_log.txt"%(folder),'%s,%s'%(error,time.time()))

def writew(path,data):
    try:
        log=open(path,'w')
        log.write("\n%s"%(str(data)))
        log.close()
    except:
        print('log write error')