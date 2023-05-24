#include <array>
#include <cmath>
#include <iostream>

const std::array<float, 5> K_COINS = {2.0f, 1.0f, 0.5f, 0.2f, 0.1f};

std::array<int, 5> get_coins(float amount)
{
  amount = round(amount * 10.0) / 10.0;
  std::array<int, 5> arr;	
  arr.fill(0.0f);
  for (int i = 0; i < 5; i++)
  {
  	while (amount > K_COINS[i])
	{
	  arr[i] += amount / K_COINS[i];
	  amount = fmodf(amount, K_COINS[i]);
	}
  }
  return (arr);
}

int main()
{
  std::array<int, 5> arr = get_coins(21.88);
  for (int i = 0; i < arr.size(); i++) {
    std::cout << arr[i] << " | ";
  }
  std::cout << std::endl;
  return (0);
}
