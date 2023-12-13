# File: calibrations_processor.py

def process_calibrations(calibrations_file):
    """
    Process calibration data from the given file.

    Args:
        calibrations_file (str): The path to the calibration file.

    Returns:
        int: The total sum of processed calibration numbers.
    """
    expected_result = []

    with open(calibrations_file, "r") as file:
        lines = file.readlines()

        for line in lines:
            numbers = ''.join(char for char in line if char.isdigit())

            if len(numbers) == 1:
                expected_result.append(int(numbers[0] * 2))
            elif len(numbers) >= 2:
                expected_result.append(int(''.join(numbers[::len(numbers) - 1])))
            else:
                print("Error processing line:", repr(line))

    total_sum = sum(expected_result)
    return total_sum

if __name__ == "__main__":
    calibrations_file = "calibrations.txt"
    total_sum = process_calibrations(calibrations_file)
    print("Total Sum:", total_sum)

    
 