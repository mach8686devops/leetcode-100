class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n=s.size();
        // vector<vector<int>> dp(n, vector<int>(n,0));
        // for (int i=0;i<n;i++)
        //     dp[i][i]=1;
        // for (int i=n-2;i>=0;i--){
        //     for(int j=i+1;j<n;j++){
        //         if (s[i]==s[j])
        //             dp[i][j]=dp[i+1][j-1]+2;
        //         else
        //             dp[i][j]=max(dp[i+1][j],dp[i][j-1]);
        //     }
        // }
        
        // return dp[0][n-1];
        vector<int> dp(n,1);
        for (int i=n-2;i>=0;i--){
            int pre=0;
            for(int j=i+1;j<n;j++){
                int temp=dp[j];
                if (s[i]==s[j])
                    dp[j]=pre+2;
                else
                    dp[j]=max(dp[j],dp[j-1]);
                pre=temp;
            }
        }
        
        return dp[n-1];

    }
};