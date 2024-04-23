from app.mysql_connection import mysql_connection

def get_doctors_list():
    connection = mysql_connection()
    cursor = connection.cursor()
    query = "select doctor_id, doctor_name from doctors"
    doctors = []
    cursor.execute(query)
    for (doctor_id, doctor_name) in cursor:
        doctors.append({
            "doctor_id":doctor_id,
            "doctor_name":doctor_name
        })

    cursor.close()
    connection.close()
    return doctors

def get_doctor_details(doctor_id):
    connection = mysql_connection()
    cursor = connection.cursor()
    query = "select * from doctors where doctor_id = %s"
    doctor = []
    cursor.execute(query, doctor_id)
    for (doctor_id, doctor_name, address) in cursor:
        doctor.append({
            "doctor_id":doctor_id,
            "doctor_name":doctor_name,
            "address":address
        })
    
    cursor.close()
    connection.close()
    return doctor

if __name__ == "__main__":
    doctors = get_doctors_list()
    print(doctors)
    doctor = get_doctor_details(1)
    print(doctor)