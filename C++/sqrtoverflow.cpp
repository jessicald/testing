#include <iostream>
using namespace std;
#include <cmath>

int main()
{
	cout.precision(13);
	int i = 2;
	//for (int t = 0; t < 10; t++)
	while (true)
	{
		double sqrt_i = sqrt(i);
		int x = int (sqrt_i);
		if (sqrt_i - double (x) < 1E-7)
		{
			cout << "sqrt(" << i << ") = " << sqrt_i << '\n';
		}
		i++;
	}
}
