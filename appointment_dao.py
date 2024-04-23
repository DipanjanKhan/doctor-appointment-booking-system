from mysql_connection import mysql_connection

def get_appointment_details(doctor_id, appointment_date):
    connection = mysql_connection()
    cursor = connection.cursor()
    query = "select * from appointments_list where doctor_id = %s and appointment_date = '%s'"
    cursor.execute(query, (doctor_id, appointment_date))
    appointment_details = []
    
    for (doctor_id, patient_name, appointment_date) in cursor:
        appointment_details.append({
            "doctor_id": doctor_id,
            "patient_name": patient_name, 
            "appointment_date": appointment_date
        })
    cursor.close()
    connection.close()
    return appointment_details

def get_all_appointment_details():
    connection = mysql_connection()
    cursor = connection.cursor()
    query = "select * from appointments_list "
    cursor.execute(query)
    appointment_details = []
    for (doctor_id, patient_name, appointment_date) in cursor:
        appointment_details.append({
            "doctor_id": doctor_id,
            "patient_name": patient_name, 
            "appointment_date": appointment_date
        })
    cursor.close()
    connection.close()
    return appointment_details

def get_appointment_details_date(date):
    connection = mysql_connection()
    cursor = connection.cursor()
    query = "select * from appointments_list where appointment_date = '%s'"
    cursor.execute(query, date)
    appointment_details = []
    
    for (doctor_id, patient_name, appointment_date) in cursor:
        appointment_details.append({
            "doctor_id": doctor_id,
            "patient_name": patient_name, 
            "appointment_date": appointment_date
        })
    cursor.close()
    connection.close()
    return appointment_details

def get_appointment_details_doctor(doctor_id):
    connection = mysql_connection()
    cursor = connection.cursor()
    query = "select * from appointments_list where doctor_id = %s"
    cursor.execute(query,(doctor_id))
    appointment_details = []
    
    for (doctor_id, patient_name, appointment_date) in cursor:
        appointment_details.append({
            "doctor_id": doctor_id,
            "patient_name": patient_name, 
            "appointment_date": appointment_date
        })
    cursor.close()
    connection.close()
    return appointment_details

def insert_appointment_details(data):
    connection = mysql_connection()
    cursor = connection.cursor()
    query = "insert into appointments_list (doctor_id, patient_name, appointment_date) values(%s, %s, %s)"
    appointment_data = (data["doctor_id"], data["patient_name"], data["appointment_date"])
    cursor.execute(query, appointment_data)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    data = [{
        "doctor_id": 2,
        "patient_name": "Nisith", 
        "appointment_date": "2024-04-26"
    }]
    # insert_appointment_details(data[0])
    print(get_all_appointment_details())