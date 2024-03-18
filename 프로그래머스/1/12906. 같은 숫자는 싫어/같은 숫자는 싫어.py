def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    answer.append(arr[0])
    for v in arr[1:]:
        if v != answer[-1]:
            answer.append(v)
    
    return answer