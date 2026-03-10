# import numpy as np



# # def matrix_multi(A,B):
# #     m,n =A.shape
# #     a,b =B.shape
# #     if n != a :
# #         raise ValueError("colums and rows of matrix are not matching")
    
# #     C=np.zeros((m,b))

# #     for i in range(m):
# #         for  j in range (b):
# #             for k in range (a):
# #                 C[i,j] += A[i,k]*B[k,j]
# #     return C

# # A=np.array([[1,2,3],[4,5,6]])
# # B=np.array([[7,8,9],[10,11,12],[13,14,15]])

# # result=matrix_multi(A,B)
# # print(result)

# # dot =np.dot(A,B)
# # print(dot)


# #Linear_Transformation 

# # matrix=np.array([[2,0],
# #                  [0,1]],dtype=int)
# # vect =np.array([2,1],dtype=int)
# # y= np.zeros([2],dtype=int)
# # print(y)

# # # trans = matrix @ vect
# # q,w = matrix.shape
# # for i in range(q):
# #     for j in range(w):
# #         y[i] += matrix[i,j]*vect[j]

# # print(y)
# #         


# # res = vect * matrix
# # print(res)

# # print("before transformation", vect)
# # print("After",trans)

# #3d tranformers


# # vect1=np.array([1,0,0])
# # vect2=np.array([0,1,0])
# # vect3=np.array([0,0,1])


# # v= np.array([2,3,1])

# # trans=np.array([[1,1,0],
# #                 [0,1,0],
# #                 [0,0,1]])
# # # print(trans.shape)
# # a,b = trans.shape
# # c=np.zeros(3,dtype=int)
# # # print(c)
# # res=trans @ v

# # for i in range (a):
# #     for j in range(b):
# #         c[i] += trans[i,j] * v[j]

# # print(c)
# # print('result :',np.allclose(c,res))
# # print(res)

# #determinat

# # a=np.array([[1,2],
# #             [2,3]])
# # deter =np.linalg.det(a)
# # print(deter)

# # b=np.array([[1,0],[0,1]])
# # print(np.linalg.det(b))

# # import numpy as np

# # # 3 features for 5 students
# # data = np.array([[80, 70, 90],
# #                  [60, 65, 70],
# #                  [90, 85, 95],
# #                  [50, 55, 60],
# #                  [75, 70, 80]])

# # # Covariance matrix
# # cov_matrix = np.cov(data.T)
# # print(cov_matrix)









# # Vector
# # What: List of numbers representing data
# # Why: Represent any data as numbers
# # Where: Images, text, audio — all vectors
# # Dot Product
# # What: Multiplies pairs then adds up
# # Why: Measure similarity between two things
# # Where: RAG finding relevant documents
# # Matrix Multiply
# # What: Transforms input into new representation
# # Why: Learn which features matter most
# # Where: Every neural network layer
# # Linear Transformation
# # What: Stretch, compress, rotate, crush
# # Why: Change data into meaningful representation
# # Where: Each layer in deep learning
# # Transpose
# # What: Flip rows and columns
# # Why: Make matrix shapes compatible
# # Where: Attention mechanism in Transformers
# # Determinant
# # What: Measures area/volume
# # Why: Detect if information is lost
# # Where: Checking multicollinearity in features
# # Eigenvalues
# # What: How much a vector stretches
# # Why: Find directions of maximum variance
# # Where: PCA dimensionality reduction
# # Eigenvectors
# # What: Special vectors that never rotate
# # Why: Find principal components of data
# # Where: PCA — reduce 100 features to 2
# # Identity Matrix
# # What: Changes nothing
# # Why: Starting point, testing, debugging
# # Where: Weight initialization
# # Non Square Matrix
# # What: Different rows and columns
# # Why: Transform between different dimensions
# # Where: Neural network layers (4 inputs → 2 outputs)

# # DOT PRODUCT — 3 CASES
# # High positive → Very similar → Query matches document in RAG
# # Zero → Nothing in common → Document not relevant to query
# # Negative → Opposite → Document contradicts query

# # LINEAR TRANSFORMATION — 4 THINGS
# # Expand → [[2,0],[0,2]] → Vector bigger → Amplifying features
# # Compress → [[0.5,0],[0,0.5]] → Vector smaller → Dimensionality reduction
# # Rotate → [[0,-1],[1,0]] → Direction changes → Finding new feature directions
# # Crush → [[1,2],[2,4]] → Flattened (det=0) → Bad — information lost


# # DETERMINANT — 3 CASES
# # Greater than 1 → Area stretched → Features amplified
# # Equal to 1 → Area unchanged → Perfect preservation
# # Equal to 0 → Area destroyed → Multicollinearity — breaks model

# # COVARIANCE

# # What:
# # Measures how two features move together

# # 3 cases:
# # Positive → move together   → may be redundant features
# # Negative → move opposite   → inversely related features
# # Zero     → no movement     → completely independent

# # Difference from Correlation:
# # Covariance → direction only → any number
# # Correlation → direction + strength → always -1 to +1

# # Where in ML:
# # PCA → covariance matrix → find related features
# # Feature selection → remove redundant features
# # Anomaly detection → multivariate Gaussian

