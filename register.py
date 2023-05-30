import json_utilies
def register(sname,scourse):
    data=json_utilies.student("data/student.json")
    student_json={
        "sno":len(data["students"])+1,
        "student_name":sname,
        "student_course":scourse,
        "student_status":"open"
    }
    
    data["students"].append(student_json)
    json_utilies.write("data/student.json",data)
    
    