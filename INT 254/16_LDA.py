import numpy as np

class LDA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.eigenvectors = None

    def fit(self, X, y):
        # Calculate class means
        class_means = []
        for c in np.unique(y):
            class_means.append(np.mean(X[y == c], axis=0))

        # Calculate within-class scatter matrix
        within_scatter_matrix = np.zeros((X.shape[1], X.shape[1]))
        for c, mean in zip(np.unique(y), class_means):
            class_scatter = np.cov(X[y == c], rowvar=False)
            within_scatter_matrix += class_scatter

        # Calculate between-class scatter matrix
        overall_mean = np.mean(X, axis=0)
        between_scatter_matrix = np.zeros((X.shape[1], X.shape[1]))
        for c, mean in zip(np.unique(y), class_means):
            n = X[y == c].shape[0]
            mean_diff = (mean - overall_mean).reshape(-1, 1)
            between_scatter_matrix += n * mean_diff.dot(mean_diff.T)

        # Solve eigenvalue problem
        eigenvalues, eigenvectors = np.linalg.eig(np.linalg.inv(within_scatter_matrix).dot(between_scatter_matrix))

        # Select top k eigenvectors
        idx = eigenvalues.argsort()[::-1]
        self.eigenvectors = eigenvectors[:, idx[:self.n_components]]

    def transform(self, X):
        return np.dot(X, self.eigenvectors)

# Example usage
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([0, 0, 1, 1])

lda = LDA(n_components=1)
lda.fit(X, y)
X_lda = lda.transform(X)

print(X_lda)