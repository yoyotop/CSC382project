# Import necessary modules
import time  # For measuring time
import random  # For generating random numbers

# Function to perform insertion sort
def insertionSort(arr):
    """
    Sorts the given array using insertion sort algorithm.

    Parameters:
        arr (list): The input list to be sorted.

    Returns:
        list: Sorted list.
    """
    for i in range(1, len(arr)):
        key = arr[i]

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr

# Function to find the ith order statistic in an array
def orderStatistics(arr, i):
    """
    Finds the ith order statistic (ith smallest element) in the given array.

    Parameters:
        arr (list): The input list.
        i (int): The position of the desired order statistic.

    Returns:
        int: The ith order statistic.
    """
    # If the array size is small, use insertion sort
    if len(arr) <= 5:
        A = insertionSort(arr)
        return A[i]
    
    # Divide the array into groups of 5 and find medians of each group
    groupsOf5 = []
    j = 0
    while j < len(arr):
        groupsOf5.append(insertionSort(arr[j : j  + 5]))
        j += 5
    medians = []

    for group in groupsOf5:
        medians.append(group[len(group) // 2])
    
    # Find the median of medians recursively
    if len(medians) <= 5:
        pivot = medians[len(medians) // 2]
    else:
        pivot = orderStatistics(medians, len(medians) // 2)
    
    # Partition the array based on the pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    
    k = len(low)
    
    # Recursively search for the ith element
    if i < k:
        return orderStatistics(low, i)
    elif i < k + len(middle):
        return pivot
    else:
        return orderStatistics(high, i - k - len(middle))

# Function to run tests and record runtime
def runTests():
    """
    Runs tests to measure the runtime of orderStatistics function.

    Parameters:
        None

    Returns:
        None
    """
    runTimeArr = []
    # Define sample sizes and population sizes
    sampleSizeN = [100, 300, 500, 1000, 2000, 4000, 5000, 8000, 10000]
    populationSizeN = [100, 300, 500, 1000, 2000, 4000]
    
    # Loop over each sample size
    for n in range(len(sampleSizeN)):
        print("|=================================================================================|")
        # Loop over each population size
        for popN in range(len(populationSizeN)):
            print(f"For Sample Size: {sampleSizeN[n]} and Population Size: {populationSizeN[popN]}")
            # Generate a random array of integers within the specified population size
            theArray = [random.randint(1, populationSizeN[popN]) for x in range(sampleSizeN[n])]
            # Perform tests for each sample
            for ith in range(5):
                i = random.randint(0, sampleSizeN[n])
                print("Find ith number:", i + 1, "(th/rd) number")
                start = time.process_time()  # Start measuring time
                theIthNum = orderStatistics(theArray, i)
                end = time.process_time()  # End measuring time
                timeTook = end - start  # Calculate the runtime
                # Append runtime information to the array
                runTimeArr.append(f"{sampleSizeN[n]}, {populationSizeN[popN]}, {i + 1}, {round(timeTook, 4)}" )
    # Write runtime information to a CSV file
    with open("runTime.csv", "w") as file:
        for i in range(len(runTimeArr)):
            print(runTimeArr[i], file=file)

# Function to get average runtime for each test case
def getAverage():
    """
    Runs tests to get the average runtime of orderStatistics function.

    Parameters:
        None

    Returns:
        None
    """
    # Initialize an empty list to store runtime information
    runTimeArr = []
        
        # Define the sample sizes and population sizes for testing
    sampleSizeN = [100, 300, 500, 1000, 2000, 4000, 5000, 8000, 10000]
    populationSizeN = [100, 300, 500, 1000, 2000, 4000]
        
        # Loop over each sample size
    for n in range(len(sampleSizeN)):
        print("|=================================================================================|")
            
            # Loop over each population size
        for popN in range(len(populationSizeN)):
            print(f"For Sample Size: {sampleSizeN[n]} and Population Size: {populationSizeN[popN]}")
            
                # Generate a random array of integers within the specified population size
            theArray = [random.randint(1, populationSizeN[popN]) for x in range(sampleSizeN[n])]
                
                # Initialize a variable to store the total runtime for each sample
            totalRunTime = 0
                
                # Perform tests for each sample
            for ith in range(5):
                i = random.randint(0, sampleSizeN[n])
                print("Find ith number:", i + 1, "(th/rd) number")
                    
                    # Measure the start time of the test
                start = time.process_time()
                    
                    # Find the ith order statistic in the array
                theIthNum = orderStatistics(theArray, i)
                    
                    # Measure the end time of the test
                end = time.process_time()
                    
                    # Calculate the runtime of the test
                timeTook = end - start
                    
                    # Accumulate the total runtime
                totalRunTime += timeTook
                    
                    # Print the result and runtime of the test
                print("The", i + 1, "(th/rd) number is", theIthNum)
                print(f"RunTime =  {round(timeTook, 4)} Seconds")
            
                # Calculate the average runtime for the sample and append it to the runtime list
            runTimeArr.append(f"{sampleSizeN[n]}, {populationSizeN[popN]},{round(totalRunTime/5, 4)}" )
            print("|=================================================================================|")
        
        # Write the average runtime information to a CSV file
    with open("avgRunTime.csv", "w") as file:
        for i in range(len(runTimeArr)):
            print(runTimeArr[i], file=file)


if __name__ == "__main__":
    getAverage()