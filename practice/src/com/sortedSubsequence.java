package com;

/**
 * Created by dwipam on 5/27/17.
 */
public class sortedSubsequence {
    public void sortedSequence(int[] numbers){
        int[] smaller = new int[numbers.length];
        smaller[0] = -1; int[] larger = new int[numbers.length]; larger[numbers.length-1] = -1;
        int minIndex = 0 ; int maxIndex = numbers.length-1;
        for(int i= 1; i<numbers.length;i++){
            if (numbers[i] <= numbers[minIndex]){
                minIndex = i;
                smaller[i] = -1;
            }
            else
                smaller[i] = minIndex;
        }
        for (int i = numbers.length-2; i >= 0; i--){
            if(numbers[i] > numbers[maxIndex]){
                maxIndex = i;
                larger[i] = -1;
            }
            else{
                larger[i] = maxIndex;
            }
        }
        for(int i = 0; i<numbers.length;i++){
            if (smaller[i] != -1 && larger[i] != -1) {
                System.out.println(numbers[smaller[i]] + " " + numbers[i] + " " + numbers[larger[i]]);
                return;
            }
        }
        System.out.print("No such triplet");
    }
    public static void main(String args[]) throws Exception{
        sortedSubsequence _ = new sortedSubsequence();
        int[] numbers = {12, 11, 10, 5, 6, 2, 30};
        _.sortedSequence(numbers);
    }
}
