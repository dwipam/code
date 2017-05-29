package com;

import java.util.HashMap;

/**
 * Created by dwipam on 5/28/17.
 */
public class findDiff2 {
    public String findPair(int[] arr, int x){
        HashMap<Integer, Integer> diff = new HashMap<Integer, Integer>();
        for (int i: arr){
            if (diff.containsKey(i)) return diff.get(i).toString() +", "+i;
            else diff.put(Math.abs(x-i),i); diff.put(x+i,i);
        }
        return "Not found";
    }
    public static void main(String args[]) throws Exception{
        findDiff2 _ = new findDiff2();
        System.out.print(_.findPair(new int[] {1, 8, 30, 100, 40},60));
    }
}
