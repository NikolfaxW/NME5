import numpy as np

def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    x = np.array([-4, -1, 2])
    y = np.array([-28, -16, -40])
    n = x.shape[0] - 1
    x_0 = -0.5
    matrix = np.zeros((n + 1,n + 1))
    for i in range(n + 1):
        matrix[i,i] = y[i]

    for k in range(1,n + 1):
        for it in range(n + 1 - k):
            i = it
            j = k + it
            matrix[i,j] = ((x_0 - x[i]) * matrix[i+1, j] - (x_0 - x[j])*matrix[i,j-1])/(x[i] - x[j])


    print("The result got by Neville's algorithm for polynomial interpolation is ", matrix[0, n])
    if np.allclose(matrix[0, n], -17.5):
        print(
            "The result \033[92mIS CLOSE\033[0m to expected result \033[92m-17.5\033[0m")
    else:
        print(
            "The result \033[91mIS NOT CLOSE\033[0m to expected result \033[92m-17.5\033[0m")