#include <iostream>
#include <vector>
#include <algorithm>
#include <random>

int hashone(int a, int b, int c, int x)
{
    int output = ((a * x + b) % c) % 100;
    return output;
}

int hashtwo(int a, int b, int c, int x)
{
    int output = ((b * x + a) % c) % 100;
    return output;
}

int hashthree(int a, int b, int c, int x)
{
    int output = ((c * x + b) % a) % 100;
    return output;
}

int hashfour(int a, int b, int c, int x)
{
    int output = ((b * x + c) % a) % 100;
    return output;
}

int hashfive(int a, int b, int c, int x)
{
    int output = ((c * x + a) % b) % 100;
    return output;
}

// Run all 3 on an an element and store in a vector which can be compared to another vector
std::vector<int> triplehash(int a, int b, int c, int e)
{
    int compareone;
    int comparetwo;
    int comparethree;
    std::vector<int> cvector;

    compareone = hashone(a, b, c, e);
    comparetwo = hashtwo(a, b, c, e);
    comparethree = hashthree(a, b, c, e);

    cvector.push_back(compareone);
    cvector.push_back(comparetwo);
    cvector.push_back(comparethree);
    return cvector;
}

// Run all 5 on an an element and store in a vector which can be compared to another vector
std::vector<int> quintuplehash(int a, int b, int c, int e)
{
    int compareone;
    int comparetwo;
    int comparethree;
    int comparefour;
    int comparefive;

    std::vector<int> cvector;

    compareone = hashone(a, b, c, e);
    comparetwo = hashtwo(a, b, c, e);
    comparethree = hashthree(a, b, c, e);
    comparefour = hashfour(a, b, c, e);
    comparefive = hashfive(a, b, c, e);

    cvector.push_back(compareone);
    cvector.push_back(comparetwo);
    cvector.push_back(comparethree);
    cvector.push_back(comparefour);
    cvector.push_back(comparefive);

    return cvector;
}

// Delete any duplicates from a vector
std::vector<int> delete_dupes(std::vector<int> collisions){
    sort( collisions.begin(), collisions.end() );
            collisions.erase( unique( collisions.begin(), collisions.end() ), collisions.end() );
    return collisions;
}



// 3-hash Generate a vector from hashing an element in the query set then generate a vector from hashing an element for every element in the S set.
// If any number is in both vectors a part or all of a collision has occured.
std::vector<int> investigatefp(std::vector<int> s, int fp, int a, int b, int c)
{
    int e;

    std::vector<int> collisions;

    int count = 0;

    std::vector<int> fpvector = triplehash(a, b, c, fp); // Hash the false positive that was found

    for (int i = 0; i < s.size(); i++)
    {
        e = s[i];

        std::vector<int> svector = triplehash(a, b, c, e); // Hash an element from S

        for (int j = 0; j < svector.size(); j++) // Iterate over the svector to check for any intersections
        {
            if (std::find(fpvector.begin(), fpvector.end(), svector[j]) != fpvector.end())
            {
                collisions.push_back(svector[j]);
                count++;
            }
        }

        if (count == 3)
        {   // Anytime two or more of the hashes from an e in S produced the same value results,
            // a duplicate e would get added to the collision vector. This removes duplicates.  
            sort( collisions.begin(), collisions.end() ); 
            collisions.erase( unique( collisions.begin(), collisions.end() ), collisions.end() );
            return collisions;
        }
    }
    sort( collisions.begin(), collisions.end() );
    collisions.erase( unique( collisions.begin(), collisions.end() ), collisions.end() );
    return collisions; 

}

