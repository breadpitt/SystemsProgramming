#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <string>
#include <sstream>

/// Weaknesses: could improve by using hybrid instead of just tail tweaking
// using same file for username and password
// assigning a truly random index number would be best instead of reusing the first random roll
// for simplicities sake duplicate random rolls are rare enough to be ignored but would otherwise be a big nono
// complicated user entered username could stand out due to simplicity of hw file
int rand_digit(void)
{
    int r = rand() % 999 + 1;
    return r;
}

void print_vector(std::vector<std::string> pvector)
{
    for (int i = 0; i < pvector.size(); i++)
    {
        std::cout << pvector[i] << ",";
    }
    std::cout << "\n";
}

std::vector<std::string> shuffle_vector(std::vector<std::string> ordered)
{
    std::random_device rd;
    std::mt19937 g(rd());
    std::shuffle(ordered.begin(), ordered.end(), g); // Randomly shuffles the elements in the vector
    return ordered;
}

std::vector<std::vector<std::string> > shuffle_vector(std::vector<std::vector<std::string> > vectorvector)
{
    std::random_device rd;
    std::mt19937 g(rd());
    std::shuffle(vectorvector.begin(), vectorvector.end(), g); // Randomly shuffles the elements in the vector of string vectors
    return vectorvector;
}

std::vector<std::string> gen_var_randoms(int num_honeyaccounts)
{
    std::vector<std::string> randvect;
    int rando;
    for (int i = 0; i < num_honeyaccounts - 1; i++)
    {
        rando = rand_digit();
        randvect.push_back(std::to_string(rando));
    }
    return randvect;
}

std::vector<std::string> get_honeyindex(std::string filename, std::string username)
{
    int offset = 0;
    std::string line;
    std::ifstream Myfile;
    Myfile.open(filename);

    if (Myfile.is_open())
    {
        while (!Myfile.eof())
        {
            getline(Myfile, line);
            std::stringstream ss(line);

            std::string temp; //int i = 0;
            std::vector<std::string> honeyvector;
            while (std::getline(ss, temp, ','))
            {
                honeyvector.push_back(temp);
            }
            if (honeyvector[0] == username)
            {
                return honeyvector;
            }
        }
        Myfile.close();
    }
    std::vector<std::string> emptyvector;
    emptyvector[0] = "FAIL";
    return emptyvector;
}

bool check_file(std::string filename, std::string username)
{
    int offset = 0;
    std::string line;
    std::ifstream Myfile;
    Myfile.open(filename);

    if (Myfile.is_open())
    {
        while (!Myfile.eof())
        {
            getline(Myfile, line);
            if ((offset = line.find(username, 0)) != std::string::npos)
            {
                //std::cout << "found '" << username << " \n\n"<< line  << std::endl;
                return true;
            }
        }
        Myfile.close();
    }
    else
    {
        std::cout << "Unable to open this file." << std::endl;
    }
    return false;
}

std::string rand_username(void)
{
    int count = 0;
    std::string ryline = ""; // random line for rockyou
    int numOfLines = 0;
    std::string rusername = "";

    std::ifstream rockyou("rockyou.txt");

    int ryru = rand_digit(); // rock you random user
    if (rockyou.is_open())
    {
        while (getline(rockyou, ryline))
        {
            ++numOfLines;

            if (numOfLines == ryru)
            {
                rusername = ryline;
                //std::cout << rusername << "\n";
            }
        }
    }
    else
    {
        std::cout << "File Didn't Open\n";
        return rusername;
    }
    rockyou.close();
    count++;

    return rusername;
}

///////////// gen rand pswd
std::vector<std::string> rand_pswd(int num_honeywords, std::string pswd)
{
    std::random_device rd;
    std::mt19937 g(rd());

    int r = rand_digit();
    std::string sugarword = pswd + std::to_string(r);
    std::vector<std::string> honeyvector;
    honeyvector.push_back(sugarword);

    for (int i = 0; i < num_honeywords - 1; i++)
    {
        std::string honeyword = "";
        int rd = rand_digit();
        honeyword = pswd + std::to_string(rd);
        honeyvector.push_back(honeyword);
    }

    std::shuffle(honeyvector.begin(), honeyvector.end(), g); // Randomly shuffles the elements in the vector
    return honeyvector;
}

// create vector of vectors of the form < <username, password, index>, <...>, ...>
std::vector<std::vector<std::string> > gen_honeylist(std::vector<std::string> sugarvector, int num_honeyaccounts)
{
    std::vector<std::vector<std::string> > honeylist;
    std::vector<std::string> honey_index;

    for (int i = 0; i < num_honeyaccounts; i++)
    {
        std::vector<std::string> honeyusernamevector;
        std::string genusername = rand_username();
        honeyusernamevector.push_back(genusername);
        std::string genpassword = rand_username();
        std::vector<std::string> temp_pswdvector = rand_pswd(num_honeyaccounts, genpassword);

        for (int i = 0; i < temp_pswdvector.size(); i++)
            {
                honeyusernamevector.push_back(temp_pswdvector[i]);
            }

        //honeyusernamevector.push_back(genpassword);
        int rand_index = rand_digit(); // before loop so the sugar account doesn't have 1 more index than others
        honey_index = gen_var_randoms(num_honeyaccounts);
        honey_index.push_back(std::to_string(rand_index));
        honey_index = shuffle_vector(honey_index); // otherwise the first or last index will be known to always be the sugar

        for (int i = 0; i < honey_index.size(); i++)
        {
            honeyusernamevector.push_back(honey_index[i]);
        }
        //honeyusernamevector.push_back(std::to_string(rand_index));
        //print_vector(honeyusernamevector);
        honeylist.push_back(honeyusernamevector);
    }
    honeylist.push_back(sugarvector);
    honeylist = shuffle_vector(honeylist);
    return honeylist;
}

