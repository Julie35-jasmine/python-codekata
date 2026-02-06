# 머쓱이보다 키 큰 사람
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120585
# 알고리즘: 기초
# 작성자: 이주은
# 작성일: 2026. 02. 06. 09:50:27

def solution(array, height):
    high = 0
    for i in range(len(array)):
        if int(array[i]) > height:
            high += 1
    return high