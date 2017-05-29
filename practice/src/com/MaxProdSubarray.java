package com;
import java.io.*;

/**
 * Created by dwipam on 5/28/17.
 */
public class MaxProdSubarray {
    public int maxProdSubarray(int[] arr) {
        int maxSoFar = 1;
        int minSoFar = 1;
        int max = 1;
        for (int i : arr) {
            if (i > 0) {
                maxSoFar = Math.max(i * maxSoFar, 1);
                minSoFar = Math.min(i * minSoFar, 1);
            } else if (i == 0) {
                maxSoFar = 1;
                minSoFar = 1;
            } else {
                int temp = maxSoFar;
                maxSoFar = Math.max(minSoFar*i,1);
                minSoFar = temp*i;
            }
            if (max < maxSoFar){
                max = maxSoFar;
            }

        }
        return max;
    }
    public static void main(String args[]) throws Exception{
        MaxProdSubarray _ = new MaxProdSubarray();
        System.out.print(_.maxProdSubarray(new int[] {1, -2, -3, 0, 7, -8, -2}));
    }
}
