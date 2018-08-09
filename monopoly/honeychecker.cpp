#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <string>

int rand_digit(void){
    int r = rand() % 999 + 1;
    return r;
}
int main(){
    std::random_device rd;
    std::mt19937 g(rd());
    srand((unsigned) time(NULL));

    std::ofstream tmp_file("temp.txt");
    std::ofstream hash_file("hashFile.txt");
    std::ifstream rock_you("rock_you.txt");

    int num_hw = 6; // change this later
    int num_hacc = 6; // honeyaccounts
    std::string ryline = ""; // rockyou line
    std::cout << "Enter a password between 8 and 12 characters in length \n";
    std::string pswd = "";
    std::cin >> pswd;

    while (pswd.length() < 8 || pswd.length() > 12){
        std::cout << "Invalid number of characters. Please enter a password between 8 and 12 characters in length \n";
        std::cin >> pswd;
    }

    int r = rand_digit();
    std::string sugarword = pswd + std::to_string(r);
    std::vector<std::string> honeyvector;
    honeyvector.push_back(sugarword);

    for (int i = 0; i < num_hw - 1; i++){
        std::string honeyword = "";
        int rd = rand_digit();
        honeyword = pswd + std::to_string(rd);
        honeyvector.push_back(honeyword);
    }

    std::shuffle(honeyvector.begin(), honeyvector.end(), g); // Randomly shuffles the elements in the vector

    for (int i = 0; i < honeyvector.size(); i++){
        tmp_file << honeyvector[i] << std::endl;
        tmp_file.close();
    }
/*
    for (int i = 0; i < honeyvector.size(); i++){
       std::cout << honeyvector[i] << "\n";
    }
*/
    /*

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
    read a random username from a file
    */

    int count = 1;
while(count <= 3)
{
    int rw = rand_digit(); // rand int for rant username / pswd
    while(getline(rock_you, ryline))
    {
        ++numOfLines;

        if(numOfLines == random)
        {
            std::cout << ryline;
        }
    }
    count++;
}
/*
check if word in file

    int offset; 
    string line;
    ifstream Myfile;
    Myfile.open (filename);

    if(Myfile.is_open())
    {
        while(!Myfile.eof())
        {
            getline(Myfile,line);
            if ((offset = line.find(search, 0)) != string::npos) 
            {
             cout << "found '" << search << " \n\n"<< line  <<endl;
             return true;
            }
            else
            {

                cout << "Not found \n\n";

            }
        }
        Myfile.close();
    }
    else
    cout<<"Unable to open this file."<<endl;
    */

    return 0;
}