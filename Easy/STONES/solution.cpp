#include <iostream>
using namespace std;

int main() {
    int t,sum=0;
    cin>>t;
    while(t--){
        string j,s;
        cin>>j>>s;
        for (int m=0;m<=j.size()-1;++m){
            for (int i=0;i<=s.size()-1;++i){
                if (s[i]==j[m]){
                    sum=sum+1;
                    s[i]=0;
                }
                
            }
        }
        cout<<sum<<endl;
        sum=0;
    }
	return 0;
}