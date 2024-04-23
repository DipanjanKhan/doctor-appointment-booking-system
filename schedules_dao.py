from app.mysql_connection import mysql_connection

def get_schedule(doctor_id):
    connection = mysql_connection()
    cursor = connection.cursor()
    schedules = []
    query_schedule = "select schedule_day, schedule_time from doctors_schedules where doctor_id = %s"
    cursor.execute(query_schedule, doctor_id)
    for (schedule_day, schedule_time) in cursor:
        schedule = str(schedule_day) + " " +  str(schedule_time)
        schedules.append(schedule)
    
    cursor.close()
    connection.close()
    return schedules

def add_schedule(doctor_data):
    connection = mysql_connection()
    cursor = connection.cursor()
    query = "insert into doctors_schedules(doctor_id, schedule_day, schedule_time) values(%s, %s, %s)"
    data = (doctor_data["doctor_id"], doctor_data["schedule_day"], doctor_data["schedule_time"])
    cursor.execute(query, data)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    # data = {
    #     "doctor_id": 1,
    #     "schedule_day": "Tuesday",
    #     "schedule_time": "5pm to 7pm"
    # }
    # add_schedule(data)
    schedules = get_schedule(1)
    # print(schedules)