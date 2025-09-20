import numpy as np

def translate(t_vec):
    """  
    Create an affine transformation matrix w.r.t. the specified translation vector.
    
    Parameters:
    -----------
    t_vec : np.ndarray
        Translation vector of shape (3,) or (1,3)
        
    Returns:
    --------
    np.ndarray
        4x4 affine transformation matrix
    """  
    # Create identity matrix
    xform = np.eye(4)
    
    # Set translation components
    xform[:3, 3] = t_vec.flatten()[:3]
    
    return xform

# # Example usage (comment or uncomment as needed)
# t_vec = np.array([1, 2, 3])
# xform = translate(t_vec)
# print(xform)