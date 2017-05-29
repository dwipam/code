package com;

/**
 * Created by dwipam on 5/28/17.
 */
// Approximate Sum.
public class NearestSum {
    public String nearestSum(int[] arr, int x){
        int sum = 0; int index1 = 0; int index2 = 0; int j = 0; int best = Integer.MAX_VALUE;
        int i = 0;
        while(i<arr.length){
            sum+=arr[i];
            if (sum > x && Math.abs(sum-x) > best){
                sum-=arr[j];
                j++;

            }
            if (Math.abs(sum-x) < best){
                best = Math.abs(sum-x);
                index1 = j;index2 = i;
            }
            i++;

        }
         j = arr.length-1; sum = 0;
        for(i = arr.length-1; i>=0;i--){
            sum+=arr[i];
            if (sum > x && Math.abs(sum-x) > best){
                sum-=arr[j];
                j--;

            }
            if (Math.abs(sum-x) < best){
                best = Math.abs(sum-x);
                index2 = j;index1 = i;
            }
        }
        return Integer.toString(index1)+" to "+Integer.toString(index2);
    }
    public static void main(String args[]) throws Exception{
        NearestSum _ = new NearestSum();
        int[] arr = {1,2,5,0,4,100};
        System.out.print(_.nearestSum(arr,8));
    }
}
