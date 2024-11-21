import json
import os

mock_groups_path = os.path.join(os.path.dirname(__file__), "../mock_data/groups.json")
mock_groups_path = os.path.abspath(mock_groups_path)

mock_teachers_path = os.path.join(os.path.dirname(__file__), "../mock_data/teachers.json")
mock_teachers_path = os.path.abspath(mock_teachers_path)


def find_group_by_id(faculty: int, group_num: int) -> dict | None:
    with open(mock_groups_path, 'r') as groups_file:
        groups = json.load(groups_file)

    result = list(
        filter(lambda group: faculty == group['faculty'] and group_num == group['group'], groups['mock_data']))

    if not result:
        return None

    return result[0]


def find_group_by_name(group_name: str) -> list | None:
    with open(mock_groups_path, 'r') as groups_file:
        groups = json.load(groups_file)

    result = list(filter(lambda group: group_name in group['name'], groups['mock_data']))

    if not result:
        return None

    return result


def find_teacher_by_name(teacher_name: str) -> list | None:
    with open(mock_teachers_path, 'r') as groups_file:
        teachers = json.load(groups_file)

    result = list(filter(lambda teacher: teacher_name in teacher['name'], teachers['mock_data']))

    if not result:
        return None

    return result


if __name__ == '__main__':
    data = find_group_by_id(
        faculty=125,
        group_num=40518
    )
    print(data)
