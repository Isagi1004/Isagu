class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        m = []

        for i in range(len(tokens)):
            if tokens[i].lstrip('-').isdigit():
                m.append(int(tokens[i]))
            else:
                match tokens[i]:
                    case "+":
                        m[-2] = m[-2] + m[-1]
                        m.pop()
                    case "-":
                        m[-2] = m[-2] - m[-1]
                        m.pop()
                    case "*":
                        m[-2] = m[-2] * m[-1]
                        m.pop()
                    case "/":
                        m[-2] = int(m[-2] / m[-1])
                        m.pop()
        return m[0]