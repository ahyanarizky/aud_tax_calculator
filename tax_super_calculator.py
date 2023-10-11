# Global variable to control when the program stop
running = True

while running:
    name = input('''Hi, welcome to tax&super calculator app!\nplease insert your name: ''')

    # Validation for 'name' (cannot contain number or symbol)
    for char in name:
        if not ('a' <= char <= 'z' or 'A' <= char <= 'Z' or char == ' '):
            print('your name is invalid')
            running = False
            break

    if not running:
        break

    hour_worked = input('please insert your hour worked: ')
    valid_characters = set('0123456789.,')
    # Validation for 'hour_worked' (cannot contain alphabet and another symbol)
    for char in hour_worked:
        if char not in valid_characters:
            print('your hour worked value is invalid')
            running = False
            break

    if not running:
        break

    max_hours_in_month = 744
    # Assuming max days in month = 31 and 1 day = 24 hours;
    # then 31*24 = 744
    if float(hour_worked) > max_hours_in_month:
        print('your hour worked value is invalid')
        running = False
        break

    hourly_rate = input('please insert your hourly rate (in AUD): ')
    for char in hourly_rate:
        if char not in valid_characters:
            print('your hourly rate value is invalid')
            running = False
            break

    if not running:
        break

    income_tax_rate = 0.2
    super_tax_rate = 0.1
    total_income = float(hour_worked) * float(hourly_rate)
    income_tax_deduction = total_income * income_tax_rate
    superannuation_deduction = total_income * super_tax_rate

    print(f'''============================================
    Hi {name}, this is your calculation details:
    - Hours worked: {hour_worked}
    - Hourly rate: {hourly_rate} AUD
    - Total income: {total_income}
    - Income tax deduction: {income_tax_deduction}
    - Superannuation deduction: {superannuation_deduction}
============================================''')

    if running:
        running = False
        # program ends.
