import re

class Calculator:
    """
    A simple calculator class for evaluating mathematical expressions.

    Methods:
    - calculate(expression): Evaluates the given mathematical expression.
    """

    @classmethod
    def calculate(cls,expression):
        """
        Evaluates the given mathematical expression.

        Args:
        - expression (str): The mathematical expression to be evaluated.

        Returns:
        - float or str: The result of the evaluation if successful, otherwise returns "SYNTAX ERROR".

        Notes:
        - This method uses the eval function to compute the result.
        - If the expression cannot be evaluated properly due to syntax errors, it returns "SYNTAX ERROR".
        """

        try:
            expression = cls.__resolver(expression)
            result = eval(expression)

            if not isinstance(result, (int, float, complex,)):
                raise Exception()
            else:
                return result
        except:
            return "SYNTAX ERROR"
        

    @classmethod
    def __resolver(cls,expression: str):
        """
        Responsible for resolving and refining mathematical expressions for accurate calculation.

        Args:
        - expression (str): The mathematical expression to be refined.

        Returns:
        - str: The refined expression after applying necessary adjustments.
        """
        try:
            expression = cls.__resolve_dots(expression)
            expression = cls.__resolve_opening_bracket(expression)
            return expression

        except Exception as e:
            print("ERROR occurred in resolver: ", e)


    @classmethod
    def __resolve_dots(cls, expression):
        """
        Replaces dots not preceded or followed by a digit with '0.' in the given expression.

        Args:
        - expression (str): The mathematical expression.

        Returns:
        - str: The modified expression with dots resolved.
        """
        try:
            expression = re.sub(r'(?<!\d)\.(?![0-9])', '0.', expression)
            return expression
        
        except Exception as e:
            print("ERROR occurred while resolving dots: ", e)


    @classmethod
    def __resolve_opening_bracket(cls, expression: str):
        """
        Replaces opening brackets '(' preceded by a digit or ')' with '*(' in the given expression.

        Args:
        - expression (str): The mathematical expression.

        Returns:
        - str: The modified expression with opening brackets resolved.
        """
        try:
            def repl(match):
                return '*('

            pattern = r'(?<=[0-9\)])\('
            cleaned_value = re.sub(pattern, repl, expression)
            return cleaned_value

        except Exception as e:
            print("ERROR occurred in resolver: ", e)


        

        
