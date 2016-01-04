import java.util.Scanner;

public class LCS {
    
    public static void main(String[] args) {
    	Scanner in=new Scanner(System.in);
        int i,j;
        
        System.out.print("Enter the first String  : ");
        String X = in.next();
         
        System.out.print("Enter the Second String : ");
        String Y = in.next();
        int p = X.length();
        int q = Y.length();
        
        int[][] cache = new int[p+1][q+1];
        int[][] direction= new int[p+1][q+1];
	
        
        for (i = 0; i <= p; i++) {
            cache[i][0] = 0;
        }
	
        
        for (j = 0; j <= q; j++) {
            cache[0][j] = 0;
        }
        
        
        for (i = 1; i <= p; i++) {
            for (j = 1; j <= q; j++) {
                if (X.charAt(i-1) == Y.charAt(j-1)) {
                    cache[i][j]=cache[i-1][j-1]+1;
                    direction[i][j]=1;  
                }
                else if (cache[i-1][j]>=cache[i][j-1]) {
                    cache[i][j]=cache[i-1][j];
                    direction[i][j] = 2;  
                }
                else {
                    cache[i][j]=cache[i][j-1];     
                    direction[i][j]=3;   
                }
            }
        }
        
        String lcs = new String();
        i=p;
        j=q;
        while (i!=0 && j!=0) {
            if (direction[i][j] ==1) {   
                lcs =X.charAt(i-1) + lcs;
                i = i - 1;
                j = j - 1;
            }
            if (direction[i][j] == 2) {  
                i = i - 1;
            }
            if (direction[i][j] == 3) {  
                j = j - 1;
            }
        }
        
        
        System.out.println("The LCS is " + lcs);
        
    }
}