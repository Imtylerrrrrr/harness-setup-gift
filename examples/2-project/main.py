"""단어장 퀴즈 — 아주 작은 예제 프로젝트.

이 프로젝트의 주인공은 코드가 아니라 .claude/ 폴더입니다.
프로젝트별 세팅(.claude/CLAUDE.md, 스킬, .mcp.json)이 어떻게 생겼는지 보여주기 위한 예제입니다.

실행: python main.py
"""
import random

from words import WORD_SETS


def choose_set():
    """세트 목록을 보여주고 하나를 고르게 한다."""
    names = list(WORD_SETS)
    print("=== 단어장 퀴즈 ===")
    for i, name in enumerate(names, 1):
        print(f"  {i}. {name} ({len(WORD_SETS[name])}단어)")
    while True:
        raw = input("풀어볼 세트 번호: ").strip()
        if raw.isdigit() and 1 <= int(raw) <= len(names):
            return names[int(raw) - 1]
        print("목록에 있는 번호를 입력해 주세요.")


def run_quiz(set_name, count=5):
    """세트에서 최대 count개를 뽑아 퀴즈를 낸다."""
    words = WORD_SETS[set_name]
    picked = random.sample(list(words.items()), min(count, len(words)))
    score = 0
    for i, (question, answer) in enumerate(picked, 1):
        guess = input(f"[{i}/{len(picked)}] {question} = ").strip()
        if guess.lower() == answer.lower():
            print("  정답!")
            score += 1
        else:
            print(f"  아쉽다. 정답은 '{answer}'")
    print(f"\n결과: {len(picked)}문제 중 {score}개 정답")


if __name__ == "__main__":
    run_quiz(choose_set())
