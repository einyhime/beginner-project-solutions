#include <iostream>
#include <string>
#include <cmath>

int main()
{
	while (true)
	{
		int num;
		std::cout << "Enter a number: ";
		std::cin >> num;
		std::string str = std::to_string(num);
		int digit = str.size(), total = 0;
		for (auto i : str)
			total += pow((i - 48), digit);

		std::cout << num;

		if (num == total)
			std::cout << " is an Armstrong Number!";
		else
			std::cout << " is not an Armstrong Number!";

		std::cout << "\nCheck another number? press q to quit... ";
		char quit;
		std::cin >> quit;
		if (quit == 'q')
			break;
	}
}
