#include <iostream>
#include <vector>
#include <algorithm>
#include <random>

int main(){
    std::cout << "Enter a password between 8 and 12 characters in length \n";
    std::string pswd = "";
    std::cin >> pswd;

    while (pswd.length() < 8 || pswd.length() > 12){
        std::cout << "Invalid number of characters. Please enter a password between 8 and 12 characters in length \n";
        std::cin >> pswd;
    }

    std::string create_username = "";
    std::string create_pswd = "";
    std::cout << "Create a new account? (y/n)\n";
    std::string createacc = "";
    if (createacc == "y" || createacc == "Y"){
        std::cout << "Enter a username \n";
        std::cin >> create_username;
        std::cout << "Enter a password \n";
        std::cin >> create_pswd;
        
    }

    return 0;
}