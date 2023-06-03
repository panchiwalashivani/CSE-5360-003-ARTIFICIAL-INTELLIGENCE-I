
public class Hypo {
	
	public double prior;
	public double cherry;
	public double lime;
	
	public Hypo(double prior, double cherry, double lime)
	{
		round(prior,5);
		this.prior=prior;
		round(cherry,5);
		this.cherry=cherry;
		round(lime,5);
		this.lime=lime;
	}
	
	public static double round(double val, int place)
	{
	    if (place < 0) throw new IllegalArgumentException();

	    long factor = (long) Math.pow(10, place);
	    val = val * factor;
	    return (double) val / factor;
	}
	
}