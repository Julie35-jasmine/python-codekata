# 최댓값 만들기(1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120847
# 알고리즘: 기초
# 작성자: 이주은
# 작성일: 2026. 01. 22. 11:22:21

def solution(numbers):
    numbers.sort(reverse=True)
    answer = int(numbers[0]) * int(numbers[1])
    return answer