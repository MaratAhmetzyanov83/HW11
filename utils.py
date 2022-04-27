import json  # подключили библиотеку для работы с json
from pprint import pprint


def load_candidates_from_json(path):
    # возвращает список всех кандидатов
    with open(path, "r", encoding="utf-8") as f:  # открыли файл с данными
        return json.load(f)  # загнали все, что получилось в переменную


def get_candidate(candidate_id):
    # возвращает одного кандидата по его id
    candidates = load_candidates_from_json("candidates.json")
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate
    return None


def get_candidates_by_name(candidate_name):
    # возвращает кандидатов по имени
    candidates = load_candidates_from_json("candidates.json")
    matches = []
    for candidate in candidates:
        if candidate_name.lower() in candidate["name"].lower():
            matches.append(candidate)
    return matches


def get_candidates_by_skill(skill_name):
    # возвращает кандидатов по навыку
    candidates = load_candidates_from_json("candidates.json")
    matches = []
    for candidate in candidates:
        if skill_name.lower() in candidate["skills"].lower().split(", "):
            matches.append(candidate)
    return matches

