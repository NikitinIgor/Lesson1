def get_vat(payment, persent=18):
    try:
        payment= float(payment)
        persent =int (persent)
        vat = payment /100 * persent
        vat = round(vat,2)
        return 'Сумма НДС: {}'.format(vat)
    except (TypeError, ValueError):
        return("Не могу посчитать, проверьте вводимые данные.")

result = get_vat(400, 10)
print(result)
