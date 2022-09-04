#include<iostream>
#include<string>
#include<vector>
using namespace std;
int main(){
    vector<int> arr(26, 0);
    string s;
    cin>>s;

    for(int i=0; i<s.size(); i++){
        arr[s[i]-'a']++;
    }
    for(int i=0; i<arr.size(); i++)
        cout << arr[i] << ' ';
    return 0;
}