// 5-hash Generate a vector from hashing an element in the query set then generate a vector from hashing an element for every element in the S set.
// If any number is in both vectors a part or all of a collision has occured.
std::vector<int> investigatefpfive(std::vector<int> s, int fp, int a, int b, int c)
{
    int e;

    std::vector<int> collisions;
    std::vector<int> tempvector;
    int count = 0;

    std::vector<int> fpvector = quintuplehash(a, b, c, fp); // Hash the false positive that was found
    /*
    printf("QUERY NUMBER: %d FPVECTOR: [ ", fp);
    for (int i = 0; i < fpvector.size(); i++)
    {
        printf("%d ", fpvector[i]);
    }
    printf("]\n");
    */
    for (int i = 0; i < s.size(); i++)
    {
        e = s[i];

        std::vector<int> svector = quintuplehash(a, b, c, e); // Hash an element from S

        std::set_intersection(fpvector.begin(), fpvector.end(), svector.begin(), svector.end(),
                                                                std::back_inserter(tempvector));
        // Merge the vectors
        collisions.insert( collisions.end(), tempvector.begin(), tempvector.end() );
        // Delete duplicates
        collisions = delete_dupes(collisions);

        if (collisions.size() > 3){
            while (collisions.size() < 3){
                collisions.pop_back();
            }
            return collisions;
        }
        else if (collisions.size() == 3){
            return collisions;
        }
        /*
   // printf("SVECTOR %d: [ ", i);
    /*for (int i = 0; i < svector.size(); i++)
    {
        printf("%d ", svector[i]);
    }
    printf("]\n");
    
       // for (int j = 0; j < svector.size(); j++) // Iterate over the svector to check for any intersections
        //{
           // co
            if (std::find(fpvector.begin(), fpvector.end(), svector[j]) != fpvector.end())
            {
                collisions.push_back(svector[e]);
                count++;
            }
            else {
                printf("S ELEMENT %d IS UNIQUE \n", e);
            }
        //}

        if (count == 3)
        {
            sort( collisions.begin(), collisions.end() );
            collisions.erase( unique( collisions.begin(), collisions.end() ), collisions.end() );
           return collisions;
        }
        */
    }
    
    return collisions; 

}



 // Use 3 hash functions
void three_bloom(){
    printf("Three hash bloom filter \n");
 unsigned seed = std::chrono::system_clock::now().time_since_epoch().count(); // RNG seed
    std::default_random_engine rng(seed);

    int a = 3298;
    int b = 2390;
    int c = 10203;

    std::vector<int> Universe; // U
    std::vector<int> S;        // set of old passwords I think

    for (int i = 0; i < 100; i++)
    {
        Universe.push_back(i);
    }

    std::shuffle(Universe.begin(), Universe.end(), rng); // Randomly shuffles the elements in the vector

    printf("S is: [");
    for (int i = 0; i < 25; i++)
    {
        int temp = Universe[i];
        Universe.erase(Universe.begin() + i); // Creates the query list
        S.push_back(temp);
        printf("%d ", S[i]);
    }
    printf("] \n");

    int e;    // A password from S
    int kone; // Outputs from hashing e
    int ktwo;
    int kthree;
    int bfilter[100] = {0}; // Initialize bloom filter to 0

    for (int i = 0; i < S.size(); i++)
    {
        e = S[i]; // Select a password
        // Hash the password through each hash function
        kone = hashone(a, b, c, e);
        ktwo = hashtwo(a, b, c, e);
        kthree = hashthree(a, b, c, e);
        // Set the bloomfilter equal to one at the positions
        bfilter[kone] = 1;
        bfilter[ktwo] = 1;
        bfilter[kthree] = 1;
    }

    printf("Bloom Filter: [ ");
    for (int i = 0; i < 100; i++)
    {
        printf("%d ", bfilter[i]);
    }
    printf("]");

    printf("\nQuery Set: [ ");
    for (int i = 0; i < Universe.size(); i++)
    {
        printf("%d ", Universe[i]);
    }
    printf("]");

    int q;             // Query element
    int truenegative;  // Number of queries not in the set
    int falsepositive; // Number of queries that are in the set that shouldn't be

    for (int i = 0; i < Universe.size(); i++)
    {
        q = Universe[i]; // Select a query
        // Hash it through each hash function
        kone = hashone(a, b, c, q);
        ktwo = hashtwo(a, b, c, q);
        kthree = hashthree(a, b, c, q);
        
        if (bfilter[kone] == 0 || bfilter[ktwo] == 0 || bfilter[kthree] == 0)
        {
            truenegative++;
        }

        if (bfilter[kone] == 1 && bfilter[ktwo] == 1 && bfilter[kthree] == 1)
        {
            printf("\n False Positive at query %d.", q);
            falsepositive++;
            printf(" Collision with elements in S at: ");
            std::vector<int> fpvector = investigatefp(S, q, a, b, c);
            for (int j = 0; j < fpvector.size(); j++)
            {
                printf("%d ", fpvector[j]);
            }
        }
    }

    double fprate = double(falsepositive) / truenegative;
    printf("\n True Negatives: %d \n False Positives: %d \n False Positive Rate: %f \n",
           truenegative, falsepositive, fprate);
}



