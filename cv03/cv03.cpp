#include <iostream>
#include "formla.h"

int main()
{
	Formula *f = new Equivalence(
		new Conjunction(
			new Variable("alfa"),
			new Negation(new Variable("beta"))
		),
		new Disjunction(
			new Vriable("alfa"),
			new Implication(
				new Variable("beta"),
				new Variable("alfa")
			)
		)
	);
	// vypise ((alfa&-beta)<=>(alfa|(beta=>alfa)))
	std::cout << f->toString() << std::endl;
	Interpretation i;
	i["alfa"] = true;
	i["beta"] = false;
	if (f->eval(i))
		std::cout << "pravdiva" << std::endl;
	else
		std::cout << "nepravdiva" << std::endl;

	delete f;
	return 0;
}
