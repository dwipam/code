import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Timestamp;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.concurrent.TimeUnit;

import org.json.JSONException;
import org.json.JSONObject;
class Route
{
	String stop;
	Long arr;
	Long dep;
	Long diff;
}
public class BetterCode {

	private static ArrayList<Long> t = new ArrayList<Long>();
	private static ArrayList<Long> dif = new ArrayList<Long>();
	private static HashSet<Date>date=new HashSet<Date>();
	private static HashSet<Integer>bus=new HashSet<Integer>();
	private static Map<Date,HashSet<Integer>> busDate=new HashMap<Date,HashSet<Integer>>();
	private static Map<Date,Map<Integer,Map<String,ArrayList<String>>>> ds=new HashMap<Date,Map<Integer,Map<String,ArrayList<String>>>>();
	private static Date commonDate;
	static int flag=1;
	static char c;
	static Scanner in ;
	static PrintWriter out;
	public static void main(String args[]) throws IOException {
		// Scanner 
		in = new Scanner(new File(args[0]));


		PrintWriter pr = new PrintWriter(new FileWriter(new File(args[1])));
		//PrintWriter out,out2,out3,out4,out5,out6;
		//out = new PrintWriter(new BufferedWriter(new FileWriter("F://Bus Data//foo1.csv")));
		in.nextLine();
		while (in.hasNextLine()) {
			String line = in.nextLine();
			String[] parts = splitLine(line);
			BusId_Date_Map(parts);
			final JSONObject obj = mapJson(parts);
			pr.println(obj.toString());
			// Distinct Bus ID's stored in bus HashSet 
			bus.add(Integer.parseInt(parts[5]));
			//mapdatebusid(parts);
			//for(int i=0;i<parts.length;i++)
			//System.out.print(parts[9]+" "+parts[10]+" "+parts[11]);
			//System.out.print(line.substring(0,9)+" ");
			//System.out.println(line.substring(11));
			//System.out.println();
			//pr.println(parts[0]);
		}

		in.close();
		//out.close();

		in = new Scanner(new File(args[0]));
		out = new PrintWriter(new BufferedWriter(new FileWriter("F://Bus Data//foo1.csv")));
		/*out2 = new PrintWriter(new BufferedWriter(new FileWriter("F://Bus Data//foo2.csv")));
		out3 = new PrintWriter(new BufferedWriter(new FileWriter("F://Bus Data//foo3.csv")));
		out4 = new PrintWriter(new BufferedWriter(new FileWriter("F://Bus Data//foo4.csv")));
		out5 = new PrintWriter(new BufferedWriter(new FileWriter("F://Bus Data//foo5.csv")));
		out6 = new PrintWriter(new BufferedWriter(new FileWriter("F://Bus Data//foo6.csv")));*/
		in.nextLine();

		while (in.hasNextLine()) {
			String line = in.nextLine();
			String[] parts = splitLine(line);

			mapdatebusid(parts);

		}
		in.close();
		out.close();
		for(Date d:busDate.keySet())
		{
			//System.out.println(busDate.keySet());
			for(Integer i:busDate.get(d))
			{
				ds.get(d).put(i,null);
			}
		}

		in = new Scanner(new File(args[0]));
		out = new PrintWriter(new BufferedWriter(new FileWriter("F://Bus Data//foo1.csv")));
		in.nextLine();
		// while (in.hasNextLine()) {
		//in.nextLine();
		String line = in.nextLine();
		String[] parts = splitLine(line);

		mapbusshift(parts);//once
		out.println(ds);
		out.println("................................................");
		System.out.println("....................................................");
		c = (char) System.in.read();

		for(int i=0;i<3908;i++)
		{

			line = in.nextLine();
			parts = splitLine(line);
			if(parts[5].equals("657"))
			{

				mapbusshift(parts);//eightth
				out.println(ds);
				out.println("................................................");
				System.out.println("....................................................");
				//c = (char) System.in.read();
			}

		}

		/*for(Date d:ds.keySet())
		{
			for(Integer i:ds.get(d).keySet())
			{
				for(String s:ds.get(d).get(i).keySet())
				{
				System.out.print(d+"    "+i);
				System.out.println();

			//	String s="F://Bus Data//foo"+i+".csv";
				//out = new PrintWriter(new BufferedWriter(new FileWriter("F://Bus Data//foo.csv")));
				out.println("THE VALUES ARE"+d+"  "+i+"   "+s );
				out.println(ds.get(d).get(i).get(s));
				out.println();
				}
			}
			//System.out.println("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||");
		}*/
		// }



		/*for(int i=0;i<ds.size();i++)
		   System.out.println(ds);*/

		//for(int i=0;i<t.size();i++)
		//System.out.println(t.get(i));
		//System.out.println(t.size());
		//out.println(t);
		//for(int i=0;i<t.size()-1;i++)
		//System.out.println(dif.add(TimeUnit.MILLISECONDS.toSeconds(t.get(i+1)-t.get(i))));
		//out.println(dif);
		//out.println(date);
		///out.println(busDate);
		//System.out.println(bus);
		//System.out.println(date);

		in.close();
		pr.close();
	}

