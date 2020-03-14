import textwrap

def wrap(string, max_width):
    wrapper=textwrap.TextWrapper(width=4)
    result= wrapper.fill(text=string)
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)