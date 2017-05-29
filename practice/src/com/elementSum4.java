package com;

/**
 * Created by dwipam on 5/28/17.
 */
public class elementSum4 {
    public String elemtsSum4(int[] arr,int x){
        for(int i=0;i<arr.length;i++){
            for(int j=i+1;i<arr.length;j++){
                int k=j+1; int l = arr.length-1;
                while(k<l){
                    if (arr[i] + arr[j] + arr[k] + arr[l] == x){
                        return Integer.toString(arr[i]) + " "+Integer.toString(arr[j])
                                +" "+Integer.toString(arr[k])+" "+Integer.toString(arr[l]);
                    }
                    int y = arr[i] + arr[j] + arr[k] + arr[l];
                    if (y < x) k++;
                    if(y>x) l--;
                }
            }
        }
        return "Not Found";
    }
    public static void main(String args[])throws Exception{
        elementSum4 _ = new elementSum4();
        System.out.print(_.elemtsSum4(new int[]{1,2,3,4,5,6},14));
    }
}
