#github 
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def infixToPostfix(expression):
    stack = []
    result = []
    for char in expression:
        if char.isalnum():
            result.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                result.append(stack.pop())
            stack.append(char)
    
    while stack:
        result.append(stack.pop())
    
    return ''.join(result)

expression = input("Enter infix expression: ")
print("Postfix expression:", infixToPostfix(expression))

INPUT:-
Enter infix expression: A*(B+C)

OUTPUT:-
Postfix expression: ABC+*
