def individual_staff(staff) -> dict:
    return {
        "id" : str(staff["_id"]),
        "name": staff["name"],
        "age" : (staff["age"]),
        "staffID" : staff["staffID"],
        "email" : staff["email"],
        "gender"  : staff["gender"]
    }

def list_staff(staffs) -> list:
    return [individual_staff(staff) for staff in staffs]