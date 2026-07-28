import ast
import math
import operator


class Calculator:
    def __init__(self):
        self.expression = ""

        # Mapping allowed standard binary operators
        self._operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Mod: operator.mod,
            ast.Pow: operator.pow,
            ast.USub: operator.neg,
            ast.UAdd: operator.pos,
        }

    def clear(self):
        """Resets the current calculation string."""
        self.expression = ""
        return self.expression

    def press(self, button: str) -> str:
        """Appends button input dynamically to the expression.

        Supports UI symbols like '×', '÷', 'π', '√', 'x²', 'mod', '%'.
        """
        if button == "C":
            return self.clear()

        # Translate special UI buttons into expression format
        if button == "π":
            self.expression += str(math.pi)
        elif button == "x²":
            self.expression += "**2"
        elif button == "√":
            self.expression += "sqrt("
        elif button == "%":
            self.expression += "/100"
        elif button == "mod":
            self.expression += "%"
        else:
            self.expression += str(button)

        return self.expression

    def evaluate(self) -> str:
        """Safely evaluates the current mathematical expression."""
        if not self.expression:
            return "0"

        try:
            # Format expression for Python parser
            formatted_expr = (
                self.expression.replace("×", "*")
                .replace("÷", "/")
                .replace("sqrt", "math_sqrt")
            )

            # Parse and evaluate safely without using eval()
            parsed_ast = ast.parse(formatted_expr, mode="eval")
            result = self._eval_node(parsed_ast.body)

            # Format floating points cleanly (e.g., 5.0 -> 5)
            if isinstance(result, float) and result.is_integer():
                result = int(result)

            self.expression = str(result)
            return self.expression

        except ZeroDivisionError:
            self.expression = ""
            return "Error: Division by zero"
        except Exception:
            self.expression = ""
            return "Error"

    def _eval_node(self, node):
        """Recursive AST evaluator for safe math computation."""
        if isinstance(node, ast.Constant):  # Numbers
            return node.value

        elif isinstance(node, ast.BinOp):  # Binary operations (+, -, *, /, %, **)
            left = self._eval_node(node.left)
            right = self._eval_node(node.right)
            op_type = type(node.op)
            if op_type in self._operators:
                return self._operators[op_type](left, right)

        elif isinstance(node, ast.UnaryOp):  # Negation (-5)
            operand = self._eval_node(node.operand)
            op_type = type(node.op)
            if op_type in self._operators:
                return self._operators[op_type](operand)

        elif isinstance(node, ast.Call):  # Functions like √ (sqrt)
            if getattr(node.func, "id", "") == "math_sqrt":
                arg = self._eval_node(node.args[0])
                if arg < 0:
                    raise ValueError("Cannot calculate square root of negative number")
                return math.sqrt(arg)

        raise ValueError("Invalid Expression")


# ==================== টার্মিনালে ইউজার ইনপুট দিয়ে চালানোর অংশ ====================
if __name__ == "__main__":
    calc = Calculator()

    print("--- Python Calculator ---")
    print("Input Rules:")
    print(" multiply: * or × | divide: / or ÷ | power/square: **2")
    print(" root: sqrt(25) | modulus: % or mod | do stop: exit\n")

    while True:
        user_input = input("Write Calculate (ex: (8 * 9) / 2): ")

        if user_input.lower() == "exit":
            print("Close Calculator")
            break

        # direct input set
        calc.expression = user_input

        # fetch result
        result = calc.evaluate()
        print(f"Result: {result}\n")
