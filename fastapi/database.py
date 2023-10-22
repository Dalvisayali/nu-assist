from typing import List, Union

from beanie import PydanticObjectId

from models.User import User
from models.Report import Report

admin_collection = User
report_collection = Report


async def add_admin(new_admin: User) -> User:
    admin = await new_admin.create()
    return admin


async def retrieve_reports() -> List[Report]:
    students = await report_collection.all().to_list()
    return students


async def add_report(new_student: Report) -> Report:
    student = await new_student.create()
    return student


async def retrieve_report(id: PydanticObjectId) -> Report:
    student = await report_collection.get(id)
    if student:
        return student


