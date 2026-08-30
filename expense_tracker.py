expenses=[ ]
print('='*60)
print('             student expense tracker')
print('='*60)
print('1.add expense')
print('2.view expense')
print('3.total spending')
print('4.exit')
choise=input('enter ur choise:')
while True:
	print('welcome')
	choise=input('enter ur choise:')
	if choise=='1':
		name=input('enter expense name:')
		amount=float(input('enter expense amount:'))
		expenses.append((name,amount))
		print('expense added succesfully')
	elif choise=='2':
		if expenses:
			for name,amount in expenses:
				print(name, ' - ',amount)
		else:
			print('no expense found')
	elif choise=='3':
	    total=sum(amount for name,amount in expenses)
	    print('total spending:',total)
	elif choise=='4':
		print('thankyou for using student expense tracker ')
		break
	else:
		print('invalid choise please try again')
	