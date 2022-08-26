class Matrix_calculation:

# 매트릭스 곱셈
  def matMulti(A, B):
    answer = [len(B[0]) * [0] for i in range(len(A))]
    if len(A[0]) == len(B):
        for i in range(0, len(A)):
            for j in range(0,len(B[0])):
                for k in range(0, len(A[0])):
                    answer[i][j] += A[i][k]*B[k][j]
        return answer

# 매트릭스 덧셈
  def matAdd(A,B):
    answer = [[0 for j in range(len(A[0]))] for i in range(len(A))]
    if(len(A)==len(B)) and (len(A[0])==len(B[0])):
      for i in range(0, len(A)):
        for j in range(0,len(A[0])):
          answer[i][j] = A[i][j]+B[i][j]
    return answer  

 # 매트릭스 곱셈 
  def matSub(A,B):
    answer = [[0 for j in range(len(A[0]))] for i in range(len(A))]
    if(len(A)==len(B)) and (len(A[0])==len(B[0])):
      for i in range(0, len(A)):
        for j in range(0,len(A[0])):
          answer[i][j] = A[i][j]-B[i][j]
    return answer