// Use five hash functions
void five_bloom(){

    printf("\nFive hash bloom filter \n");
    unsigned seed = std::chrono::system_clock::now().time_since_epoch().count(); // RNG seed
    std::default_random_engine rng(seed);

    int a = 3298;
    int b = 2390;
    int c = 10203;

    std::vector<int> Universef; // U
    std::vector<int> Sf;        // set of old passwords I think

    for (int i = 0; i < 100; i++)
    {
        Universef.push_back(i);
    }

    std::shuffle(Universef.begin(), Universef.end(), rng); // Randomly shuffles the elements in the vector

    printf("S is: [");
    for (int i = 0; i < 25; i++)
    {
        int temp = Universef[i];
        Universef.erase(Universef.begin() + i); // Creates the query list
        Sf.push_back(temp);
        printf("%d ", Sf[i]);
    }
    printf("] \n");

    int e;    // A password from S
    int kone; // Outputs from hashing e
    int ktwo;
    int kthree;
    int kfour;
    int kfive;

    int bfilter[100] = {0}; // Initialize bloom filter to 0

    for (int i = 0; i < Sf.size(); i++)
    {
        e = Sf[i]; // Select a password
        // Hash the password through each hash function
        kone = hashone(a, b, c, e);
        ktwo = hashtwo(a, b, c, e);
        kthree = hashthree(a, b, c, e);
        kfour = hashfour(a, b, c, e);
        kfive = hashfive(a, b, c, e);

        // Set the bloomfilter equal to one at the positions
        bfilter[kone] = 1;
        bfilter[ktwo] = 1;
        bfilter[kthree] = 1;
        bfilter[kfour] = 1;
        bfilter[kfive] = 1;
    }

    printf("Bloom Filter: [ ");
    for (int i = 0; i < 100; i++)
    {
        printf("%d ", bfilter[i]);
    }
    printf("]");

    printf("\nQuery Set: [ ");

    for (int i = 0; i < Universef.size(); i++)
    {
        printf("%d ", Universef[i]);
    }
    printf("]");

    int q;             // Query element
    int truenegative;  // Number of queries not in the set
    int falsepositive; // Number of queries that are in the set that shouldn't be

    for (int i = 0; i < Universef.size(); i++)
    {
        q = Universef[i]; // Select a query
        // Hash it through each hash function
        kone = hashone(a, b, c, q);
        ktwo = hashtwo(a, b, c, q);
        kthree = hashthree(a, b, c, q);
        kfour = hashfour(a,b,c,q);
        kfive = hashfive(a,b,c,q);
        
        if (bfilter[kone] == 0 || bfilter[ktwo] == 0 || bfilter[kthree] == 0 || bfilter[kfour] == 0 || bfilter[kfive] == 0)
        {
            truenegative++;
        }

        if (bfilter[kone] == 1 && bfilter[ktwo] == 1 && bfilter[kthree] == 1 && bfilter[kfour] == 1 && bfilter[kfive] == 1)
        {
            printf("\n False Positive at query %d.", q);
            falsepositive++;
            printf(" Collision with elements in S at: ");
            std::vector<int> fpvector = investigatefpfive(Sf, q, a, b, c);
            for (int j = 0; j < fpvector.size(); j++)
            {
                printf("%d ", fpvector[j]);
            }
        }
    }

    double fprate = double(falsepositive) / truenegative;
    printf("\n True Negatives: %d \n False Positives: %d \n False Positive Rate: %f\n",
           truenegative, falsepositive, fprate);
}

int main()
{
    three_bloom();
    five_bloom();
    return 0;
}
