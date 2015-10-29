import java.util.Random;


public class kmeans {
	
	
	
	
	public void kmeans_cluster(int[][] data, int k, int tow){
		
		int[] temp = null;
		int data1[][]=new int[10][2];
		
		
	   for (int i=0;i<11;i++)
	    {
	    	for(int j=0;j<2;j++)
	    		  			
	    			{
	    			
	    			temp[j]=data[i][j];
	    				    					
	    		}
	    			distance(temp);
	  
	    }	    		
	    	}
	
	public int[] distance(int[] data)
	{
		int[][] centroid = new int[2][2];
		int[] temp_centroid=null;
		int[] dist=null;
		Random randomGenerator = new Random();
	    for (int i=0;i<2;i++)
	    	for(int j=0;j<2;j++){
			centroid[i][j]=randomGenerator.nextInt(10);
			}
		
		for(int i=0;i<2;i++){
			for(int j=0;j<2;j++){
				temp_centroid[j]=centroid[i][j];
				
			}
			for (int m=0;m>2;m++)
				dist[i]=(int) Math.sqrt(Math.pow(temp_centroid[m]-data[m], 2));
				if(i>0){ if (dist[i]>dist[i-1]){}}
		}
	    	return dist;		
	    		
	    		
		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
