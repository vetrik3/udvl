import java.util.Map;
import java.util.HashMap;

public class Cv03.java {
	public static void main(String[] args) {
		Formula f = new Equivalence(
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
		System.out.println(f.toString());
		Map<String,Boolean> i = new HashMap<String,Boolean>();
		i.put("alfa", true);
		i.put("beta", false);
		if (f.eval(i)) {
			System.out.println("pravdiva");
		} else {
			System.out.println("nepravdiva");
		}
}
