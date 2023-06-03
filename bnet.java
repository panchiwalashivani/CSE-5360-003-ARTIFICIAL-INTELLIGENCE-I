import java.util.ArrayList;

public class bnet {
	static ArrayList<String> den_array = new ArrayList<String>();//denominator array
	static ArrayList<String> num_array = new ArrayList<String>();//numerator array
	static double B= 0.001; 
	static double E= 0.002;
	static double A[]= {0.95,0.94,0.29,0.001}; 
	static double J[]= {0.90,0.05};
	static double M[]= {0.70,0.01};

	public static void main(String[] args) {

		int B_Counter=0,E_Counter=0,A_Counter=0,J_Counter=0,M_Counter=0;
		if (args.length < 1 || args.length > 6) { 
			System.exit(0);//exit when the given arguments are more than 6 or less than 1
		}
		int index =-1;
		for(int i=0;i < args.length;i++) { 
			if(args[i].equals("given")){
				index=0;
				continue;
			}if(index==-1) {
				num_array.add(args[i]);//storing arguments given before "given" in num_array
			}
			else
			{
				den_array.add(args[i]);//storing arguments given before "given" in den_array
			}

		}	
		if (num_array.size() <1 || num_array.size() > 6) { 
			System.exit(0);//checking if number of arguments are greater than 1 and less than 7 
		}
		if(index==0) {
			if (den_array.size() <1 || den_array.size() > 4) {
				System.exit(0);//checking if number of arguments are greater than 1 and less than 7
			}		
		}

		System.out.println(num_array + "given" + den_array);
		num_array.addAll(den_array); //append num_array with den_array elements

		for(int i=0;i< num_array.size();i++) {  
			if (!num_array.contains("Bt")&&!num_array.contains("Bf")) {
				num_array.add("Bt");
				num_array.add("Bf");
				B_Counter=1;
			}
			if (!num_array.contains("Et")&&!num_array.contains("Ef")) {
				num_array.add("Et");
				num_array.add("Ef");
				E_Counter=1;
			}
			if (!num_array.contains("At")&&!num_array.contains("Af")) {
				num_array.add("At");
				num_array.add("Af");
				A_Counter=1;}
			if (!(num_array.contains("Jt"))&&!num_array.contains("Jf")) {
				num_array.add("Jt");
				num_array.add("Jf");
				J_Counter=1;
			}
			if (!num_array.contains("Mt")&&!num_array.contains("Mf")) {
				num_array.add("Mt");
				num_array.add("Mf");
				M_Counter=1;}}

		double numerator = callCompute(B_Counter, E_Counter, A_Counter, J_Counter, M_Counter, num_array);
		if(den_array.size()==0) {
			System.out.println("Computed Probability: "+numerator);
		}
		B_Counter=E_Counter=A_Counter=J_Counter=M_Counter=0;
		for(int j=0;j< den_array.size();j++) {
			if (!den_array.contains("Bt")&&!den_array.contains("Bf")) {
				den_array.add("Bt");
				den_array.add("Bf");
				B_Counter=1;}
			if (!den_array.contains("Et")&&!den_array.contains("Ef")) {
				den_array.add("Et");
				den_array.add("Ef");
				E_Counter=1;}
			if (!den_array.contains("At")&&!den_array.contains("Af")) {
				den_array.add("At");
				den_array.add("Af");
				A_Counter=1;}
			if (!den_array.contains("Jt")&&!den_array.contains("Jf")) {
				den_array.add("Jt");
				den_array.add("Jf");
				J_Counter=1;}
			if (!den_array.contains("Mt")&&!den_array.contains("Mf")) {
				den_array.add("Mt");
				den_array.add("Mf");
				M_Counter=1;}}
		double denominator = callCompute(B_Counter, E_Counter, A_Counter, J_Counter, M_Counter, den_array);
		if(den_array.size()>0) {
			System.out.println("Computed Probability: "+numerator/denominator);
		}
	}

	public static double callCompute(int bc,int ec,int ac,int jc,int mc,ArrayList<String> arrayProc) {
		double probability=0.0;
		Boolean b_bool=false,e_bool=false,a_bool=false,j_bool=false,m_bool=false;
		if(bc==0) {
			if(arrayProc.contains("Bt")) {
				b_bool=true;
			}
			else b_bool=false;
		}
		if(ec==0) {
			if(arrayProc.contains("Et")) {
				e_bool=true;
			}
			else e_bool=false;
		}
		if(ac==0) {
			if(arrayProc.contains("At")) {
				a_bool=true;
			}
			else a_bool=false;
		}
		if(jc==0) {
			if(arrayProc.contains("Jt")) {
				j_bool=true;
			}
			else j_bool=false;
		}
		if(mc==0) {
			if(arrayProc.contains("Mt")) {
				m_bool=true;
			}
			else m_bool=false;
		}
		for(int i1=0;i1<=bc;i1++) {
			for(int i2=0;i2<=ec;i2++) {
				for(int i3=0;i3<=ac;i3++) {
					for(int i4=0;i4<=jc;i4++) {
						for(int i5=0;i5<=mc;i5++) {
							probability+=computeProbability(b_bool, e_bool, a_bool, j_bool, m_bool);
							if(mc==1 && m_bool==false) m_bool=true;
							else if(mc==1 && m_bool==true) m_bool=false;
						}
						if(jc==1 && j_bool==false) j_bool=true;
						else if(jc==1 && j_bool==true) j_bool=false;
					}
					if(ac==1 && a_bool==false) a_bool=true;
					else if(ac==1 && a_bool==true) a_bool=false;
				}
				if(ec==1 && e_bool==false) e_bool=true;
				else if(ec==1 && e_bool==true) e_bool=false;
			}
			if(bc==1 && b_bool==false) b_bool=true;
			else if(bc==1 && b_bool==true) b_bool=false;
		}
		return probability;
	}

	public static double computeProbability(boolean b, boolean e, boolean a, boolean j, boolean m) {
		double Bval=0.0;
		if(b) {
			Bval=B;}
		else {
			Bval = 1-B;}
		double Eval;
		if(e) {
			Eval=E;}
		else {
			Eval = 1-E;}
		double Aval = 0.0;
		if(a) {
			if(b==true && e==true )
				Aval = A[0];
			else if(b==true && e==false )
				Aval = A[1];
			else if(b==false && e==true )
				Aval = A[2];
			else if(b==false && e==false )
				Aval = A[3];}
		else
		{
			if(b==true && e==true )
				Aval = 1-A[0];
			else if(b==true && e==false )
				Aval = 1-A[1];
			else if(b==false && e==true )
				Aval = 1-A[2];
			else if(b==false && e==false )
				Aval = 1-A[3];}

		double Jval = 0.0;
		if(j) {
			if(a==true)
				Jval = J[0];
			else if(a==false )
				Jval = J[1];}

		else
		{
			if(a==true)
				Jval =1-J[0];
			else if(a==false )
				Jval =1-J[1];}

		double Mval = 0.0;
		if(m) {
			if(a==true)
				Mval = M[0];
			else if(a==false )
				Mval = M[1];}

		else
		{
			if(a==true)
				Mval =1-M[0];
			else if(a==false )
				Mval =1-M[1];
		}
		return Bval*Eval*Aval*Jval*Mval; 
	}

}