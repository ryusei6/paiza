alpabet = {}
for i in range(97, 123):
    alpabet[chr(i)] = 0


def analyze(num_s, S):
    f = '1'
    for i in range(len(S)):
        if S[i] == '(':
            f += '*' + num_s
            num_s = ''
            continue
        if S[i] == ')':
            f = '*'.join(f.split('*')[:-1])
            if f == '':
                f = '1'
            continue
        # print(f, num_s, S[i])
        if S[i].isalpha():
            if num_s == '':
                num_s = '1'
            alpabet[S[i]] += eval(f) * int(num_s)
            num_s = ''
        else:
            num_s += S[i]
    for c_i in range(97, 123):
        print(chr(c_i), alpabet[chr(c_i)])


def main():
    S = input()
    analyze('', S)


if __name__ == '__main__':
    main()