	private static void mapdatebusid(String []parts)
	{
		final String dateStr = parts[DATE_INDEX];
		final String timeStr = parts[TIME_INDEX];
		HashSet<Integer> b=new HashSet<Integer>();
		try
		{
			SimpleDateFormat formatter1 = new SimpleDateFormat("hh:mm:ss");
			SimpleDateFormat formatter = new SimpleDateFormat("MM/dd/yyyy");
			Date dt1 = formatter.parse(dateStr);
			Date dt = formatter1.parse(timeStr);



			for(Date d:date)
			{
				//System.out.println(d);
				if(d.equals(dt1))
				{
					/*if(flag==0)
				{
					ds.get(d).put(Integer.parseInt(parts[5]),null);
				}*/
					busDate.get(d).add(Integer.parseInt(parts[5]));
					//ds.get(d).put(Integer.parseInt(parts[5]),null);
				}
			}





			//System.out.println(minutes);
			//,1/12/2015,7:19:58
			//final long timestamp = getTimestamp(dateStr, timeStr);
			//final long timestamp = getTimestamp( timeStr);


		} catch (Exception e) {
			e.printStackTrace();

		}
	}


	private static void mapbusshift(String[]parts)
	{
		/*System.out.println("Bus ID is "+parts[5]);
		System.out.println("Stop is "+parts[3]);
		System.out.println("Value of flag is "+flag);*/
		out.println("Bus ID is "+parts[5]);
		out.println("Stop is "+parts[3]);
		out.println("Value of flag is "+flag);
		final String dateStr = parts[DATE_INDEX];
		final String timeStr = parts[TIME_INDEX];
		HashSet<Integer> b=new HashSet<Integer>();
		try
		{
			SimpleDateFormat formatter1 = new SimpleDateFormat("hh:mm:ss");
			SimpleDateFormat formatter = new SimpleDateFormat("MM/dd/yyyy");
			Date dt1 = formatter.parse(dateStr);
			commonDate=dt1;
			Date dt = formatter1.parse(timeStr);


			if(ds.containsKey(dt1))

			{

				//System.out.println("first if"+dt1+Integer.parseInt(parts[5]));
				out.println("first if"+dt1+Integer.parseInt(parts[5]));
				//if(ds.get(dt1).containsKey(Integer.parseInt(parts[5])))
				if(ds.get(dt1).containsKey(657))
				{
					//System.out.println("second if"+ds.get(dt1));
					out.println("second if"+ds.get(dt1));
					//System.out.println("scnd if"+parts[3]);
					out.println("scnd if"+parts[3]);
					if(flag==1)
					{
						if(parts[3].equals("Stadium (A)")||parts[3].equals("Stadium ()"))
						{

							System.out.println("third if"+parts[3]);
							flag=0;
							//System.out.println("the bus ids"+ds.get(dt1).get(Integer.parseInt(parts[5])));
							out.println("the bus ids"+ds.get(dt1).get(Integer.parseInt(parts[5])));
							if(ds.get(dt1).get(Integer.parseInt(parts[5]))==null){
								//System.out.println("timestr allocated\n");
								out.println("timestr allocated\n");
								ds.get(dt1).put(Integer.parseInt(parts[5]),new HashMap<String,ArrayList<String>>());}
							ds.get(dt1).get(Integer.parseInt(parts[5])).put(timeStr,null);
							if(ds.get(dt1).get(Integer.parseInt(parts[5])).get(timeStr)==null){
								//System.out.println("Stop allocated\n");
								ds.get(dt1).get(Integer.parseInt(parts[5])).put(timeStr, new ArrayList<String>());}
							ds.get(dt1).get(Integer.parseInt(parts[5])).get(timeStr).add("Stadium (A)");

						}
						else// else of flag=0 when (not stadium(A))
						{
							flag=0;
							if(ds.get(dt1).get(Integer.parseInt(parts[5]))!=null){
								long min=99999;
								String ky=null;
								//System.out.println("keyset is "+ds.get(dt1).get(Integer.parseInt(parts[5])).keySet());
								out.println("keyset is "+ds.get(dt1).get(Integer.parseInt(parts[5])).keySet());
								for(String k : ds.get(dt1).get(Integer.parseInt(parts[5])).keySet())
								{
									out.println("parts[8] is "+parts[8]);
									SimpleDateFormat f1 = new SimpleDateFormat("hh:mm:ss");
									Date df1 = f1.parse(k);
									Long tf1 = new Long(df1.getTime());
									long sf1 = TimeUnit.MILLISECONDS.toSeconds(tf1);

									SimpleDateFormat f2 = new SimpleDateFormat("hh:mm:ss");
									Date df2 = f2.parse(parts[8]);
									Long tf2 = new Long(df2.getTime());
									long sf2 = TimeUnit.MILLISECONDS.toSeconds(tf2);

									if(sf2-sf1<min){
										ky=k;
										//System.out.println("key selected"+ky);
										out.println("sf2"+sf2);
										out.println("sf1"+sf1);
										out.println("key selected"+ky);
										min=sf2-sf1;
										//System.out.println("difference"+min);
										out.println("difference"+min);
									}


								}
								if(ky!=null){
									ds.get(dt1).get(Integer.parseInt(parts[5])).get(ky).add(parts[3]);
								}
								//System.out.println(ds.get(dt1).get(Integer.parseInt(parts[5])).get(ds.get(dt1).get(Integer.parseInt(parts[5]))));
								out.println(ds.get(dt1).get(Integer.parseInt(parts[5])).get(ds.get(dt1).get(Integer.parseInt(parts[5]))));
							}

						}
					}
					else//if of flag=1
					{
						//System.out.println("In the else\n");
						out.println("In the else\n");
						//System.out.println("second if in else"+ds.get(dt1));
						out.println("second if in else"+ds.get(dt1));
						//if(flag==0 && !parts[3].equals("Stadium (A)"))
						if(flag==0)
							//while(flag==0 && !parts[3].equals("Stadium (A)"))
						{
							if(parts[3].equals("Stadium (A)")||parts[3].equals("Stadium ()"))
							{
								flag=1;
							}
							else{

								//ds.get(dt1).get(Integer.parseInt(parts[5])).get(timeStr).add(parts[3]);
								/*if(ds.get(dt1).get(Integer.parseInt(parts[5]))==null)
									ds.get(dt1).put(Integer.parseInt(parts[5]),new HashMap<String,ArrayList<String>>());
								ds.get(dt1).get(Integer.parseInt(parts[5])).put(timeStr,null);
								if(ds.get(dt1).get(Integer.parseInt(parts[5])).get(timeStr)==null)
									ds.get(dt1).get(Integer.parseInt(parts[5])).put(timeStr, new ArrayList<String>());
								ds.get(dt1).get(Integer.parseInt(parts[5])).get(timeStr).add(parts[3]);*/
								if(ds.get(dt1).get(Integer.parseInt(parts[5]))!=null){
									long min=99999;
									String ky=null;
									//System.out.println("keyset is "+ds.get(dt1).get(Integer.parseInt(parts[5])).keySet());
									out.println("keyset is "+ds.get(dt1).get(Integer.parseInt(parts[5])).keySet());
									for(String k : ds.get(dt1).get(Integer.parseInt(parts[5])).keySet())
									{
										out.println("parts[8] is "+parts[8]);
										SimpleDateFormat f1 = new SimpleDateFormat("hh:mm:ss");
										Date df1 = f1.parse(k);
										Long tf1 = new Long(df1.getTime());
										long sf1 = TimeUnit.MILLISECONDS.toSeconds(tf1);

										SimpleDateFormat f2 = new SimpleDateFormat("hh:mm:ss");
										Date df2 = f2.parse(parts[8]);
										Long tf2 = new Long(df2.getTime());
										long sf2 = TimeUnit.MILLISECONDS.toSeconds(tf2);

										if(sf2-sf1<min){
											ky=k;
											out.println("sf2"+sf2);
											out.println("sf1"+sf1);
											//System.out.println("key selected"+ky);
											out.println("key selected"+ky);
											min=sf2-sf1;
											//System.out.println("difference"+min);
											out.println("difference"+min);
										}


									}
									if(ky!=null){
										ds.get(dt1).get(Integer.parseInt(parts[5])).get(ky).add(parts[3]);
									}
									//System.out.println(ds.get(dt1).get(Integer.parseInt(parts[5])).get(ds.get(dt1).get(Integer.parseInt(parts[5]))));
									out.println(ds.get(dt1).get(Integer.parseInt(parts[5])).get(ds.get(dt1).get(Integer.parseInt(parts[5]))));
								}


							}
							//mapbusshift(in.nextLine().split(","));
						}
					}

				}
				else
					ds.get(dt1).put(Integer.parseInt(parts[5]),null);


			}



		}
		catch(Exception e)
		{
			e.printStackTrace();
		}



	}

