class Solution {
public:
    bool isPalindrome(int x) {
        string str = to_string(x);
        string rstr = to_string(x);
        reverse(rstr.begin(),rstr.end());
        if(str==rstr){
            return true;
        }
        return false;
    }
};
