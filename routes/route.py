from fastapi import APIRouter
from models.staffdetails import Staff
from config.database import collection_name
from schema.schemas import list_staff
from bson import ObjectId

router = APIRouter()

@router.get("/get-staffs")
async def get_staffs():
    staffs = list_staff(collection_name.find())
    return staffs

@router.post("/add-staff")
async def add_staff(staff:Staff):
    collection_name.insert_one(dict(staff))

# @router.put("update_staff_details/{id}")
# async def update(id:str,staff:Staff):
#     collection_name.update_one({"_id": ObjectId(id)}, {"$set": dict(staff)})
@router.put("/update_staff_details/{staff_id}")
def update_staff(staff_id: str, updated_staff: Staff):
    query = {"_id": ObjectId(staff_id)}
    new_values = {"$set": dict(updated_staff)}
    collection_name.update_one(query, new_values)
    return {"message": "Staff updated successfully"}

@router.delete("/delete_staff/{id}")
def delete_staff(id:str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})


