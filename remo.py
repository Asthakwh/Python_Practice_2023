    import numpy as np

    arr1 = np.array([10, 20, 30])
    arr2 = np.array([[1, 1], [2, 2]])

    # Save multiple arrays to a .npz file
    np.savez('multiple_arrays.npz', array1=arr1, array2=arr2)

    # Load arrays from the .npz file
    data = np.load('multiple_arrays.npz')
    print(data['array1'])
    print(data['array2'])