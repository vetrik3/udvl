#include <vector>
#include <string>
#include <fstream>

namespace sat {

class DimacsWriter
{
	std::string m_filename;
	std::ofstream m_f;

public:
	DimacsWriter(const std::string &name, std::ios_base::open_mode mode = std::ios_base::out);
	std::string filename() const { return m_filename; }
	void writeLiteral(int lit);
	void finishClause();
	void writeClause(const std::vector<int> &clause);
	void writeClause(const std::initializer_list<int> &clause);
	void writeImpl(int left, int right);
	bool closed();
	void close();
};

class SatSolver
{
public:
	struct Result {
		bool sat = false;
		std::vector<int> vars;
	};
	SatSolver(const std::string &solverPath = "");
	std::string getSolverPath();
	Result solve(const std::string &theoryFile, const std::string &outputFile);
	Result solve(DimacsWriter *theoryWriter, const std::string &outputFile);
};

} //namespace sat
