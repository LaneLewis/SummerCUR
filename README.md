In this summer project, we built a novel deterministic CUR decomposition algorithm (Subspace)and compared it against a slightly modified version of the current non-deterministic method for performing the docomposition.

To test our decomposition, Subspace, on a dataset run:
```
dataframe = some df that is m×n..
top_k_singular_vectors = some number less than min(m,n)..
hyperparameter = some number less than n..
C,U,R,distances = subspace_cur(dataframe, top_k_singular_vectors_to_use, hyperparameter)
```
To test a slighly modified version of the exactly algorithm (called Leverage) from Drineas Petros, Michael W. Mahoney, and Shan Muthukrishnan's paper ”Relative-error CUR matrix decompositions” that we compare our algorithm to run:
```
dataframe = some df that is m×n..
top_k_singular_vectors = some number less than min(m,n)..
hyperparameter = some number
C,U,R,distances = leverage_cur(dataframe, top_k_singular_vectors_to_use, hyperparameter)
```
