#include<bits/stdc++.h>
using namespace std;
 
int calculateMex(unordered_set<int> Set){
    int Mex = 0;
 
    while (Set.find(Mex) != Set.end())
        Mex++;
 
    return (Mex);
}


int calculateGrundy (int n){
    if (n == 0 || n == 1 || n == 2){
        return (0);
    }

    unordered_set<int> Set; // A Hash Table

    Set.insert(calculateGrundy(n-2));

    for (int k=0; k< n-1; k++){ 
        Set.insert(calculateGrundy(k-2)^calculateGrundy(n-k-1));

    }
    return (calculateMex(Set));
}

int main(){

    int n = 1;
    cout << calculateGrundy(10);
    return 0;
}