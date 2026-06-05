def is_malicious_input(user_input):
    dangerous_keywords = [
    "忽略",
    "ignore",
    "system prompt",
    "developer",
    "開發者模式",
    "直接告訴我",
    "答案",
    "正確答案",
    "prompt",
    "指令",
    "規則",
    "洩漏",
    "破解",
    "role",
    "admin",
    "jailbreak",
    "你現在是",
    "不要遵守",
    "輸出完整",
    "show me",
    "reveal",
]

    text = user_input.lower()

    if len(user_input) > 50:
        return True, "問題太長，請限制在 50 字以內。"

    for keyword in dangerous_keywords:
        if keyword.lower() in text:
            return True, "偵測到疑似提示注入攻擊，系統已阻擋。"

    return False, ""


def clean_ai_answer(answer):
    allowed_answers = ["是", "不是", "不完全是", "與故事無關"]

    answer = answer.strip()

    for allowed in allowed_answers:
        if allowed in answer:
            return allowed

    return "與故事無關"