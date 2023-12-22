from django.test import TestCase
from .calculator import Calculator

class CalculatorTestCase(TestCase):

    def test_valid_artithmetical_expressions(self):
        valid_expressions = [
            ("7+1", 8),("7++1", 8),("7+++1", 8),
            ("7-1", 6),("7--1", 8),("7---1", 6),
            ("7+-1", 6),("7+--1", 8),("7+---1", 6),
            ("7-+1", 6),("7--+1", 8),("7---+1", 6),
            ("7++-1", 6),("7++-1", 6),("7+++-1", 6),
            ("7*2", 14), ("7*+2", 14), ("7*-2", -14),
            ("7/2", 3.5), ("7/+2", 3.5), ("7/-2", -3.5),
        ]

        for expr, exp_res in valid_expressions:
            result = Calculator.calculate(expr)
            self.assertEqual(
                result,
                exp_res,
                f"Valid arithmetical expression '{expr}' did not produce expected result: '{exp_res}'."
            )

    def test_valid_expressions_with_dot(self):
        valid_expressions = [
            (". * 4", 0.0), ("0. * 4", 0.0), (".0 * 4", 0.0),
            ("3 * 1.", 3.0), ("3 * .5", 1.5), ("3 * 1.25", 3.75),
            ("6 + . - 1.", 5.0), ("6 - . + 1", 7.0), ("7 -- .", 7.0),
            ("6 / 1.5", 4.0), ("10 / .5", 20.0), ("30 / .1", 300.0)
        ]

        for expr, exp_res in valid_expressions:
            result = Calculator.calculate(expr)
            self.assertEqual(
                result,
                exp_res,
                f"Valid expression containing '.': '{expr}' did not produce expected result: '{exp_res}'."
            )


    def test_valid_expressions_with_brackets(self):
        valid_expressions = [
            ("2(5)", 10), ("2*(5)", 10), ("(5+2)(3+1)", 28),
            ("5(5(5) )", 125), ("5 * (5(5))", 125), ("5 * (5 * (5))", 125),
            ("6 / (5+1)", 1.0), ("(5+1) / 2", 3.0), ("7+2(5)", 17),
            ("(5/2.5)(4+3) --1", 15.0), ("5/(5(.5)) * 5", 10.0)
        ]

        for expr, exp_res in valid_expressions:
            result = Calculator.calculate(expr)
            self.assertEqual(
                result,
                exp_res,
                f"Valid expression containing brackets '()': '{expr}' did not produce expected result: '{exp_res}'."
            )


    def test_invalid_expressions(self):
        invalid_expressions = [
            ("7***6"), ("7///1"), ("7 + 0..1"),
            ("6(5))"), ("(9+5)5"), ("5*/2"), 
            ("4/*2"), ("(6 + 2"), ("(5+2).(10+1)"),
            ("7.7.1"), (".)+1"), ("/1"), ("*2"),
            ("()"), ("5()"), ("1.((8))")
        ]

        exp_res = "SYNTAX ERROR"

        for expr in invalid_expressions:
            result = Calculator.calculate(expr)
            self.assertEqual(
                result,
                exp_res,
                f"Invalid expression: '{expr}' did not produce expected result: '{exp_res}'."
            )


    

