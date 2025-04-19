class DynamicProgramming:
    @staticmethod
    def fibonacci(n):
        """
        Calculate nth Fibonacci number using dynamic programming.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not isinstance(n, int) or n < 0:
            raise ValueError("Input must be a non-negative integer")
        if n <= 1:
            return n
        prev, curr = 0, 1
        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr
        return curr

    @staticmethod
    def knapsack(values, weights, capacity):
        """
        Solve the 0/1 Knapsack problem.

        Time Complexity: O(n * capacity)
        Space Complexity: O(n * capacity)
        """
        if len(values) != len(weights):
            raise ValueError("Values and weights must be of the same length")

        n = len(values)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(capacity + 1):
                if weights[i - 1] <= w:
                    dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
                else:
                    dp[i][w] = dp[i - 1][w]

        return dp[n][capacity]

    @staticmethod
    def longest_common_subsequence(str1, str2):
        """
        Find length of the Longest Common Subsequence (LCS).

        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]

    @staticmethod
    def matrix_chain_multiplication(p):
        """
        Compute minimum scalar multiplications for matrix chain.

        Time Complexity: O(n^3)
        Space Complexity: O(n^2)
        """
        if len(p) < 2:
            raise ValueError("Invalid dimensions array")

        n = len(p) - 1
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                for k in range(i, j):
                    cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                    dp[i][j] = min(dp[i][j], cost)

        return dp[0][n - 1]

    @staticmethod
    def coin_change(coins, amount):
        """
        Find minimum number of coins to make amount.

        Time Complexity: O(amount * len(coins))
        Space Complexity: O(amount)
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[amount] == float('inf') else dp[amount]


# Interactive user prompts with loop
if __name__ == "__main__":
    while True:
        print("\nSelect a Dynamic Programming Problem to Solve:")
        print("1. Fibonacci")
        print("2. 0/1 Knapsack")
        print("3. Longest Common Subsequence")
        print("4. Matrix Chain Multiplication")
        print("5. Coin Change Problem")
        print("6. Exit")

        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            n = int(input("Enter n for Fibonacci(n): "))
            print("Fibonacci(", n, ") =", DynamicProgramming.fibonacci(n))

        elif choice == 2:
            values = list(map(int, input("Enter values separated by space: ").split()))
            weights = list(map(int, input("Enter weights separated by space: ").split()))
            capacity = int(input("Enter knapsack capacity: "))
            print("Maximum value:", DynamicProgramming.knapsack(values, weights, capacity))

        elif choice == 3:
            str1 = input("Enter first string: ")
            str2 = input("Enter second string: ")
            print("Length of LCS:", DynamicProgramming.longest_common_subsequence(str1, str2))

        elif choice == 4:
            dimensions = list(map(int, input("Enter matrix dimensions (e.g., 40 20 30 10 30): ").split()))
            print("Minimum multiplication cost:", DynamicProgramming.matrix_chain_multiplication(dimensions))

        elif choice == 5:
            coins = list(map(int, input("Enter coin denominations: ").split()))
            amount = int(input("Enter amount: "))
            print("Minimum coins required:", DynamicProgramming.coin_change(coins, amount))

        elif choice == 6:
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")
