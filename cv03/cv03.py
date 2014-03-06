from formula import Variable, Negation, Conjunction, Dijunction, Implication, Equivalence

f = Equivalence(
	Conjunction(
		Variable('alfa'),
		Negation(Variable('beta'))
	),
	Disjunction(
		Variable('alfa'),
		Implication(
			Variable('beta'),
			Variable('alfa')
		)
	)
)
# vypise ((alfa&-beta)<=>(alfa|(beta=>alfa)))
print(f.toString())

i = {}
i['alfa'] = True;
i['beta'] = False;
if f.eval(i):
	print('pravdiva')
else:
	print('nepravdiva')
return 0;
