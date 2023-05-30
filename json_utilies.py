import json
def student(file):
    f=open(file)
    data=json.load(f)
    f.close()
    return data

def write(f,data):
    fw=open(f,"w")
    data2=json.dumps(data,indent=3)
    fw.write(data2)
    fw.close()
   