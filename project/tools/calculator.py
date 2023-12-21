import re

class Calculator:
    
    def __init__(self, calculation: str):
        self.value = calculation
        self.__bracket_pairs = []
        self.__num_indexes = len(calculation) - 1 if calculation else 0

    def __str__(self):
        return self.value
    
    def __repr__(self):
        return f"Calculator(calculation = '{self.value}')"

    def __validate(self):
        valid = False
        if self.__validate_bracket_pairs():
            if self.__validate_format():
                valid = True

        return valid

    def __validate_bracket_pairs(self):
        try:
            if not ( self.value.count("(") == self.value.count(")") ):
                return False
            else:
                stack = []
                for ind, char in enumerate(self.value):
                    if char == "(":
                        stack.append(ind)

                    elif char == ")":
                        if stack:
                            open_ind = stack.pop()
                            self.__bracket_pairs.append( (open_ind, ind) )
                        else:
                            raise Exception(f"Closing bracket at index {ind} has no opening bracket...")
                
                self.__bracket_pairs = sorted(self.__bracket_pairs, key=lambda pair: pair[0])
                return True
            

        except Exception as e:
            print("ERROR occurred while validating bracket pairs: ", e)
            return False
                
    def __validate_format(self):
        valid = True
        try:
            if self.__num_indexes < 0:
                return valid
            else:
                operators = ["+", "-", "x", "/"]
                illegal_preceedings = ["x", "/", ")"]

                for ind, char in enumerate(self.value):
                    # first char check
                    if ind == 0:
                        if char in ["x", "/", ")"]:
                            valid=False
                    # last char checks
                    elif ind == self.__num_indexes:
                        if char in ["x", "/", "+", "-", "("]:
                            valid = False
                    # additional checks
                    else:
                        if (char in operators or char == "(") and self.value[ind+1] in illegal_preceedings:
                            valid = False

                        elif char == ")" and (self.value[ind+1] == "." or self.value[ind+1].isdigit()):
                            valid = False

                        elif char == "." and self.value[ind+1] == ".":
                            valid = False

                    if not valid:
                        break

                return valid

        except Exception as e:
            print("ERROR occurred while validating format: ", e)
            return valid

    
    
    def __get_nearest_number_pair(self, ind: int):
        try:
            pass
        except Exception as e:
            print("ERROR occurred in getting nearest number pair: ", e)



    def __replacer(self, value: str, replacement: str, start_ind: int, end_ind: int):
        try:
            pass
        except Exception as e:
            print("ERROR occurred in replacer: ", e)



    def __perform_calculation(self, value: str):
        try:
            if value.count("(") > 0:
                pass
            else:
                pass

        except:
            pass



    def __resolve_dots(self, value):
        try:
            # Replace ".digit" with "0.digit"
            value = re.sub(r'(?<=\D)\.(?=\d)', '0.', value)
            
            # Replace digit. with 'digit.0'
            value = re.sub(r'(?<=\d)\.(?!\d)', '.0', value)

            # Replace "digit." at the end with "digit.0"
            value = re.sub(r'(?<=\d)\.$', '.0', value)

            return value
        
        except Exception as e:
            print("ERROR occurred while resolving dots: ", e)

    def __resolve_sequential_operators(self, value: str):
        try:
            def repl(match):
                if match.group() == '--':  # Replace consecutive '-' with '+'
                    return '+'
                else:  # Replace other patterns
                    return match.group().replace('+', '').replace('-', '')

            pattern = r'\+{2,}|-{2,}|\+-|-\+'
            cleaned_value = re.sub(pattern, repl, value)
            return cleaned_value

        except Exception as e:
            print("ERROR occurred in resolver: ", e)

    def __resolve_opening_bracket(self, value: str):
        try:
            # Define a replacement function for the regular expression
            def repl(match):
                return 'x('

            # Regular expression pattern to identify '(' preceded by a digit or ')'
            pattern = r'(?<=[0-9\)])\('
            cleaned_value = re.sub(pattern, repl, value)
            return cleaned_value

        except Exception as e:
            print("ERROR occurred in resolver: ", e)

    def __resolver(self, value: str):
        """
        Responsible for resolving calculation values -> performs cleanup.

        Does the following cleanup duties:
        - turns sequences of + or - into a single operator.
        - places x before a ( bracket if no operator is found.
        - places a digit before or after . if no digit is found before or after.
        """
        try:
            value = self.__resolve_sequential_operators(value)
            value = self.__resolve_dots(value)
            value = self.__resolve_opening_bracket(value)

            return value

        except Exception as e:
            print("ERROR occurred in resolver: ", e)

   
   
    def calculate(self):
        if not self.__validate():
            return "SYNTAX ERROR"
        else:
            self.value = self.__resolver(self.value)
            print(self.value)
            return self.__perform_calculation(self.value)
        

        



        
