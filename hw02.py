class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            print("pop() error: Stack is empty.")
            return None

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("peek() error: Stack is empty.")
            return None

    def size(self):
        return len(self.items)


"""
1. postfixEval
Input type: a list of strings
Output type: a floating point number
"""

def postfixEval(list):
    s = Stack()
    total = 0
    for n in list:
        if n != "+" and n!= "-" and n!= "*" and n!= "/":
            s.push(n)
            total = n
        if n == "+":
            a = float(s.pop())
            b = float(s.pop())
            total = (a + b)
            s.push(total)
        if n == "-":
            c = float(s.pop())
            d = float(s.pop())
            total = (d - c)
            s.push(total)
        if n == "*":
            e = float(s.pop())
            f = float(s.pop())
            total = (f * e)
            s.push(total)
        if n == "/":
            g = float(s.pop())
            h = float(s.pop())
            total = (h / g)
            s.push(total)
    return float(total)


"""
2. validParentheses
Input type: a string
Output type: a Boolean
"""
def validParentheses(string):
    s = Stack()
    for ch in string:
        if ch == "(" or ch == "[" or ch == "{":
            s.push(ch)
        if ch == ")":
            if not s.isEmpty():
                a = s.pop()
                if a != "(":
                     return False
            else:
                return False
        if ch == "]":
            if not s.isEmpty():
                b = s.pop()
                if b != "[":
                    return False
            else:
                return False
        if ch == "}":
            if not s.isEmpty():
                c = s.pop()
                if c != "{":
                    return False
            else:
                return False
    return s.isEmpty() 



"""
3. reverseString
Input type: a string
Output type: a string
"""
def reverseString(string):
    stack1 = Stack()
    new_string = ""
    for c in string:
        stack1.push(c)
    for c in string:
        new_string += stack1.pop()
    return new_string
        
        







