import numpy as np
print ("Hello,Numpy!")
arr=np.array([10,20,30,40,50])
print("Array",arr)
print("shape",arr.shape)

arr_1d=np.array([10,20,30,40,50])
print("\n1D Array:")
print(arr_1d)
print("Shape:",arr_1d.shape)

arr_2d=np.array([
    [1,2,3],
    [4,5,6]
])
print("\n2D Array:")
print(arr_2d)
print("Shape:",arr_2d.shape)

arr_3d=np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])
print("\n3D Array:")
print(arr_3d)
print("Shape:",arr_3d.shape)

numbers=np.array([10,20,30,40,50])
broadcast_result=numbers+5
print("\nBroadcasting:")
print("original:",numbers)
print("After adding 5:",broadcast_result)

#VECTORISED OPER
values =np.array([1,2,3,4,5])

squared=values**2
doubled=values*2

print("\nVectorised operations:")
print("original:",values)
print("squared:",squared)
print("Doubled:",doubled)

#MATRIX MULTI
A=np.array([
    [1,2],
    [3,4]
])
B=np.array([
    [5,6],
    [7,8]
])

matrix_result=A@B
print("\nMatrix Multiplication:")
print(matrix_result)

#READ CSV DATASET
data=np.genfromtxt(
    "student_scores.csv",
    delimiter=",",
    skip_header=1,
)
data =data[~np.isnan(data).any(axis=1)]

hours= data[:, 0]
marks= data[:, 1]


print("\nCSV Dataset:")
print(data) 

#CALCULATE MEAN
mean_hours=np.mean(hours)
mean_marks=np.mean(marks)

print("\nMean:")
print("Average Hours Studied:",mean_hours)
print("Average Marks:",mean_marks)

#STD(Calculate standard deviation)
std_hours=np.std(hours)
std_marks=np.std(marks)

print("\nStandards Deviation:")
print("std Hours Studied:",std_hours)
print("std Marks:",std_marks)

#CORRELATION
correlation =np.corrcoef(hours,marks)[0,1]

print("\ncorrelation:")
print("Hours vs marks:",correlation)

