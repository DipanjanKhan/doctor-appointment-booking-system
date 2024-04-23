from flask import Flask, jsonify, request
from mysql_connection import mysql_connection
import doctors_dao, schedules_dao, appointment_dao

app = Flask(__name__)

connection = mysql_connection()

@app.route("/api/doctors", methods=["GET"])
def get_doctors_list():
    doctors = doctors_dao.get_doctors_list()
    return jsonify(doctors)

@app.route("/api/doctors/<int:doctor_id>", methods=["GET"])
def get_doctor_details(doctor_id):
    doctor_details = doctors_dao.get_doctor_details(doctor_id)
    if doctor_details:
        return jsonify(doctor_details)
    else:
        return jsonify({"error": "Doctor not found"}), 404
    
@app.route("/api/doctors/<int:doctor_id>/availability", methods=["GET"])
def get_availiability(doctor_id):
    doctor_details = doctors_dao.get_doctor_details(doctor_id)
    availiability = schedules_dao.get_schedule(doctor_id)
    if doctor_details:
        availiability_details = {"doctor_name": doctor_details[0]["doctor_name"], "doctor_id": doctor_id, "availiability": availiability}
        return jsonify(availiability_details)
    else:
        return jsonify({"error": "Doctor not found"}), 404
    
@app.route("/api/appointments", methods=["GET"])
def show_all_appointments():
    appointment_details = appointment_dao.get_all_appointment_details()
    if appointment_details:
        return jsonify(appointment_details)
    else:
        return jsonify({"error": "No appointment found"})
    
@app.route("/api/appointments/<int:doctor_id>", methods=["GET"])
def show_all_appointments_doctor(doctor_id):
    appointment_details = appointment_dao.get_appointment_details_doctor(doctor_id)
    if appointment_details:
        return jsonify(appointment_details)
    else:
        return jsonify({"error": "No appointment found"})
    
@app.route("/api/appointments/<appointment_date>", methods=["GET"])
def show_all_appointments_date(appointment_date):
    appointment_details = appointment_dao.get_appointment_details_date(appointment_date)
    if appointment_details:
        return jsonify(appointment_details)
    else:
        return jsonify({"error": "No appointment found"})
    
@app.route("/api/appointments/book", methods=["POST"])
def appointment_book():
    data = request.json
    doctor_id = data["doctor_id"]
    appointment_date = data["appointment_date"]
    appointment_details = appointment_dao.get_appointment_details(doctor_id, appointment_date)
    appointment_slots_left = 9 - len(appointment_details)
    data["appointment_slots_left"] = appointment_slots_left
    if appointment_details != None and len(appointment_details)>=10:
        return jsonify({"message": "No appointment slots are avaliable"})
    else:
        appointment_dao.insert_appointment_details(data)
        return jsonify({"message": "Appointment booked successfully", "appointment_details": data})
    

if __name__ == "__main__":
    app.run(debug=True)