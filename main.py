def is_palindrome(s):
    s = s.lower()
    s = ''.join(filter(str.isalnum, s))
    return s == s[::-1]


def main():
    try:
        number = input('Masukan Nilai: ')
        if is_palindrome(number):
            print(f'{number} is palindrome')
        else:
            print(f'{number} is not palindrome')
    except:
        print('Input Invalid')


if __name__ == '__main__':
    main()
