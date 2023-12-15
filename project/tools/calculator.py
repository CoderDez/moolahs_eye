class Calculator:
    
    def __init__(self, calculation: str) -> None:
        self.calculation = calculation
        self.num_indexes = len(calculation) - 1

    def __validate(self):
        valid = True
        try:
            # if string is empty return valid
            if self.num_indexes < 0:
                return valid
            
            operators = ["+", "-", "x", "/"]
            illegal_operator_preceedings = ["x", "/"]

            for ind, char in enumerate(self.calculation):
                # if first character
                if ind == 0:
                    if char in ["x", "/", ")"]:
                        valid = False
                        break
                # if last character
                elif ind == self.num_indexes:
                    if char in ["x", "/", "(", "+", "-"]:
                        valid = False
                        break
                # if not first or last char
                else:
                    if char in operators:
                        if self.calculation[ind+1] in illegal_operator_preceedings:
                            valid = False
                            break

                    elif char == "(":
                        if self.calculation[ind+1] == ")":
                            valid = False
                            break
                    
                    elif char == ")":
                        if self.calculation[ind+1] == "." or self.calculation[ind+1].isdigit():
                            valid = False
                            break
                    
                    elif char == ".":
                        pass

                
        except Exception as e:
            valid = False
            return valid
    
    def __get_bracket_pairs(self):
        brackets = []
        try:
            found_opening =  0
            found_closing = self.num_indexes

            while found_opening != -1 or found_closing != -1:
                if not brackets:
                    found_opening = self.calculation.find("(")
                    found_closing = self.calculation.rfind(")")
                else:
                    found_opening = self.calculation.find("(", start=found_opening+1)
                    found_closing = self.calculation.rfind(")", start=found_closing-1)

                if found_opening != -1 or found_closing != -1:
                    brackets.append((found_closing, found_opening,))
        except:
            pass


    def calculate(self):
        try:
            valid = self.__validate()
        except Exception as e:
            raise

        if valid:
            pass


def get_bracket_pairs(calculation: str):
    opening_brackets = []
    closing_brackets = []
    try:
        for ind , char in enumerate(calculation):
            if char == "(":
                opening_brackets.append(ind)
            elif char == ")":
                closing_brackets.append(ind)
                
    except:
        pass


get_bracket_pairs("((Now)) (((9)))")