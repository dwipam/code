package com;

/**
 * Created by dwipam on 5/28/17.
 */
public class Partition {
    public boolean partition(int[] arr, int n, int sum){
        if (sum == 0) return true;
        if (n == 0 && sum != 0) return false;
        if (arr[n-1] > sum) return partition(arr, n-1, sum);

        return partition(arr,n-1,sum) || partition(arr,n-1,sum-arr[n-1]);

    }
    public boolean getPartition(int[] arr){
        int sum = 0;
        for(int i:arr) sum+=i;
        if (sum%2==0) return partition(arr,arr.length,sum/2);
        return false;
    }
    public static void main(String args[])throws Exception{
        Partition _ = new Partition();
        int[] arr = {3, 1, 5, 9, 12};
        System.out.print(_.getPartition(arr));
    }
}
