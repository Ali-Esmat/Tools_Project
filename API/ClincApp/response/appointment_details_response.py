class AppointmentDetailsResponse:

    def __init__(self,doctor_name, appointment_date):
        self.doctor_name = doctor_name
        self.appointment_date = appointment_date

    def set_doctor_name(self,doctor_name):
        self.doctor_name = doctor_name

    def set_appointment_date(self, appointment_date):
        self.appointment_date = appointment_date