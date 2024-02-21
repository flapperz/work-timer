#include <iostream>
#include <fstream>
#include <string>
// using namespace std;

#define LOG_FNAME "/Users/flap/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents/work-timer-log.txt"

int main()
{
	std::ifstream file;
	std::string readline;

	file.open(LOG_FNAME);

	if (file.is_open())
	{
		while (file.good())
		{
			std::getline (file, readline);
			std::cout << readline << std::endl;
		}
		
	}
	std::cout << "Hello World!" << std::endl;
	return 0;
}