#include "cnf.h"
#include <iostream>

struct Case {
	Case(const Interpretation &i_, bool result_)
		: i(i_)
		, result(result_)
	{}
	Interpretation i;
	bool result;
};
/**
 * Pekny vypis interpretatcie
 */
std::ostream& operator<< (std::ostream& stream, const Interpretation &i)
{
	stream << "{ ";
	for(auto p : i) {
		stream << p.first << ": " << p.second << " ";
	}
	stream << "}";
	return stream;
}

class Tester {
	int m_tested = 0;
	int m_passed = 0;
public:

	template<typename T, typename... Ms>
	void compare(const T &result, const T &expected, Ms... msgs)
	{
		m_tested++;
		if (result == expected) {
			m_passed++;
		}
		else {
			std::cerr << "    Failed: ";
			int dummy[sizeof...(Ms)] =  { (std::cerr << " " << msgs, 0)... };
			int x = sizeof(dummy); x++; // dummy is unused ;(
			std::cerr << ":" << std::endl;
			std::cerr << "      got " << result << " expected: " << expected << std::endl;
		}
	}

	void status()
	{
		std::cerr << "TESTED " << m_tested << std::endl;
		std::cerr << "PASSED " << m_passed << std::endl;
		std::cerr << ( m_tested == m_passed ? "OK" : "ERROR" ) << std::endl;
	}


	template<class C>
	void testCnf(const C &cnf, const std::string &str, const std::vector<Case> &cases){
		compare(cnf.toString(), str, "toString");
		for (const auto &c : cases) {
//			std::cerr << "Interpretation " << c.i << std::endl;
			compare(cnf.eval(c.i), c.result, "eval", c.i);
		}
	}

};

int main()
{
	Tester t;


    t.compare( CnfLit("a").name(), std::string("a"), "CnfLit.name" );
    t.compare( CnfLit("a").neg(), false, "CnfLit.neg" );
    t.compare( CnfLit::Not("a").name(), std::string("a"), "CnfLit.Not.name" );
    t.compare( CnfLit::Not("a").neg(), true, "CnfLit.Not.neg" );
    t.compare( (-CnfLit("a")).name(), std::string("a"), "-CnfLit.Not.name" );
    t.compare( (-CnfLit("a")).neg(), true, "-CnfLit.Not.neg" );
    t.compare( (- -CnfLit("a")).name(), std::string("a"), "--CnfLit.Not.name" );
    t.compare( (- -CnfLit("a")).neg(), false, "--CnfLit.Not.neg" );

	Interpretation i1t, i1f, i2tt, i2tf, i2ft, i2ff;
	i1t["a"] = true;
	i1f["a"] = false;
	i2tt["a"] = true;  i2tt["b"] = true;
	i2tf["a"] = true;  i2tf["b"] = false;
	i2ft["a"] = false; i2ft["b"] = true;
	i2ff["a"] = false; i2ff["b"] = false;
	t.testCnf(
			CnfLit("a"), "a",
			{
				Case(i1t, true),
				Case(i1f, false),
			});;

	t.testCnf(
			-CnfLit("a"),"-a",
			{
				Case(i1t, false),
				Case(i1f, true),
			});

	t.testCnf(
			CnfLit::Not("a"), "-a",
			{
				Case(i1t, false),
				Case(i1f, true),
			});

	t.testCnf(
			CnfClause( { CnfLit("a"), CnfLit("a") } ), "a a",
			{
				Case(i1t, true),
				Case(i1f, false),
			});

	t.testCnf(
			CnfClause( { CnfLit("a"), CnfLit::Not("a") } ), "a -a",
			{
				Case(i1t, true),
				Case(i1f, true),
			});

	t.testCnf(
			Cnf( {
				CnfClause( { CnfLit("a"), CnfLit::Not("b") } ),
				CnfClause( { CnfLit("b") } ),
			}),
			"a -b\nb\n",
			{
				Case(i2tt, true),
				Case(i2tf, false),
				Case(i2ft, false),
				Case(i2ff, false),
			});

	// TODO otestovat VariableMap, extendVarMap, writeTo / readFrom File

	t.status();
	return 0;
}
