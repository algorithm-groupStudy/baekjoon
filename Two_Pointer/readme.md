# 투 포인터(Two Pointers) 기법 

- 개념
    - 1차원 배열에서 시작점과 끝점 혹은 왼쪽 포인터와 오른쪽 포인터를 조작하는 방식의 문제 풀이 전략 
    - 완전탐색으로 해결하면 시간 초과가 나는 문제에 사용 
    - 정렬된 배열에 사용하는 경우가 많다. 

- 투포인터 문제집: [문제집](https://www.acmicpc.net/problemset?sort=ac_desc&algo=80)

- 예제 코드: 특정 합을 가지는 부분 연속 수열의 개수 구하기

    ```python 
    nums = [1, 2, 3, 2, 5]
    n = 5   # 배열의 길이 
    m = 5   # 찾고자하는 부분합 
 
    count = 0
    total = 0
    end = 0
 
    for start in range(n):
        while total < m and end < n:
            total += nums[end]
            end += 1
        if total == m:
            count += 1
        total -= nums[start]
    
    print(count)
    ```
    - start, end 두 개의 포인터 사용, index 0부터 시작 
    - 현재 합이 구하고자 하는 합보다 작으면 end 포인터를 1 증가,
    - 구하고자 하는 합과 같으면 count를 증가,  
    - 구하고자 하는 합보다 크거나 같으면 start 포인터를 1 증가시킨다. 
    - 시간복잡도 O(N) 으로 브루트 포스 O(N^2)보다 효율적인 탐색을 할 수 있다. 

---


### cf. 슬라이딩 윈도우 
- 개념
    - 고정 사이즈의 윈도우가 이동하며 윈도우 내에 있는 데이터를 이용해 문제를 풀이 
    - 투 포인터는 왼쪽, 오른쪽 포인터가 자유롭게 움직이지만, 슬라이딩 윈도우는 두 포인터가 함께 움직인다. 또한 보통 좌측 혹은 우측 한 방향으로만 움직인다. 

- 이미지 <br>
    ![slidingwindow](https://velog.velcdn.com/images%2Fjminkyoung%2Fpost%2F2127e592-2897-4541-be9e-06f5b8315b72%2Fezgif.com-gif-maker.gif)
    - [이미지 출처](https://velog.io/@jminkyoung/AL-%ED%88%AC-%ED%8F%AC%EC%9D%B8%ED%84%B0-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%94%A9-%EC%9C%88%EB%8F%84%EC%9A%B0-JavaScript)

    