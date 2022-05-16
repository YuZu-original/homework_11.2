import json


def load_candidates_from_json(path):
    """возвращает список всех кандидатов"""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def get_candidate_by_id(candidate_id, data):
    """возвращает одного кандидата по его id"""
    for cand in data:
        if cand["id"] == candidate_id:
            return cand

def get_candidates_by_name(candidate_name:str, data):
    """возвращает кандидатов по имени"""
    candidate_name = candidate_name.strip().lower()
    return [cand for cand in data if candidate_name in cand["name"].lower()]

def get_candidates_by_skill(skill_name, data):
    """возвращает кандидатов по навыку"""
    skill_name = skill_name.strip().lower()
    return [cand for cand in data if skill_name in cand["skills"].strip().lower().split(", ")]
