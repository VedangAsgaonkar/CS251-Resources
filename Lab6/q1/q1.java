public class q1
{
    public static void main(String[] args)
    {
        double s = 0,p = 1;
        int n = args.length;
        System.out.print(n+",");
        for(int i = 0; i<n;i++){
            s+= Double.parseDouble(args[i]);
            p*= Double.parseDouble(args[i]);
        }
        System.out.print(s+","+p);

    }   
}
