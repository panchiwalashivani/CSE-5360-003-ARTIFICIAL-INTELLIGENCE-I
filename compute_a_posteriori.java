import java.io.*;

public class compute_a_posteriori {

public static void main(String[] args) throws IOException {
        
		
	  Hypo h1= new Hypo(0.10000,1.00000,0.00000);
        Hypo h2= new Hypo(0.20000,0.75000,0.25000);
        Hypo h3= new Hypo(0.40000,0.50000,0.50000);
        Hypo h4= new Hypo(0.20000,0.25000,0.75000);
        Hypo h5= new Hypo(0.10000,0.00000,1.00000);

		File file=new File("Result.txt");
		BufferedWriter bw=new BufferedWriter(new FileWriter(file));
		String observation_string=args[0];
		String[] inputArray=observation_string.split("");
		
        bw.write("Observation Sequence :");
        bw.write(observation_string);
        bw.newLine();
        
        bw.write("Length of Q :");
        bw.write(observation_string.length());
        bw.newLine();
        bw.newLine();
        
		
        double c0,l0 = 0.0;    
        double newPrior=0.0;
	

   for(int i=0;i<inputArray.length;i++)
	{
			c0 = ((h1.prior * h1.cherry) + (h2.prior * h2.cherry) + (h3.prior * h3.cherry) + (h4.prior * h4.cherry) + (h5.prior * h5.cherry));
			l0 = 1-c0;
			

	try {
		
		if(observation_string.charAt(i)=='C'){
			
			newPrior=((h1.cherry*h1.prior)/c0);
			h1.prior=newPrior;
			newPrior=((h2.cherry*h2.prior)/c0);
			h2.prior=newPrior;
			newPrior=((h3.cherry*h3.prior)/c0);
			h3.prior=newPrior;
			newPrior=((h4.cherry*h4.prior)/c0);
			h4.prior=newPrior;
			newPrior=((h5.cherry*h5.prior)/c0);
			h5.prior=newPrior;
			
		}
	
		else if(observation_string.charAt(i)=='L'){
			
				newPrior=((h1.lime*h1.prior)/l0);
				h1.prior=newPrior;
				newPrior=((h2.lime*h2.prior)/l0);
				h2.prior=newPrior;
				newPrior=((h3.lime*h3.prior)/l0);
				h3.prior=newPrior;
				newPrior=((h4.lime*h4.prior)/l0);
				h4.prior=newPrior;
				newPrior=((h5.lime*h5.prior)/l0);
				h5.prior=newPrior;
				
			}
		
		bw.write("After Observation "+(i+1)+ " = " + String.valueOf(observation_string.charAt(i)) +":");
        bw.newLine();
        
		bw.write("P(h1 | Q) =\t");
        bw.write(String.valueOf(round(h1.prior,5)));
        bw.newLine();
        
        bw.write("P(h2 | Q) =\t");
        bw.write(String.valueOf(round(h2.prior,5)));
        bw.newLine();
        
        bw.write("P(h3 | Q) =\t");
        bw.write(String.valueOf(round(h3.prior,5)));
        bw.newLine();
        
        bw.write("P(h4 | Q) =\t");
        bw.write(String.valueOf(round(h4.prior,5)));
        bw.newLine();
        
        bw.write("P(h5 | Q) =\t");
        bw.write(String.valueOf(round(h5.prior,5)));
        bw.newLine();
        bw.newLine();
        
        bw.write("Probability that the next candy will be Cherry, given Q:"+ round(c0,5) +"\n");
        bw.write("Probability that the next candy will be Lime, given Q:"+ round(l0,5) + "\n");
        
        bw.newLine();
        bw.newLine();
        
		}
 
	 	catch(Exception e){
			System.out.println("Error!");
	    }

		}
   
	bw.close();
	System.out.println("Result.txt is generated");
}

	public static double round(double val, int places)
	{
	    if (places < 0) throw new IllegalArgumentException();
	
	    long factor = (long) Math.pow(10, places);
	    val = val * factor;
	    long tmp = Math.round(val);
	    return (double) tmp / factor;
	
    }
	
	
}