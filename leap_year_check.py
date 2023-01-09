
def main():
    try:
        year = int(input('Enter the year: '))
    except:
        print('Enter a valid year'); exit()

    if year % 4 == 0 and year % 100 != 0:
        print(f'{year} is a leap year')
    elif year % 400 == 0 and year % 100 == 0:
        print(f'{year} is a leap year')
    else:
        print(f'{year} is not a leap year')


if __name__=='__main__':
    main()