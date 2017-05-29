package com;

/**
 * Created by dwipam on 5/28/17.
 */
public class replaceGreates {
    public int[] getGreatest(int[] arr, int n){
        int maxSoFar = arr[n-1];
        int temp = 0;
        arr[n-1] = -1;
        for (int i = n-2;i>=0;i--){
            if (maxSoFar < arr[i]){
                temp = arr[i];
                arr[i] = -1;
                maxSoFar = temp;
            }
            else arr[i] = maxSoFar;
            }
        return arr;
        }
    public static void main(String args[]) throws Exception{
        replaceGreates _  = new replaceGreates();
        int[] arr = _.getGreatest(new int[] {2,5,7,1,2,3},6);
        for(int i:arr) System.out.print(i);
    }
    }
