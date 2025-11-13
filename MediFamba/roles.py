from rolepermissions.roles import AbstractUserRole


class Doctor(AbstractUserRole):
    available_permissions = {'view_appointments':True,'create_appointments':True}


class Patient(AbstractUserRole):
    available_permissions = {'view_doctors':True,'view_agenda':True}


class User(AbstractUserRole):
    available_permissions = {'view_info':True}