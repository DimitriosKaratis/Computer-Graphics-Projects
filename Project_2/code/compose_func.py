import numpy as np

def compose(mat1: np.ndarray, mat2: np.ndarray) -> np.ndarray:
    """
    Composes two 4×4 affine transformation matrices by multiplying them.
    
    Parameters:
        mat1 (np.ndarray): First 4×4 affine transformation matrix
        mat2 (np.ndarray): Second 4×4 affine transformation matrix
    
    Returns:
        np.ndarray: Combined 4×4 affine transformation matrix (mat1 @ mat2)
    
    Note:
        The multiplication order follows standard matrix multiplication rules.
        This means mat2 is applied FIRST, then mat1 (right-to-left composition).
    """
    # Verify input shapes
    if mat1.shape != (4, 4) or mat2.shape != (4, 4):
        raise ValueError("Both matrices must be 4×4 in order to have affine transformations.")
    
    # Matrix multiplication (using @ operator)
    return mat1 @ mat2




# # Example usage (comment or uncomment as needed)

# # Create a translation matrix
# translation = np.array([
#     [1, 0, 0, 2],
#     [0, 1, 0, 3],
#     [0, 0, 1, 5],
#     [0, 0, 0, 1]
# ])

# # Create a rotation matrix (90° around Z-axis)
# rotation = np.array([
#     [0, -1, 0, 0],
#     [1, 0, 0, 0],
#     [0, 0, 1, 0],
#     [0, 0, 0, 1]
# ])

# # Compose them (rotation will be applied first)
# combined = compose(translation, rotation)
# print(combined)