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
    std::shuffle(ordered.begin(), ordered.end(), g);
    return ordered;
}
// Randomly shuffles the elements in the vector of string vectors
std::vector<std::vector<std::string> > shuffle_vector(std::vector<std::vector<std::string> > vectorvector)
{
    std::random_device rd;
    std::mt19937 g(rd());
    std::shuffle(vectorvector.begin(), vectorvector.end(), g);
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

std::string rand_username(void)
{
    int count = 0;
    std::string ryline = ""; // random line for rockyou
    int numOfLines = 0;
    std::string rusername = "";

    std::ifstream rockyou("rockyou.txt");

    int ryru = rand_digit();
    if (rockyou.is_open())
    {
        while (getline(rockyou, ryline))
        {
            ++numOfLines;

            if (numOfLines == ryru)
            {
                rusername = ryline;
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

///////////// gen rand pswd - take a tail
/*
std::vector<std::string> rand_pswd_take_tail(int num_honeywords, std::string pswd, std::string sugarword)
{
    std::random_device rd;
    std::mt19937 g(rd());

    int r = rand_digit();
    std::vector<std::string> honeyvector;

    for (int i = 0; i < num_honeywords - 1; i++)
    {
        std::string honeyword = "";
        int rd = rand_digit();
        honeyword = pswd + rd);
     honeyvector.push_back(honeyword);
    }

    honeyvector.push_back(sugarword);
    std::shuffle(honeyvector.begin(), honeyvector.end(), g);
    return honeyvector;
}
*/

std::vector<std::string> rand_pswd(int num_honeywords, std::string sugarword)
{
    std::random_device rd;
    std::mt19937 g(rd());

    std::vector<std::string> honeyvector;

    for (int i = 0; i < num_honeywords - 1; i++)
    {
        std::string honeyword = rand_username();
        honeyvector.push_back(honeyword);
    }

    honeyvector.push_back(sugarword);
    std::shuffle(honeyvector.begin(), honeyvector.end(), g);
    return honeyvector;
}



// create vector of vectors of the form < <username, password, index>, <...>, ...>
std::vector<std::vector<std::string> > gen_honeylist(std::vector<std::string> sugarvector, int num_honeyaccounts, std::vector<std::string> &index_basket)
{
    std::vector<std::vector<std::string> > honeylist;
    std::vector<std::string> honey_index;

    for (int i = 0; i < num_honeyaccounts; i++)
    {
        std::vector<std::string> honeyusernamevector;
        std::string genusername = rand_username();
        honeyusernamevector.push_back(genusername);
        std::string honeypassword = rand_username();

        std::string honeysugarindex = index_basket.back();
        index_basket.pop_back();

        std::vector<std::string> honeysugarindexes;
        honeysugarindexes = gen_var_randoms(num_honeyaccounts);
        honeysugarindexes.push_back(honeysugarindex);
        honeysugarindexes = shuffle_vector(honeysugarindexes);
        
        for (int i = 0; i < honeysugarindex.size(); i++){
            honeyusernamevector.push_back(std::to_string(honeysugarindex[i]));
        }
        //honeyusernamevector.push_back(honeypassword);
        //should now have a honey account with a honeysugarword and honeyhoneywords
        /*
        std::vector<std::string> temp_pswdvector = rand_pswd(num_honeyaccounts, honeypassword);
        for (int i = 0; i < temp_pswdvector.size(); i++)
        {
            honeyusernamevector.push_back(temp_pswdvector[i]);
        }
        
        for (int i = 0; i < num_honeyaccounts; i++)
        {
            honeyusernamevector.push_back(index_basket.back());
            index_basket.pop_back();
        }
        */

        
        /*
        // generate a take-a-tail honeypasswords

        //int honeytail = rand_digit();
        //std::string fakesugarword = genpassword + honeytail);        //std::vector<std::string> temp_pswdvector = rand_pswd(num_honeyaccounts, genpassword, fakesugarword); 

        for (int i = 0; i < temp_pswdvector.size(); i++)
        {
            honeyusernamevector.push_back(temp_pswdvector[i]);
        }
        
       
        for (int i = 0; i < num_honeyaccounts; i++)
        {
            honeyusernamevector.push_back(index_basket.back());
            index_basket.pop_back();
        }
        */

        honeylist.push_back(honeyusernamevector);
        print_vector(honeyusernamevector);
    }
    honeylist.push_back(sugarvector);
    honeylist = shuffle_vector(honeylist);
    return honeylist;
}

int create_account(std::ofstream &userindex, std::ofstream &indexpassword, std::ofstream &honeychecker, std::string username, std::string sugarword, int num_honeywords, int num_honeyaccounts)
{
    // create all the random indexs needed
    std::vector<std::string> index_basket;
    
    for (int i = 0; i < 10 * num_honeyaccounts; i++)
    {
        std::vector<std::string> gen_indexes = gen_var_randoms(num_honeyaccounts);
        for (int j = 0; j < gen_indexes.size(); j++)
        {
            index_basket.push_back(gen_indexes[j]);
        }
    }
    // constructs a vector of <username, sugarword, hw, ... ,>
    std::vector<std::string> sugarvector;
    //std::cout << "SUGARWORD IS " << sugarword << "\n";
    std::vector<std::string> honeyindexes_forsugar;
    sugarvector.push_back(username);
    sugarvector.push_back(sugarword);
    std::string sugar_index = index_basket.back();
    index_basket.pop_back();
    
    // write sugar index and username to the honeychecker
    honeychecker << sugar_index << "," << username << "\n";
    std::cout << "SUGAR INDEX IS : " << sugar_index << "\n";


    honeyindexes_forsugar = gen_var_randoms(num_honeyaccounts);
    honeyindexes_forsugar.push_back(sugar_index);
    honeyindexes_forsugar = shuffle_vector(honeyindexes_forsugar); // shuffles the sugarindex
    for (int i = 0; i < honeyindexes_forsugar.size(); i++)
    {
        sugarvector.push_back(honeyindexes_forsugar[i]);
    }
    std::cout << "sugvect: \n";
    print_vector(sugarvector);
    /*
    std::vector<std::string> temp_pswdvector = rand_pswd(num_honeywords, pswd, sugarword); // also shuffles where sugarword is in the vector
    std::cout << "HONEYWORDS ARE: ";
    print_vector(temp_pswdvector);
    for (int i = 0; i < temp_pswdvector.size(); i++)
    {
        sugarvector.push_back(temp_pswdvector[i]);
    }
    
     constructs a vector of <username, sugarword, hw, ... , sugarindex, ... honeyindex, ...., >
    
    honeyindexes_forsugar = gen_var_randoms(num_honeyaccounts);
    honeyindexes_forsugar.push_back(sugar_index);
    honeyindexes_forsugar = shuffle_vector(honeyindexes_forsugar); // shuffles the sugarindex
    for (int i = 0; i < honeyindexes_forsugar.size(); i++)
    {
        sugarvector.push_back(honeyindexes_forsugar[i]);
    }
    */

    std::vector<std::vector<std::string> > honeylist(num_honeyaccounts);
    honeylist = gen_honeylist(sugarvector, num_honeyaccounts, index_basket);

    shuffle_vector(honeylist);
    shuffle_vector(index_basket);

    // write to F1
    for (int i = 0; i < honeylist.size(); i++)
    {
        if (userindex.is_open())
        {
            std::vector<std::string> tempvector = honeylist[i];
            userindex << tempvector[0] << ","; // write username to file
            for (int j = num_honeywords + 1; j < tempvector.size(); j++)
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

    // write to F2
    for (int i = 0; i < honeylist.size(); i++)
    {
        if (indexpassword.is_open())
        {
            std::vector<std::string> tempvector = honeylist[i];
            /// need to find the sugar index from the honeylist
            tempvector.erase(tempvector.begin()); // pop username from front for simpler iterating

            if (std::find(tempvector.begin(), tempvector.end(), sugarword) != tempvector.end())
            {

                for (int y = 0; y < tempvector.size(); y++)
                {
                    if (tempvector[y] == sugarword)
                    {
                        tempvector.erase(tempvector.begin() + y);
                    }
                    if (tempvector[y] == sugar_index)
                    {
                        tempvector.erase(tempvector.begin() + y);
                    }
                }

                indexpassword << sugar_index << "," << sugarword << "\n";
                //std::string filler_hw = pswd + rand_digit(); take a tail
                //indexpassword << rand_digit() << "," << filler_hw << "\n";
            }

            // else write honey index and honeyword to file
            for (int x = num_honeywords + 1; x < tempvector.size(); x++)
            {
                int temp_rand_digit = rand_digit() % index_basket.size() + 1;
                indexpassword << index_basket[temp_rand_digit] << ",";
                indexpassword << tempvector[x - num_honeywords] << "\n";
            } 
        }
        else
        {
            std::cout << "Error opening userindex file \n";
            return 1;
        }
    }
    indexpassword.close();
}

bool check_file(std::string filename, std::string username)
{
    int offset = 0;
    std::string line;
    std::ifstream Myfile;
    Myfile.open(filename);

    if (Myfile.is_open())
    {
        while (getline(Myfile, line))
        {
            std::stringstream ss(line);
            std::string temp;

            std::vector<std::string> honeyvector;
            while (std::getline(ss, temp, ','))
            {
                honeyvector.push_back(temp);
            }
            if (honeyvector[0] == username)
            {
                return true;
            }
        }
    }
    Myfile.close();
    return false;
}

std::vector<std::string> get_honeyindex(std::string filename, std::string username)
{
    int offset = 0;
    std::string line;
    std::ifstream Myfile;
    Myfile.open(filename, std::ios_base::in);
    std::vector<std::string> fail;
    if (Myfile.is_open())
    {
        while (getline(Myfile, line))
        {
            std::stringstream ss(line);
            std::string temp;

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
    }
    Myfile.close();
    return fail;
}

int check_index(std::string filename, std::vector<std::string> indexpassword)
{

    int offset = 0;
    std::string line;
    std::ifstream Myfile;
    Myfile.open(filename, std::ios_base::in);

    if (Myfile.is_open())
    {
        while (getline(Myfile, line))
        {
            std::stringstream ss(line);
            std::string temp;

            std::vector<std::string> honeyvector;

            while (std::getline(ss, temp, ','))
            {
                honeyvector.push_back(temp);
            }

            if (honeyvector[1] == indexpassword[1]) // check passwords (hash later)
            {
                if (honeyvector[0] == indexpassword[0])
                {
                    return 1;
                }
                else
                {
                    return 2; // honeyword alert
                }
            }
        }
    }
    Myfile.close();
    return 0; //deny login right away
}

std::string check_honeycheck(std::string filename, std::vector<std::string> indexusername)
{
    int offset = 0;
    std::string line;
    std::ifstream Myfile;
    Myfile.open(filename, std::ios_base::in);
    std::string success = "Access Granted!";
    std::string fail = "Honeyword Alert";
    if (Myfile.is_open())
    {
        while (getline(Myfile, line))
        {
            std::stringstream ss(line);
            std::string temp;
            std::vector<std::string> honeyvector;
            while (std::getline(ss, temp, ','))
            {
                honeyvector.push_back(temp);
            }

            if (honeyvector[0] == indexusername[0] && honeyvector[1] == indexusername[1])
            {
                return success;
            }
        }
    }
    Myfile.close();
    return fail;
}

//////////////// main function
int main()
{
    srand((unsigned)time(NULL));

    std::string userindex_fn = "userindex.txt";
    std::string indexpassword_fn = "indexpassword.txt";
    std::string honeychecker_fn = "honeychecker.txt";

    std::ofstream userindex(userindex_fn, std::ios::app);         // F1
    std::ofstream indexpassword(indexpassword_fn, std::ios::app); // F2
    std::ofstream honeychecker("honeychecker.txt", std::ios::app);

    std::ifstream readuserindex(userindex_fn, std::ios_base::in);

    int ret = 0;
    int option = 0;            // chage back to 0
    int num_honeywords = 6;    // this can be modified
    int num_honeyaccounts = 6; // this too
    std::string sugarword = "";
    int sugartail = rand_digit();
    std::cout << "Press 1 to create account, 2 to login, 3 to delete account \n";
    std::cin >> option;

    if (option == 1)
    {
        std::cout << "Enter a username: \n";
        std::string username = ""; // change later
        std::cin >> username;
        if ((ret = check_file(userindex_fn, username)) == 1)
        {
            std::cout << "Error username already exists \n";
            return 1;
        }
        else
        {

            std::cout << "Enter a password between 8 and 12 characters in length \n";
            //std::string sugar = "";
            std::cin >> sugarword;

            while (sugarword.length() < 8 || sugarword.length() > 12)
            {
                std::cout << "Invalid number of characters. Please enter a password between 8 and 12 characters in length \n";
                std::cin >> sugarword;
            }

            // take a tail
            //sugarword = pswd + sugartail);            //std::cout << "Your new password is: " << sugarword << "\n";
            create_account(userindex, indexpassword, honeychecker, username, sugarword, num_honeywords, num_honeyaccounts);
        }
    }

    if (option == 2)
    {
        std::cout << "Enter your username: \n";
        std::string username = "username"; // change later
        std::cin >> username;
        if ((ret = check_file(userindex_fn, username)) == 1)
        {

            std::cout << "Enter your password \n";
            std::string pswd = "";
            std::cin >> pswd;

            std::vector<std::string> userhoneyindex = get_honeyindex(userindex_fn, username);
            userhoneyindex.erase(userhoneyindex.begin()); // pop off the username

            for (int i = 0; i < userhoneyindex.size(); i++)
            {
                std::vector<std::string> temp_vect;
                temp_vect.push_back(userhoneyindex[i]);
                temp_vect.push_back(pswd);
                ret = check_index(indexpassword_fn, temp_vect); // <index,username>

                if (ret == 0)
                {
                    std::cout << "Incorrect password\n";
                    return 0;
                }

                if (ret == 1)
                {

                    // just a formatting shuffle to get <index, username>
                    temp_vect.pop_back();
                    temp_vect.push_back(username);
                    temp_vect.push_back(temp_vect[0]);
                    temp_vect.erase(temp_vect.begin());

                    std::string access = check_honeycheck(honeychecker_fn, temp_vect);
                    std::cout << access << "\n";
                    return 0;
                }

                if (ret == 2)
                {
                    std::cout << "Honeypot Alert\n";
                    return 0;
                }
            }
        }

        else
        {
            std::cout << "Username not in system \n";
            return 1;
        }
    }
    return 0;
}
