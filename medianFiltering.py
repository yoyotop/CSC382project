# Import necessary modules
import os  # Provides functions for interacting with the operating system
import glob  # For file pattern matching
import cv2 as cv  # OpenCV library for computer vision tasks
import numpy as np  # Library for numerical computations
from PIL import Image as img  # Python Imaging Library for working with images

# Import custom module for order statistics
import orderStatistic as orderStat  

# Define a function to extract an n x n subarray around a given pixel from a 2D array
def extract_nxn_subarray(arr, i, j, n):
    """
    Extracts an n x n subarray around a given pixel from a 2D array.

    Parameters:
        arr (numpy.ndarray): The input 2D array.
        i (int): Row index of the center pixel.
        j (int): Column index of the center pixel.
        n (int): Size of the subarray (n x n).

    Returns:
        numpy.ndarray: The extracted n x n subarray.
    """
    # Get the dimensions of the original array
    rows, cols = arr.shape
    
    # Calculate the half size to determine the range around the center
    half_n = n // 2
    
    # Calculate start and end indices for rows and columns
    start_row = max(0, i - half_n)
    end_row = min(rows, i + half_n + 1)
    start_col = max(0, j - half_n)
    end_col = min(cols, j + half_n + 1)
    
    # Extract the subarray
    sub_array = arr[start_row:end_row, start_col:end_col]
    
    # Pad the subarray if necessary to ensure it is n x n
    if sub_array.shape != (n, n):
        pad_before_row = max(0, half_n - i)
        pad_after_row = max(0, i + half_n + 1 - rows)
        pad_before_col = max(0, half_n - j)
        pad_after_col = max(0, j + half_n + 1 - cols)
        sub_array = np.pad(sub_array,
                           ((pad_before_row, pad_after_row),
                            (pad_before_col, pad_after_col)),
                           mode='constant', constant_values=0)
    return sub_array

# Define a function to filter images using order statistics
def filterImage():
    """
    Filters images using order statistics and saves the filtered results.

    Parameters:
        None

    Returns:
        None
    """
    # Define the path where images are stored
    path = "C:/Users/yoyot/Downloads/Project1/pics/*.*"
   
    # Get the size of the window for filtering from user input
    windowSize = int(input("What size window would you like to filter by: "))
    
    # Initialize image number
    imgNum = 0
    
    # Iterate over each image in the specified path
    for file in glob.glob(pathname=path):
        # Open the image file
        theImage = img.open(file)
        
        # Convert the image to a numpy array
        imgArr = np.array(theImage)
        
        # If the image has multiple channels, reshape it to a 2D array
        if len(imgArr.shape) >= 3:
            imgArr = imgArr.reshape(imgArr.shape[0], -1).T
        
        # Iterate over each pixel in the image
        for pixelRow in range(len(imgArr)):
            for pixelCol in range(len(imgArr[pixelRow])):
                # Extract the n x n box around the current pixel
                nByNBox = extract_nxn_subarray(imgArr, pixelRow, pixelCol, windowSize)
                # Use flatten method to turn 2D array into 1D array for filtering
                nByNBox = nByNBox.flatten()
                # Apply order statistics to the n x n box and assign the result to the current pixel
                imgArr[pixelRow, pixelCol] = orderStat.orderStatistics(nByNBox, len(nByNBox) // 2)
        
        # Convert the filtered array back to an image
        filteredImage = img.fromarray(imgArr)
        
        # Save the filtered image to a specific folder with a numbered filename
        filteredImage.save(f"C:/Users/yoyot/Downloads/Project1/filteredResults/{imgNum}.png")
        
        # Increment image number for the next image
        imgNum += 1

# Entry point of the program
if __name__ == "__main__":
    filterImage()
