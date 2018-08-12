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
        honeyusernamevector.push_back(honeypassword);
        int temp_rand_digit = rand_digit() % index_basket.size() + 1;
        std::string honeysugarindex = index_basket[temp_rand_digit];
        std::cout << "HONEYSUGARINDEX: " << honeysugarindex << "\n";
        

        std::vector<std::string> honeyindexvector;
        honeyindexvector = gen_var_randoms(num_honeyaccounts);
        honeyindexvector.push_back(honeysugarindex);
        honeyindexvector = shuffle_vector(honeyindexvector);
        std::cout << "SIZE :" << honeyindexvector.size() << "\n";
        std::cout << "HONEYSUGAR VECTOR :"; 
        print_vector(honeyindexvector);
        for (int i = 0; i < honeyindexvector.size(); i++){
            honeyusernamevector.push_back(honeyindexvector[i]);
            std::cout << honeyusernamevector[i] << "\n";
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

std::vector<std::string> create_account(std::ofstream &userindex, std::ofstream &indexpassword, std::ofstream &honeychecker, std::string username, std::string sugarword, int num_honeywords, int num_honeyaccounts, std::vector<std::string> honeypot)
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
    std::string sugar_index = index_basket.back(); // make sugar index unique
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
    
    
    std::vector<std::vector<std::string> > honeylist;
    std::vector<std::string> honey_index;

    for (int i = 0; i < num_honeyaccounts; i++)
    {
        std::vector<std::string> honeyusernamevector;
        std::string genusername = rand_username();
        honeyusernamevector.push_back(genusername);
        honeypot.push_back(genusername); // add to known honeypot
        std::string honeypassword = rand_username();
        honeyusernamevector.push_back(honeypassword);
        
        int temp_rand_digit = rand_digit() % index_basket.size() + 1;
        std::string honeysugarindex = index_basket[temp_rand_digit];
        //std::cout << "HONEYSUGARINDEX: " << honeysugarindex << "\n";
        honeyusernamevector.push_back(honeysugarindex);

        honeylist.push_back(honeyusernamevector);
        print_vector(honeyusernamevector);
    }
    honeylist.push_back(sugarvector);
    honeylist = shuffle_vector(honeylist);

    // write to F2
    for (int i = 0; i < honeylist.size(); i++)
    {
        if (indexpassword.is_open())
        {
            std::vector<std::string> tempvector = honeylist[i];
            if (tempvector[0] == username){
                indexpassword << sugar_index << ",";
                indexpassword << sugarword << "\n";
            }
            else{
            indexpassword << tempvector[2] << ","; // write sugar/sugarhoney index to file
            indexpassword << tempvector[1] << "\n"; // write sugar/honey word to file
            }
        }
        else
        {
            std::cout << "Error opening userindex file \n";
        }
    }
    indexpassword.close();
    // write to f1
    if (userindex.is_open()){
    for (int i = 0 ; i < honeylist.size(); i++){
        
        std::vector<std::string> uitempvector = honeylist[i];
        if (uitempvector[0] == username){
            userindex << uitempvector[0] << ",";
            for (int j = 2; j < uitempvector.size(); j++){
                userindex << uitempvector[j] << ",";
            }
        }
        else {
        userindex << uitempvector[0] << ",";
        std::vector<std::string> honeyindexvector;
        honeyindexvector = gen_var_randoms(num_honeyaccounts);
        honeyindexvector.push_back(uitempvector[2]);
        honeyindexvector = shuffle_vector(honeyindexvector);
        for (int j = 0; j < honeyindexvector.size(); j++){
            userindex << honeyindexvector[j] << ",";
        }
        }
        userindex << "\n";
        }
        }
         else {
            std::cout << "Error opening userindex file \n";
        } 
    userindex.close();

    return honeypot;

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
    std::string fail = "Honeycheck Fail";
    std::vector<std::string> honeyvectorz;
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
                //return success;
            }
        }
    }
   
    Myfile.close();
    return fail;
}
std::string update_honeycheck(std::string filename, std::vector<std::string> indexusername)
{
        print_vector(indexusername);
    int offset = 0;
    std::string line;
    std::fstream Myfile;
    Myfile.open(filename, std::ios::in);
    std::string success = "Password Deleted!";
    std::string fail = "Error";
    std::vector<std::string> writevector;
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
            print_vector(honeyvector);
            if (honeyvector[1] != indexusername[0])
            {
                writevector.push_back(honeyvector[0]);
                writevector.push_back(honeyvector[1]);
            } 
        }
    }
    Myfile.close();
    print_vector(writevector);
    Myfile.open(filename, std::ios::out);
    for (int i = 0; i < writevector.size(); i++) {
        if (i % 2 == 0){
                Myfile << writevector[i] << ",";
        }
        else{
                Myfile << writevector[i] << "\n";
        }
            }
            Myfile.close();
            return success;
            
}
std::vector<std::string> read_honeypot(std::string filename){
    int offset = 0;
    std::string line;
    std::ifstream Myfile;
    Myfile.open(filename, std::ios_base::in);
    std::vector<std::string> honeyvector;
    if (Myfile.is_open())
    {
        while (getline(Myfile, line))
        {
            std::stringstream ss(line);
            std::string temp;
            
            while (std::getline(ss, temp)) //, ','))
            {
                honeyvector.push_back(temp);
            }
        }
    }
        else {
            std::cout << "Error opening file. ";
        }
    Myfile.close();
    return honeyvector;
}
//////////////// main function
int main()
{
    srand((unsigned)time(NULL));

    std::string userindex_fn = "userindex.txt";
    std::string indexpassword_fn = "indexpassword.txt";
    std::string honeychecker_fn = "honeychecker.txt";
    std::string honeypot_fn = "rockyou.txt";
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
    

    std::vector<std::string> honeypot = read_honeypot(honeypot_fn);
    //print_vector(honeypot);
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
            for (int j = 0; j < honeypot.size(); j++){
                        if (username == honeypot[j]){
                            std::cout << "Please pick a 'less sticky' username.\n";
                            return 1;
                        }
            }

            std::cout << "Enter a password between 8 and 12 characters in length \n";
            std::cin >> sugarword;

            while (sugarword.length() < 8 || sugarword.length() > 12)
            {
                std::cout << "Invalid number of characters. Please enter a password between 8 and 12 characters in length \n";
                std::cin >> sugarword;
            }

            create_account(userindex, indexpassword, honeychecker, username, sugarword, num_honeywords, num_honeyaccounts, honeypot);
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

                

                if (ret == 1)
                {
                    for (int j = 0; j < honeypot.size(); j++){
                        if (username == honeypot[j]){
                            std::cout << "Honeypot Alert\n";
                            return 0;
                        }
                    }
                    //check honeypot acc here
                    // just a formatting shuffle to get <index, username>
                    temp_vect.pop_back();
                    temp_vect.push_back(temp_vect[0]);
                    temp_vect.push_back(username);
                    
                    temp_vect.erase(temp_vect.begin());

                    std::string access = check_honeycheck(honeychecker_fn, temp_vect);
                    std::cout << access << "\n";
                    return 0;
                }
               
            }
            if (ret == 0)
                {
                    std::cout << "Incorrect password\n";
                }
        }

        else
        {
            std::cout << "Username not in system \n";
            return 1;
        }
    }

     if (option == 3)
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
                
                // just a formatting shuffle to get <index, username>
                    temp_vect.pop_back();
                    temp_vect.push_back(temp_vect[0]);
                    temp_vect.push_back(username);
                    
                    temp_vect.erase(temp_vect.begin());

                update_honeycheck(honeychecker_fn, temp_vect); // <index,username>

                /*
                if (ret == 1)
                {
                    for (int j = 0; j < honeypot.size(); j++){
                        if (username == honeypot[j]){
                            std::cout << "Honeypot Alert\n";
                            return 0;
                        }
                    }
                    //check honeypot acc here
                    // just a formatting shuffle to get <index, username>
                    temp_vect.pop_back();
                    temp_vect.push_back(temp_vect[0]);
                    temp_vect.push_back(username);
                    
                    temp_vect.erase(temp_vect.begin());

                    std::string access = check_honeycheck(honeychecker_fn, temp_vect);
                    std::cout << access << "\n";
                    */
                    return 0;
                }
               
            }
            if (ret == 0)
                {
                    std::cout << "Incorrect password\n";
                }

        else
        {
            std::cout << "Username not in system \n";
            return 1;
        }
    
    }

    return 0;
}

