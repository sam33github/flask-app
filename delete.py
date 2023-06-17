import json_utilies
def delete(Sno):
    data=json_utilies.student("data/student.json")
    deleted=False
    for student in data["students"]:
       if deleted==True:
            student["sno"]-=1
            print(student)
       if str(student["sno"])==str(Sno) and deleted==False:
           data["students"].remove(student)  
           data["students"][Sno-1]["sno"]=Sno
           deleted=True

    json_utilies.write("data/student.json",data)
