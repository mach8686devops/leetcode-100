// 俄罗斯套娃信封

class Solution{
    public int maxEnvelopes(int[][] envelopes){
        int n = envelopes.length;
        Arrays.sort(envelopes, new Comparator<int[]>()
        {
            public int compare(int[] a,int[] b){
                return a[0]==b[0]?
                    b[1]-a[1]:a[0]-b[0];
            }
        }
        );
        int[] height=new int[n];
        for (int i=0;i<n;i++)
            height[i]=envelopes[i][1];

        return lengthOfLIS(height);
    }

    public int lengthOfLIS(int[] nums) {
        int[] top=new int[nums.length];
        int piles=0;
        for (int i=0;i<nums.length;i++){
            int poker=nums[i];
            int left=0,right=piles;
            while (left<right){
                int mid=(left+right)/2;
                if (top[mid]>poker){
                    right=mid;
                }else if(top[mid]<poker){
                    left=mid+1;
                }else{
                    right=mid;
                }

            }
            if (left==piles) piles++;
            top[left]=poker;
        }
        return piles;
    }
}