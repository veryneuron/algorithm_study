# 최대공약수, 최소공배수?
# 사람이 구할 때? 직관적으로 공통의 약수 찾고 약수 전부 곱하면 최대공약수, 나머지 다곱하면 최소공배수
# 알고리즘? 유클리드 호제법 사용
# N, M에서 N = M*q + r일때 gcd가 b, r의 gcd와 같고, r=0일때는 b가 gcd임
# 즉 N % M 해서 r구하고 아니면 N, M을 b, r로 바꾼뒤 그다음 r=0될때까지 계속 반복
# 최소공배수는 N*M // 최대공약수


N, M = map(int, input().split())

N_ori, M_ori = N, M
result = 1

if M > N:
    M, N = M, N

while(True):
    R = N % M
    if R == 0:
        result = M
        break
    else:
        N, M = M, R

print(result, N_ori*M_ori//result, sep='\n')