/*
bool set_password(std::string password, std::string sugar_index)
{
    std::ofstream hashindex("hashindex.txt"); // F2
    if (hashindex.is_open())
    {
        // hash password here
        hashindex << password << ","; // write username to file
        hashindex << sugar_index << "\n";
    }
    else
    {
        std::cout << "Error opening hashindex file \n";
        return false;
    }
    return true;
}
*/
//////////////// main function
int main()
{
    srand((unsigned)time(NULL));

    std::ofstream tmp_file("temp.txt");
    //std::ofstream hash_file("hashFile.txt");
    std::string userindex_fn = "userindex.txt";

    std::ofstream userindex(userindex_fn); // F1

    int num_honeywords = 6;            // change this later
    int num_honeyaccounts = 6;         // honeyaccounts
    std::string username = "username"; // change later
    std::string pswd = "password";     // change late
    /*
    std::cout << "Enter a password between 8 and 12 characters in length \n";
    std::string pswd = "";
    std::cin >> pswd;

    while (pswd.length() < 8 || pswd.length() > 12)
    {
        std::cout << "Invalid number of characters. Please enter a password between 8 and 12 characters in length \n";
        std::cin >> pswd;
    }
    */

    // constructs a vector of <username, sugarword, hw, ... ,>
    std::vector<std::string> sugarvector;
    int sugartail = rand_digit();
    std::string sugarword = pswd + std::to_string(sugartail);
    std::vector<std::string> honeyindexes_forsugar;
    sugarvector.push_back(username);
    std::vector<std::string> temp_pswdvector = rand_pswd(num_honeywords, pswd); // also shuffles where sugarword is in the vector
    print_vector(temp_pswdvector);
    for (int i =0; i < temp_pswdvector.size(); i++){
            sugarvector.push_back(temp_pswdvector[i]);
    }

    // constructs a vector of <username, sugarword, hw, ... , sugarindex, ... honeyindex, ...., >
    int sugar_index = rand_digit();
    honeyindexes_forsugar = gen_var_randoms(num_honeyaccounts);
    honeyindexes_forsugar.push_back(std::to_string(sugar_index));
    honeyindexes_forsugar = shuffle_vector(honeyindexes_forsugar); // shuffles the sugarindex
    for (int i = 0; i < honeyindexes_forsugar.size(); i++)
    {
        sugarvector.push_back(honeyindexes_forsugar[i]);
    }
   
    // now do the same for x amount of honeyusers and shuffle in the sugaraccount
    std::vector<std::vector<std::string> > honeylist(num_honeyaccounts);
    honeylist = gen_honeylist(sugarvector, num_honeyaccounts);

    // write to F1
    for (int i = 0; i < honeylist.size(); i++)
    {
        if (userindex.is_open())
        {
            std::vector<std::string> tempvector = honeylist[i];
            // print_vector(tempvector);
            userindex << tempvector[0] << ","; // write username to file
            for (int j = num_honeywords; j < tempvector.size(); j++)
            {
                userindex << tempvector[j] << ","; // skip password, write honey indexes
            }
            userindex << "\n";
        }
        else
        {
            std::cout << "Error opening userindex file \n";
            return 1;
        }
    }
    userindex.close();

    // write to F1
    std::ofstream hashindex("hashindex.txt");
    for (int i = 0; i < honeylist.size(); i++)
    {
        if (hashindex.is_open())
        {
            std::vector<std::string> tempvector = honeylist[i];
            hashindex << tempvector[2] << ","; // write  an index to file 2
            hashindex << tempvector[1] << ","; // write password to file 2
            hashindex << "\n";
        }
        else
        {
            std::cout << "Error opening userindex file \n";
            return 1;
        }
    }
    hashindex.close();


    // check if username is in  F1
    int ret = 0;
    if ((ret = check_file(userindex_fn, username)) == 0)
    {
        std::cout << "Username no found in system \n";
    }
    // if it is need to grab the honeyindex from file 2 / hashindex
    std::vector<std::string> honeyindex = get_honeyindex(userindex_fn, username);
    //print_vector(honeyindex);

    // write to F2
    //set_password(std::to_string(sugar_index), pswd);

    // print_vector(hnyusnvector);
    //std::vector<std::string> honeyusernamevector;

    /* write to temp file
    for (int i = 0; i < honeyvector.size(); i++)
    {
        tmp_file << honeyvector[i] << std::endl;
        tmp_file.close();
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

    return 0;
}
