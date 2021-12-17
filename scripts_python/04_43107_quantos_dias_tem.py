
def is_year_leap(year):
# condições para o ano ser considerado bissexto ou não.
    if year < 1582:
        return False
    elif year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
    	return False

def days_in_month(year, month):
#dias dos meses
	dias_no_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# caso o ano seja bissexto, fevereiro terá 29 dias e não 28
	if is_year_leap(year):
		if month == 2:
			return 29
# em qualquer outro caso podemos retornar o numero de dias do mes de acordo com o mês passado como argumento, lembrando que no teste fevereiro é 2 e na lista dias_no_mes fevereiro é 1, por isso usaremos mount-1
	return dias_no_mes[month - 1]



test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
