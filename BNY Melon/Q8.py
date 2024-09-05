def minimize_string_changes(s):
    # Define a helper function to update the DP table
    def update_minimum(cost_list, index, new_cost):
        if new_cost >= 0 and (cost_list[index] < 0 or cost_list[index] > new_cost):
            cost_list[index] = new_cost

    # Initialize DP table for 26 lowercase letters ('a' to 'z')
    dp = [[-1] * 2 for _ in range(26)]  # dp[char][good_or_bad]
    
    # Initialize the first character's DP state
    first_char = ord(s[0]) - ord('a')  # Convert character to an index (0 for 'a', 25 for 'z')
    for char in range(26):
        dp[char][0] = abs(char - first_char)  # Cost to make the first character a specific char
    
    # Process each subsequent character in the string
    for i in range(1, len(s)):
        current_char = ord(s[i]) - ord('a')  # Convert current character to its index
        new_dp = [[-1] * 2 for _ in range(26)]  # Temporary DP table to store new results

        # Iterate over each character (from 'a' to 'z') and two states (good or not)
        for prev_char in range(26):
            for is_good in range(2):
                # If the previous state is invalid, skip
                if dp[prev_char][is_good] < 0:
                    continue
                
                # Case 1: Continue the "good" group by keeping the character the same
                update_minimum(new_dp[prev_char], 1, dp[prev_char][is_good] + abs(current_char - prev_char))
                
                # Case 2: Start a new "good" group by changing the character
                if is_good == 1:
                    for new_char in range(26):
                        if new_char != prev_char:
                            update_minimum(new_dp[new_char], 0, dp[prev_char][is_good] + abs(current_char - new_char))
        
        dp = new_dp  # Update DP table with new values

    # Find the minimum cost from the DP table
    result = -1
    for char in range(26):
        update_minimum([result], 0, dp[char][1])  # Look for the minimum in the "good" state

    return result

# Example usage
if __name__ == '__main__':
    print(minimize_string_changes("aca"))  # Output: 2
    print(minimize_string_changes("abab"))  # Output: 3
