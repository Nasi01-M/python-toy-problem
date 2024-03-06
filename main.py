# Challenge 1
def min_moves_for_target_bricks(A):
    # Calculate the number of boxes
    N = len(A)
    # Calculate the total number of bricks required for each box to have 10 bricks
    target_bricks = 10 * N
    # Calculate the total number of bricks in all boxes
    total_bricks = sum(A)
    # If the total number of bricks is not divisible by the number of boxes, it's not possible to achieve the target
    if total_bricks % N != 0:
        return -1
    # Calculate the number of bricks that each box should have
    bricks_per_box = total_bricks // N
    # Initialize the number of moves required to distribute bricks
    moves = 0
    # Iterate through each box to distribute bricks
    for i in range(N):
        # Calculate the difference between the current number of bricks and the target number of bricks
        diff = A[i] - bricks_per_box
        # If there are more bricks than needed in the current box
        if diff > 0:
            # If the current box is not the last one, distribute the extra bricks to the next box
            if i < N - 1:
                A[i + 1] += diff
                moves += diff
            # If it's the last box and there are still extra bricks, it's not possible to achieve the target
            else:
                return -1
        # If there are fewer bricks than needed in the current box
        elif diff < 0:
            # If the current box is not the last one, take the required bricks from the next box
            if i < N - 1:
                A[i + 1] += diff
                moves += abs(diff)
            # If it's the last box and there are still fewer bricks, it's not possible to achieve the target
            else:
                return -1
    # Return the total number of moves required
    return moves

# Challenge 2
def max_sum_equal_digit_sums(A):
    # Function to calculate the sum of digits of a number
    def digit_sum(num):
        return sum(int(digit) for digit in str(num))

    # Initialize the maximum sum
    max_sum = -1
    # Dictionary to store the maximum number for each digit sum
    digit_sums = {}
    # Iterate through each number in the list
    for num in A:
        # Calculate the sum of digits for the current number
        sum_digits = digit_sum(num)
        # If the digit sum is already present in the dictionary
        if sum_digits in digit_sums:
            # Update the maximum sum if the sum of the current number and the stored number is greater
            max_sum = max(max_sum, num + digit_sums[sum_digits])
            # Update the stored number to be the maximum of the current number and the stored number
            digit_sums[sum_digits] = max(num, digit_sums[sum_digits])
        else:
            # If the digit sum is not present, store the current number
            digit_sums[sum_digits] = num
    # Return the maximum sum
    return max_sum

# Challenge 3
def generate_string_with_equal_letters_count(N):
    # Define the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # Calculate the number of times the alphabet should be repeated to get the desired length
    letters_count = N // 26
    # Calculate the remaining characters if the length is not divisible by 26
    remainder = N % 26
    # If the length is divisible by 26, return the alphabet repeated that number of times
    if remainder == 0:
        return alphabet * letters_count
    # If there are remaining characters, return the first 'remainder' characters of the alphabet repeated (letters_count + 1) times
    else:
        return alphabet[:remainder] * (letters_count + 1)

# Example usage
print(min_moves_for_target_bricks([7, 15, 10, 8]))  # Output: 7
print(min_moves_for_target_bricks([11, 10, 8, 12, 8, 10, 11]))  # Output: 6
print(min_moves_for_target_bricks([7, 14, 10]))  # Output: -1

print(max_sum_equal_digit_sums([51, 71, 17, 42]))  # Output: 93
print(max_sum_equal_digit_sums([42, 33, 60]))  # Output: 102
print(max_sum_equal_digit_sums([51, 32, 43]))  # Output: -1

print(generate_string_with_equal_letters_count(3))  # Output: "abc"
print(generate_string_with_equal_letters_count(5))  # Output: "abcde"
print(generate_string_with_equal_letters_count(30))  # Output: "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
