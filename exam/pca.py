from sklearn.decomposition import PCA
import numpy as np
import pandas as pd

points = []
with open('datalof.txt','r') as file:
    lines = file.readlines()

for line in lines:
    points.append((int(line.split(",")[0]),int(line.split(",")[1])))

model = PCA(n_components=len(points))
X = np.array(points)
result = model.fit_transform(X)

print(result)

# dims = X.T #converting row to columns

# covariance = np.cov(dims)
# eigVal,eigVec = np.linalg.eig(covariance) #calculating covariance and eigenvalues, eigenvectors

# first_proj = X.dot(eigVec.T[0]) #transpose required for more than 1 entries of the vector
# data_pca = pd.DataFrame(first_proj,columns=['projected']) #creating projections of our data

# print(data_pca)