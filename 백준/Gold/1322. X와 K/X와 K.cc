#include<iostream>
#include<algorithm>
using namespace std;

long long X, K, j;
long long ans;

int main() 
{
	cin >> X >> K;

	X = ~X;

	for (int i = 0; i < 64; i++)
	{
		if (((long long)1 << i) & X)
		{
			if (((long long)1 << j) & K)
				ans += ((long long)1 << i);

			j++;
		}
	}

	cout << ans;
}