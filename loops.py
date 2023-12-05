class loops:
    @staticmethod
    def factorial(n: int):
        """Computes the factorial of a specified number

        Args:
            n (int): specified number; for example, 6

        Returns:
            int: computed factorial
        """        
        # the counter variable i more or less contains the
        # same value as the parameter n

        # the loop will repeat as long as i > 1
        # the condition that will cause the loop to stop 
        # is when i == 1 -> stopping case for the loop

        # with each iteration of the loop, we're decrementing 
        # the counter variable by 1
        i = n - 1 
        while(i > 1):
            n = n * i
            # n = 6 * 5
            # n = 30 * 4
            # n = 120 * 3 
            # n = 360 * 2
            i = i - 1

        return n
    
    @staticmethod
    def power(number: int, power: int):
        """Takes a specified number to a specified power

        Args:
            number (int): specified number; for example, 2
            power (int): specified power; for example, 5

        Returns:
            int: computed power
        """        
        # the counter variable for the loop contains the 
        # same value as power

        # the loop will repeat as long as i > 1
        # the condition that will cause the loop to stop 
        # is when i == 1 -> stopping case for the loop

        # with each iteration of the loop, we're decrementing 
        # the counter variable by 1
        result = 1

        i = power
        while (i > 0):
            result = result * number
            # result = 1 * 2 : i = 5
            # result = 2 * 2 : i = 4
            # result = 4 * 2 : i = 3
            # result = 8 * 2 : i = 2
            # result = 16 * 2 : i = 1
            i = i - 1

        return result