def print_formatted(number):
    # your code goes here
    w = len(bin(number)[2:])
    for i in range(1, number + 1):
        print(str(i).rjust(w, ' '), oct(i).lstrip('0o').rjust(w, ' ')
              , hex(i).lstrip('0x').upper().rjust(w, ' '),
              bin(i).lstrip('0b').rjust(w, ' '),
              sep=' ')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)