	private static void BusId_Date_Map(String[] str)
	{


	}

	private static HashSet<Integer> BusID (Integer id)
	{
		HashSet<Integer> bus=new HashSet<Integer>();
		bus.add(id);
		return bus; 
	}

	private static String[] splitLine(final String line) {
		return line.split(",");
	}

	private static long getTimestamp( final String timeStr) {
		final SimpleDateFormat dateFormatter = new SimpleDateFormat("MM/dd/yyyy");
		final SimpleDateFormat timeFormatter = new SimpleDateFormat("hh:mm:ss");
		try {
			return dateFormatter.parse(timeStr).getTime() ;//+ timeFormatter.parse(timeStr).getTime();
		} catch (ParseException e) {
			e.printStackTrace();
			return 0;
		}
	}
	
	
	private static JSONObject mapJson1( String[] parts)
	{
		final JSONObject obj = new JSONObject();
		String busId="636";
		try {
			obj.putOpt(busId,ds.get(commonDate).get(Integer.parseInt(busId)) );
		} catch (NumberFormatException | JSONException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return obj;
	}

	private static JSONObject mapJson(final String[] parts) {
		final JSONObject obj = new JSONObject();
		final String dateStr = parts[DATE_INDEX];
		final String timeStr = parts[TIME_INDEX];
		try
		{
			SimpleDateFormat formatter1 = new SimpleDateFormat("hh:mm:ss");
			SimpleDateFormat formatter = new SimpleDateFormat("MM/dd/yyyy");
			Date dt1 = formatter.parse(dateStr);
			Date dt = formatter1.parse(timeStr);
			Long time = new Long(dt.getTime());
			long seconds = TimeUnit.MILLISECONDS.toSeconds(time);

			date.add(dt1);
			ArrayList<String>s1=new ArrayList<String>();
			Map<String,ArrayList<String>> m1=new HashMap<String,ArrayList<String>>();
			m1.put(null,s1);

			Map<Integer,Map<String,ArrayList<String>>>m2=new HashMap<Integer,Map<String,ArrayList<String>>>();
			m2.put(null,m1);
			//Map<Date,Map<Integer,Map<Long,ArrayList<String>>>> m3=new HashMap<Date,Map<Integer,Map<Long,ArrayList<String>>>>();
			ds.put(dt1, m2);
			busDate.put(dt1, new HashSet<Integer>());
			//busDate.put(dt1,Map<Date,Map<Integer,Map<Long,ArrayList<String>>>>);
			//System.out.println(minutes);
			//,1/12/2015,7:19:58
			//final long timestamp = getTimestamp(dateStr, timeStr);
			//final long timestamp = getTimestamp( timeStr);
			t.add(time);
			obj.put(TIMESTAMP, time);
		} catch (Exception e) {
			e.printStackTrace();
			return null;
		}

		final String busId = parts[5];

		try {
			obj.put("BusId", busId);
		} catch (JSONException e) {
			e.printStackTrace();
			return null;
		}
		return obj;
	}

	private static final int DATE_INDEX = 7;
	private static final int TIME_INDEX = 8;

	private static final String TIMESTAMP = "timestamp";
}
