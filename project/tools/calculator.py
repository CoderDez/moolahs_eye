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
            if not (self.value.count("(") == self.value.count(")")):
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
                illegal_preceedings = ["x", "/"]

                for ind, char in enumerate(self.value):
                    if ind == 0:
                        if char in ["x", "/", ")"]:
                            valid=False
                    elif ind == self.__num_indexes:
                        if char in ["x", "/", "(", "+", "-"]:
                            valid = False
                    else:
                        if char in operators and self.value[ind+1] in illegal_preceedings:
                            valid = False

                        elif char == "(" and self.value[ind+1] == ")":
                            valid = False

                        elif char == ")" and (self.value[ind+1] == "." or self.value[ind+1].isdigit()):
                            valid = False

                        elif char == "." and self.value[ind+1] == ".":
                            valid = False

                    if not valid:
                        break

                return valid
#
        except Exception as e:
            print("ERROR occurred while validating format: ", e)
            return valid

    def calculate(self):
        if not self.__validate():
            return "SYNTAX ERROR"
        else:
            pass
